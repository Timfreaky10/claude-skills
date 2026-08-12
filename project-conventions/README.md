# project-conventions

Plugin personnel (skills-directory, pas de marketplace) qui porte deux
disciplines nées sur GameTracker vers n'importe quel nouveau projet :
écrire le journal au bon moment (par sujet, pas par date), et valider un
mockup avant tout code d'implémentation visuelle.

## Skills

- **`bootstrap`** — à lancer une fois, au démarrage d'un projet, pour créer
  `docs/journal/journal.md` (+ `docs/mockups/` si le projet a un frontend)
  et écrire les conventions correspondantes dans son `CLAUDE.md`.
- **`dev-journal`** — usage courant, ensuite : écrit l'entrée de journal au
  moment de clore un chantier, en lisant la convention (fichier unique ou
  table sujet→fichier) déjà établie dans le CLAUDE.md du projet courant.
- **`mockup-first`** — usage courant, ensuite : impose un mockup HTML validé
  avant tout code frontend, sur les projets qui ont un dossier
  `docs/mockups/`.

Contrairement aux skills scoped `gametracker-journal` et
`gametracker-mockup-first` (dans le repo GameTracker lui-même), ceux-ci ne
codent aucune spécificité de projet en dur — ils lisent la convention
propre à chaque projet dans son CLAUDE.md.

Chargé automatiquement à chaque session Claude Code (`project-conventions@skills-dir`),
sur n'importe quel projet — pas d'installation par projet nécessaire.
