# claude-skills

Plugins Claude Code personnels (format "skills-directory" — `.claude-plugin/plugin.json` +
`skills/*/SKILL.md`), chargés automatiquement à chaque session Claude Code sur cette machine.

Ce dossier est directement `~/.claude/skills/` — l'emplacement que Claude Code scanne pour ce
type de plugin. Cloner ce repo à cet emplacement exact sur une nouvelle machine suffit à
retrouver tous les plugins listés ci-dessous, sans étape d'installation supplémentaire.

## Plugins

- **`project-conventions`** — discipline journal-avant-commit et mockup-avant-implémentation,
  réutilisable sur n'importe quel projet (bootstrap la structure dès le jour 1, puis applique
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
