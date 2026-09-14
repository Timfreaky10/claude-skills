# journal-obsidian

Skill Claude — procédure du journal Obsidian (daily, revue hebdo, notes thématiques).

## Dépendance

Ce skill ne porte **que la procédure**. Il lit ses gabarits et ses conventions dans le dossier projet
`Journal/` du vault, non versionné ici :

```
Journal/
├── CLAUDE.md        état courant + contexte narratif actif
├── conventions.md   règles d'écriture
├── CHANGELOG.md     historique des sessions
└── templates/
    ├── daily.md
    ├── weekly.md
    └── thematic.md
```

Installé seul, sans ce dossier accessible (monté dans Cowork, ou lisible sur le disque dans Claude Code),
le skill s'arrête à l'étape 0 et le signale.

## Installation

- **Claude Code** — fait partie du dépôt `Timfreaky10/claude-skills`, cloné dans `~/.claude/skills/` :
  chargé automatiquement comme `journal-obsidian@skills-dir` à la session suivante.
- **Compte Claude (Cowork)** — copier `skills/journal-obsidian/SKILL.md` dans les skills du compte, ou zipper le
  dossier `skills/journal-obsidian/` en `.skill` et l'importer.

## Historique

- **2026-09-14** — versionné dans `claude-skills` au format plugin ; étape 0 et section « Emplacements »
  adaptées pour tourner aussi dans Claude Code, où rien n'est monté sous `$HOME/mnt/`.

- **2026-09-14** — refonte : chemins de session en dur supprimés (résolution runtime), gabarits et
  conventions descendus dans le dossier projet, `references/` supprimé, compte rendu de session
  redirigé vers `CHANGELOG.md`.
