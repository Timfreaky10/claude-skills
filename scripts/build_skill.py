"""Construit l'archive .skill d'un skill du dépôt, prête à téléverser dans un compte Claude.

Un téléversement de compte attend UN skill par archive, structurée ainsi :

    <nom>/
    <nom>/SKILL.md
    <nom>/...          (fichiers annexes éventuels du skill)

Le script prend donc un dossier de skill (celui qui contient SKILL.md), pas un plugin :
un plugin comme project-conventions en regroupe plusieurs, chacun s'extrait séparément.

Usage :
    python scripts/build_skill.py journal-obsidian
    python scripts/build_skill.py journal-obsidian learning-session --out ~/Downloads
    python scripts/build_skill.py project-conventions/skills/dev-journal

Garde-fous :
- refuse de construire depuis un dossier qui a des modifications non committées — le dépôt
  est la source unique, une archive doit correspondre à un état qui existe dans git
  (--allow-dirty pour passer outre en connaissance de cause) ;
- vérifie que le `name:` du SKILL.md correspond au nom du dossier ;
- relit l'archive produite et compare chaque fichier octet pour octet avec la source.
"""

import argparse
import subprocess
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
IGNORED = {"__pycache__", ".DS_Store", "Thumbs.db"}

# Sous Windows, Python < 3.15 écrit dans l'encodage local quand la sortie passe par un tuyau :
# les accents des messages arriveraient abîmés. Forcer l'UTF-8.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")


def fail(message: str) -> None:
    print(f"ERREUR : {message}", file=sys.stderr)
    sys.exit(1)


def resolve_skill_dir(arg: str) -> Path:
    """Accepte un chemin vers un dossier de skill, ou un simple nom de skill."""
    candidate = Path(arg).expanduser()
    if not candidate.is_absolute():
        candidate = (REPO / candidate) if not candidate.exists() else candidate.resolve()
    if candidate.is_dir() and (candidate / "SKILL.md").is_file():
        return candidate.resolve()

    matches = sorted(p.parent for p in REPO.glob(f"*/skills/{arg}/SKILL.md"))
    if not matches:
        fail(f"aucun skill « {arg} » dans le dépôt (cherché : */skills/{arg}/SKILL.md).")
    if len(matches) > 1:
        found = ", ".join(str(m.relative_to(REPO)) for m in matches)
        fail(f"plusieurs skills s'appellent « {arg} » : {found}. Donner le chemin complet.")
    return matches[0]


def frontmatter_name(skill_md: Path) -> str:
    lines = skill_md.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        fail(f"{skill_md} ne commence pas par un bloc frontmatter (---).")
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip().strip("'\"")
    fail(f"{skill_md} n'a pas de champ `name:` dans son frontmatter.")


def git(*args: str) -> str:
    result = subprocess.run(["git", "-C", str(REPO), *args], capture_output=True, text=True)
    if result.returncode != 0:
        fail(f"git {' '.join(args)} a échoué : {result.stderr.strip()}")
    return result.stdout.strip()


def skill_files(skill_dir: Path) -> list[Path]:
    return sorted(
        p for p in skill_dir.rglob("*")
        if p.is_file() and not any(part in IGNORED for part in p.relative_to(skill_dir).parts)
    )


def build(skill_dir: Path, out_dir: Path, allow_dirty: bool) -> Path:
    name = skill_dir.name
    rel = skill_dir.relative_to(REPO)

    declared = frontmatter_name(skill_dir / "SKILL.md")
    if declared != name:
        fail(f"{rel}/SKILL.md déclare `name: {declared}` mais le dossier s'appelle « {name} ».")

    dirty = git("status", "--porcelain", "--", str(rel))
    if dirty and not allow_dirty:
        fail(
            f"{rel} a des modifications non committées :\n{dirty}\n"
            "Committer d'abord (l'archive doit correspondre à un état du dépôt), "
            "ou relancer avec --allow-dirty."
        )

    files = skill_files(skill_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    archive = out_dir / f"{name}.skill"

    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(f"{name}/", "")
        for f in files:
            # as_posix() : séparateurs « / » dans l'archive, quel que soit l'OS.
            z.write(f, f"{name}/{f.relative_to(skill_dir).as_posix()}")

    # Relecture : chaque fichier de l'archive doit être identique à sa source.
    with zipfile.ZipFile(archive) as z:
        members = [m for m in z.namelist() if not m.endswith("/")]
        if len(members) != len(files):
            fail(f"{archive.name} contient {len(members)} fichiers, {len(files)} attendus.")
        for f in files:
            if z.read(f"{name}/{f.relative_to(skill_dir).as_posix()}") != f.read_bytes():
                fail(f"{archive.name} : {f.name} ne correspond pas à la source.")

    commit = git("rev-parse", "--short", "HEAD")
    state = " + modifications non committées" if dirty else ""
    print(f"OK  {archive}  ({len(files)} fichier(s), commit {commit}{state}, vérifié octet pour octet)")
    return archive


def main() -> None:
    parser = argparse.ArgumentParser(description="Construit des archives .skill depuis le dépôt.")
    parser.add_argument("skills", nargs="+", help="nom de skill, ou chemin vers son dossier")
    parser.add_argument("--out", default=str(REPO / "dist"), help="dossier de sortie (défaut : dist/)")
    parser.add_argument("--allow-dirty", action="store_true", help="accepter des modifications non committées")
    args = parser.parse_args()

    out_dir = Path(args.out).expanduser().resolve()
    for arg in args.skills:
        build(resolve_skill_dir(arg), out_dir, args.allow_dirty)


if __name__ == "__main__":
    main()
