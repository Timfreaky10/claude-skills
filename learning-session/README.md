# learning-session

Skill Claude — suivi des sessions d'apprentissage (log Obsidian, curriculum, synchro TickTick).

## Dépendance

Ce skill ne porte **que la procédure**. Il ne connaît aucun cours : chemins, emojis, tags, wikilinks,
projets et IDs TickTick vivent dans le vault, non versionnés ici :

```
02_Learning/
├── _registre.md          un bloc par cours — source de vérité
└── _templates/
    ├── log.md            gabarit du log de session
    └── curriculum.md     procédure de mise à jour du curriculum
```

Sans `02_Learning` accessible (monté dans Cowork, ou lisible sur le disque dans Claude Code), le skill
s'arrête à l'étape 0 et le signale.

## Principe

Le **nom** du projet TickTick fait foi, les IDs ne sont qu'un cache : si un ID échoue, le skill
re-résout par nom et réécrit le registre. Tout ce qu'il crée (colonne, tâche récurrente, curriculum)
est inscrit au registre dans la même session — c'est ce qui empêche les données de pourrir.

## Installation

- **Claude Code** — fait partie du dépôt `Timfreaky10/claude-skills`, cloné dans `~/.claude/skills/` :
  chargé automatiquement comme `learning-session@skills-dir` à la session suivante.
- **Compte Claude (Cowork)** — copier `skills/learning-session/SKILL.md` dans les skills du compte, ou zipper le
  dossier `skills/learning-session/` en `.skill` et l'importer.

## Historique

- **2026-09-14** — versionné dans `claude-skills` au format plugin ; étape 0 et section « Emplacements »
  adaptées pour tourner aussi dans Claude Code, où rien n'est monté sous `$HOME/mnt/`.

- **2026-09-14** — refonte : chemins Windows, emojis, tags et IDs TickTick descendus dans
  `02_Learning/_registre.md` ; gabarits extraits ; résolution TickTick par nom avec écriture en
  retour. IDs vérifiés contre TickTick à cette date.
