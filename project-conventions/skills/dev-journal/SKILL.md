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
  déjà établie), y écrit le récit détaillé, range une règle propre à une
  fonctionnalité ou une référence technique dans le fichier de référence que
  le projet désigne, et ne laisse dans CLAUDE.md que la règle durable utile à
  n'importe quelle session — puis mesure ce qu'il vient d'y écrire.
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

Chaque texte a **une seule** destination, choisie au moment d'écrire — jamais
écrire d'abord dans CLAUDE.md pour ranger plus tard :

- **Le récit → le fichier de journal choisi ci-dessus** : complet, daté,
  détaillé — décisions prises, bugs rencontrés (avec leur cause),
  vérifications faites, chiffres réels observés. Relire une entrée existante
  du même fichier pour le ton attendu : un paragraphe narratif, pas une puce
  télégraphique.
- **Une règle propre à une fonctionnalité, ou une référence technique →
  le fichier de référence que le projet désigne**, s'il en désigne (son
  CLAUDE.md, section "Conventions de travail", dit lesquels et pour quoi :
  par exemple un fichier de décisions par écran, un fichier de schéma de
  base). Respecter sa structure (index, section par fonctionnalité/table).
  Si le projet n'en désigne aucun, ce cas n'existe pas : la règle va au
  journal, ou dans CLAUDE.md si elle sert partout.
- **Une règle utile à n'importe quelle session → `CLAUDE.md`** : une ou deux
  lignes, sans le récit, dans la section la plus pertinente. Ce fichier est
  chargé à chaque session ; une règle qui ne sert que quand on touche à un
  écran ou une table précise n'y a pas sa place.

## Mesurer ce qu'on vient d'écrire dans CLAUDE.md

Après l'écriture, relire **ses propres** ajouts à CLAUDE.md. Une puce qui
porte une date *et* dépasse environ 400 caractères a presque toujours un
récit collé à sa règle : le récit part au journal, seule la règle reste. (Un
bloc de référence long — liste de colonnes, de tables — n'est pas forcément
un récit ; c'est la date qui trahit le récit.)

Ne ranger que ce qu'on vient d'écrire soi-même. Déplacer une règle plus
ancienne du CLAUDE.md se propose à Tim, ça ne se fait pas d'office.

## Étapes

1. Lire la section "Conventions de travail" du CLAUDE.md du projet courant :
   fichier de journal unique ou table sujet → fichier, et fichiers de
   référence éventuels.
2. Identifier le sujet de ce qui vient d'être fait (pas la date, pas le
   chantier en cours).
3. Choisir/valider le fichier de journal.
4. Ajouter une entrée à la fin de ce fichier, au format des entrées
   existantes.
5. Si une règle en ressort, la ranger selon « Ce qui va où » — sinon, rien
   d'autre à écrire.
6. Si CLAUDE.md a été modifié, appliquer « Mesurer ce qu'on vient d'écrire ».
7. Committer le journal (et les fichiers modifiés) avec le reste du
   changement, ou juste avant.
