---
name: journal-obsidian
description: >
  Workflow complet pour le journal Obsidian de Tim : créer ou compléter une note daily à partir
  d'une dictée Wispr, générer la revue hebdomadaire en fin de semaine, et mettre à jour les notes
  thématiques (Relationnel, Travail & Projets, Énergie & Sport, Nutrition & Corps).
  Utilise ce skill dès que Tim mentionne le journal, un daily, une revue hebdo, une note thématique,
  ou qu'il dicte des infos sur sa journée (réveil, repas, sport, humeur). Aussi utile pour corriger
  une note, compléter une section manquante, ou mettre à jour CLAUDE.md après un changement d'état.
---

# Journal Obsidian — procédure

Ce skill porte la **procédure**. Tout ce qui est propre au vault — gabarits, conventions de format,
arborescence, état du projet — vit dans le dossier projet `Journal/` et se lit **au moment où on en a
besoin**. Ne rien recopier ici : si un détail change, il change là-bas.

| Fichier du dossier projet | Contenu | Quand le lire |
|---|---|---|
| `Journal/CLAUDE.md` | état courant, contexte narratif actif, points ouverts | **toujours, en premier** |
| `Journal/conventions.md` | règles d'écriture (dates, sommeil, nourriture, Wispr, sport, météo…) | **toujours, avant d'écrire** |
| `Journal/templates/daily.md` | gabarit + règles de remplissage du daily | workflow Daily |
| `Journal/templates/weekly.md` | gabarit + calculs du weekly | workflow Weekly |
| `Journal/templates/thematic.md` | carte des notes thématiques et quoi va où | workflow Thématiques |
| `Journal/CHANGELOG.md` | historique des sessions | seulement si on cherche « qu'est-ce qui s'est passé le … » |

## Étape 0 — résoudre les chemins

Dossiers attendus : `01_Journal`, `04_Notes`, `02_Learning`, `Journal`. Où les trouver dépend de
l'environnement — **déterminer lequel avant tout accès fichier** :

- **Cowork** — les dossiers sont montés sous `$HOME/mnt/<nom>` et **le chemin complet change à chaque
  session** : lister `$HOME/mnt/`, ne jamais coder un chemin de session en dur.
- **Claude Code** — rien n'est monté (`$HOME/mnt/` n'existe pas) : les dossiers se lisent directement à
  leur emplacement Proton Drive, voir « Emplacements » ci-dessous.

Si un dossier nécessaire manque (`02_Learning` manque souvent) : **le dire à Tim et s'arrêter là pour
cette partie**. Ne pas deviner un chemin, ne pas valider un wikilink qu'on n'a pas pu vérifier — le
reprendre tel quel et le signaler.

## Emplacements, et démarrer sur une autre machine

Tout vit dans **Proton Drive**, synchronisé sur toutes les machines de Tim. Chemins typiques (Windows) :
- `…\Proton Drive\tim-mcgarry\My files\Claude\Projects\Journal` → dossier `Journal`
- `…\Proton Drive\tim-mcgarry\My files\Obisidian Vault\Obsidian Vault\Tim's Vault\` → `01_Journal`,
  `04_Notes`, `02_Learning`

Le `…` est en général le dossier utilisateur : `$HOME/Proton Drive/…` en bash,
`%USERPROFILE%\Proton Drive\…` sous Windows.

Selon l'environnement :
- **Cowork** — sur un ordinateur neuf, `$HOME/mnt/` est vide : rien n'est connecté par défaut. Demander
  l'accès aux dossiers manquants (`device_request_folder_access`).
- **Claude Code** — lire ces chemins directement. S'ils sont hors du répertoire de travail de la
  session, l'accès peut demander une autorisation : la demander, plutôt que de conclure que le dossier
  n'existe pas.

Si le chemin échoue — autre nom d'utilisateur, macOS, arborescence différente — **demander à Tim** plutôt
que d'essayer des variantes.

⚠️ **Synchronisation** : Proton Drive peut laisser des fichiers non téléchargés. Un dossier qui paraît
vide ou un fichier de taille nulle peut être un fichier non synchronisé, pas une absence. Dans le doute,
le dire à Tim au lieu de conclure que la donnée n'existe pas.

## Étape 1 — lire l'état

`Journal/CLAUDE.md` puis `Journal/conventions.md`. Évite les doublons, les contradictions avec ce qui
est déjà écrit, et les fils narratifs qu'on croirait ouverts alors qu'ils sont clos.

## Routing

| Tim dit… | Workflow | Template à lire |
|---|---|---|
| "on fait le daily", dicte sa journée | Daily | `templates/daily.md` |
| "on complète le daily du [date]", section manquante | Daily (complétion) | `templates/daily.md` |
| "revue de la semaine", "on fait le W28" | Weekly | `templates/weekly.md` |
| "mets à jour [note]", info relationnelle / pro / corporelle | Thématiques | `templates/thematic.md` |
| "mets à jour CLAUDE.md" | voir « Après écriture » | — |

## Daily

1. Identifier la date (aujourd'hui, ou explicite : « le daily du 11 »)
2. Si le fichier existe, **le lire avant de le modifier**
3. Écrire selon le gabarit

Tim dicte souvent en **deux passes** — matin (sommeil, intentions) puis soir (le reste). À la passe du
soir, ne compléter que les champs vides : ne jamais écraser une donnée existante sans vérifier.

Ce qui n'a pas été dicté reste vide. Demander plutôt qu'inventer ; les inférences qui rendent le
journal faux à la relecture sont le seul vrai risque ici.

## Weekly

1. **Lundi** : créer le stub de la semaine qui commence (voir le gabarit — la fenêtre météo ne pardonne
   pas le retard)
2. **Fin de semaine** : lire tous les dailies de lundi à dimanche, calculer, rédiger

Préserver **verbatim** les blocs déjà remplis par les scripts (tableau météo, Samsung Health) — ils ne
se régénèrent pas.

Une semaine mal documentée se **signale** (encadré en tête, nombre de dailies sources), elle ne se
lisse pas : une moyenne sur un seul jour n'est pas une moyenne.

## Thématiques

Lire la note avant d'écrire, ajouter en tête de section, ne pas contredire le contexte narratif de
`CLAUDE.md`. Le détail des règles est dans `conventions.md`.

## Après écriture

- **TickTick** : identifier ce qui mérite un suivi (idée à concrétiser, observation santé à confirmer,
  achat, rappel) et **proposer une liste de tâches** — Tim valide avant création.
- **`Journal/CLAUDE.md`** : mettre à jour l'état courant, les points ouverts et le contexte narratif
  **actif**. Y retirer ce qui vient de se clore.
- **`Journal/CHANGELOG.md`** : y consigner le compte rendu de la session — corrections, anomalies,
  écarts constatés. Ce récit va là, **pas** dans `CLAUDE.md`, qui doit rester court.
