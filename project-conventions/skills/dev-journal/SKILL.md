---
name: dev-journal
description: >
  Écrire l'entrée de journal du projet courant au moment de clore un
  chantier — le commit qui termine une tâche, un bug ou une décision de
  conception — juste avant de committer. Utiliser ce skill à chaque fin de
  tâche sur un projet qui a été bootstrappé avec ces conventions (vérifier
  dans son CLAUDE.md, section "Conventions de travail"), même pour un
  correctif qui semble mineur. Détermine le bon fichier dans docs/journal/
  en lisant la convention du projet (fichier unique ou table sujet→fichier
  déjà établie), y écrit le récit détaillé, et ne laisse dans CLAUDE.md que
  la règle durable qui en découle, s'il y en a une.
---

# Journal de projet

## Quand

Au moment de clore un chantier — pas "quand on y pense", mais précisément
**avant le commit** qui termine une tâche, corrige un bug ou acte une
décision de conception. Rien d'autre dans la boucle de dev ne déclenche ça de
façon fiable.

## Choisir le fichier — lire la convention du projet, ne pas en inventer une

Ce skill est générique : il n'a pas de table de correspondance en dur, parce
que chaque projet a ses propres sujets récurrents. Avant d'écrire, lire la
section **"Conventions de travail"** du `CLAUDE.md` du projet courant :

- **Si elle ne mentionne qu'un fichier unique** (`docs/journal/journal.md`,
  typiquement un projet jeune bootstrappé récemment) : écrire là. Si ce
  fichier commence à accumuler **deux sujets récurrents distincts** (pas un
  cas isolé — un vrai motif qui revient), proposer à Tim de le scinder par
  sujet en plusieurs fichiers et d'ajouter la table correspondante dans
  CLAUDE.md, plutôt que de continuer à tout empiler dans un seul fichier
  grossissant sans structure.
- **Si une table sujet → fichier existe déjà** dans CLAUDE.md : l'utiliser,
  en choisissant par **sujet de l'entrée, jamais par date de travail** — un
  chantier du jour peut très bien toucher un sujet déjà établi ailleurs.
  Historique réel qui a motivé cette règle sur un projet cousin (GameTracker) :
  un bug de matching avait atterri dans le fichier du chantier du jour plutôt
  que dans celui de tous les autres bugs du même type — historique coupé en
  deux, invisible pour qui rouvre le fichier "évident".
- **Si le sujet ne correspond clairement à aucune entrée de la table** :
  demander à Tim où le ranger plutôt que de deviner.

**Départage quand un bug touche à la fois une source/cause et son affichage**
(ex. un calcul faux dans une couche de données, visible ensuite dans un
écran) : classer par la **cause**, pas par l'écran où le symptôme apparaît.

## Ce qui va où

Deux textes différents, jamais un seul dupliqué à deux endroits :

- **Dans le fichier de journal choisi ci-dessus** : le récit complet, daté,
  détaillé — décisions prises, bugs rencontrés (avec leur cause),
  vérifications faites, chiffres réels observés. Relire une entrée existante
  du même fichier pour le ton attendu : un paragraphe narratif, pas une puce
  télégraphique.
- **Dans `CLAUDE.md`** (section "Conventions de travail" ou la section
  d'état la plus pertinente) : *seulement si une règle durable et générale en
  ressort* — une ou deux lignes, sans le récit. Ce fichier est chargé à
  chaque session, donc chaque ligne doit rester utile dans n'importe quelle
  session future, pas seulement pour comprendre ce qui s'est passé
  aujourd'hui.

**Signal utile pour repérer une dérive** : une puce dans CLAUDE.md qui porte
une date *et* dépasse environ 400 caractères a presque toujours un récit
collé à sa règle — le récit part au journal, seule la règle reste. (Un bloc
de référence long — liste de colonnes, de tables — n'est pas forcément un
récit ; c'est la présence d'une date qui trahit le récit.)

## Étapes

1. Lire la section "Conventions de travail" du CLAUDE.md du projet courant
   pour connaître le fichier unique ou la table en vigueur.
2. Identifier le sujet de ce qui vient d'être fait (pas la date, pas le
   chantier en cours).
3. Choisir/valider le fichier.
4. Ajouter une entrée à la fin de ce fichier, au format des entrées
   existantes.
5. Si une règle durable et générale en ressort, l'ajouter en une ou deux
   lignes dans CLAUDE.md — sinon, ne rien y ajouter.
6. Committer le journal (et CLAUDE.md si modifié) avec le reste du
   changement, ou juste avant.
