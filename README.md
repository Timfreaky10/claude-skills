# claude-skills

Plugins Claude Code personnels (format "skills-directory" — `.claude-plugin/plugin.json` +
`skills/*/SKILL.md`), chargés automatiquement à chaque session Claude Code sur cette machine.

Ce dossier est directement `~/.claude/skills/` — l'emplacement que Claude Code scanne pour ce
type de plugin. Cloner ce repo à cet emplacement exact sur une nouvelle machine suffit à
retrouver tous les plugins listés ci-dessous, sans étape d'installation supplémentaire.

## Plugins

- **`project-conventions`** — discipline journal-avant-commit, mockup-avant-implémentation et
  graphe graphify interrogé par MCP avant de fouiller, réutilisable sur n'importe quel projet (bootstrap la structure dès le jour 1, puis applique
  la convention établie dans le CLAUDE.md de chaque projet). Née sur GameTracker, généralisée
  le 2026-08-12.
- **`journal-obsidian`** — procédure du journal Obsidian (daily dicté, revue hebdo, notes thématiques).
  Dépend du dossier projet `Journal/` et du vault, non versionnés ici.
- **`learning-session`** — suivi des sessions d'apprentissage (log Obsidian, curriculum, synchro
  TickTick). Dépend de `02_Learning/_registre.md` dans le vault, non versionné ici.

## Mise en place sur une nouvelle machine

```bash
git clone https://github.com/Timfreaky10/claude-skills.git ~/.claude/skills
```

Si `~/.claude/skills/` existe déjà avec du contenu sur cette machine, fusionner manuellement
plutôt qu'écraser.

### graphify (utilisé par `project-conventions`)

Le skill `graphify/` n'est **pas** versionné ici : `graphify install` le recopie depuis le paquet pip,
et il doit correspondre à la version installée. Sur chaque machine :

```bash
pip install graphifyy
graphify install
claude mcp add --scope user graphify -- graphify-mcp
```

Le serveur MCP se déclare une seule fois, au niveau utilisateur : il lit `graphify-out/graph.json`
du dossier où la session démarre. **Même version de graphify sur toutes les machines**, sinon le
cache d'extraction versionné dans chaque projet change de dossier et tout repasse au modèle.

## Construire un `.skill` pour un compte Claude

Claude Code lit ce dossier directement : rien à construire pour lui. Un compte Claude (Cowork, claude.ai)
garde en revanche une **copie figée** de chaque skill téléversé — après toute modification, il faut la
remplacer. `scripts/build_skill.py` produit l'archive à téléverser :

```bash
python scripts/build_skill.py journal-obsidian learning-session
```

- Prend un **nom de skill** ou le chemin de son dossier. Un plugin qui en regroupe plusieurs
  (`project-conventions`) s'extrait skill par skill : `python scripts/build_skill.py dev-journal`.
- Écrit dans `dist/` par défaut (`--out` pour un autre dossier) ; `dist/` et `*.skill` sont ignorés par git.
- **Refuse un skill qui a des modifications non committées** : l'archive doit correspondre à un état du
  dépôt (`--allow-dirty` pour passer outre). Relit ensuite l'archive et la compare octet pour octet à la
  source.

Côté compte, supprimer l'ancienne version du skill avant d'importer la nouvelle. Et ne jamais modifier un
skill directement dans le compte : la modification serait écrasée au réimport suivant.
