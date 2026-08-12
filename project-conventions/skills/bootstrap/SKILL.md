---
name: bootstrap
description: >
  Initialiser la structure de travail d'un nouveau projet (ou d'un projet
  existant qui n'a pas encore ces conventions) — un fichier de journal, un
  dossier de mockups si le projet a une interface visuelle, et un CLAUDE.md
  avec les sections de base et les conventions "journal" et "mockup-first".
  Utiliser ce skill quand Tim démarre un nouveau projet et dit des choses
  comme "on structure ce projet", "mets en place le journal et les mockups
  ici", ou "fais comme sur GameTracker mais pour ce projet-ci". Ne se
  déclenche PAS tout seul sur un projet déjà en cours sans que Tim le
  demande explicitement — ce skill écrit potentiellement dans CLAUDE.md, il
  ne doit jamais écraser un projet déjà structuré sans confirmation.
argument-hint: "[nom du projet]"
---

# Bootstrap des conventions de projet

## Avant de commencer

Vérifier l'état du dossier courant :

- **`CLAUDE.md` existe déjà avec du contenu substantiel** → ne rien écraser
  silencieusement. Montrer à Tim ce qui existe et demander où/comment
  intégrer les nouvelles sections plutôt que de remplacer le fichier.
- **`docs/journal/` ou `docs/mockups/` existent déjà** → même prudence,
  demander avant de réorganiser.
- Sinon (dossier neuf ou CLAUDE.md minimal/absent), continuer normalement.

## Étapes

1. **Poser deux questions courtes à Tim** (une seule fois, pas besoin de
   ré-interroger à chaque usage du skill sur ce projet) :
   - Le nom du projet et une phrase qui résume ce qu'il fait.
   - Le projet a-t-il une interface visuelle (frontend, dashboard, appli) ?
     La réponse détermine si le mockup-first ci-dessous s'applique.

2. **Créer `docs/journal/journal.md`** — un seul fichier de départ, pas de
   table sujet→fichier pré-remplie. Un projet neuf n'a pas encore assez
   d'historique pour savoir quels sujets reviendront ; imposer une table dès
   le jour 1 serait deviner plutôt que refléter l'usage réel. Le fichier
   commence simplement avec un titre.

3. **Si le projet a un frontend** : créer `docs/mockups/` (dossier vide,
   prêt à recevoir les premiers mockups).

4. **Écrire/compléter `CLAUDE.md`** avec ces sections (ne pas ajouter de
   sections qui n'ont de sens qu'après coup — pas de "Décisions déjà
   tranchées" ou "Notes techniques" vides, elles s'ajoutent d'elles-mêmes
   quand il y a vraiment quelque chose à y mettre) :

   ```markdown
   # <Nom du projet>

   <Une phrase résumant le projet.>

   ## Architecture

   <À compléter au fil du développement — composants principaux, stack, etc.>

   ## Conventions de travail

   - **Journal — écrire au moment de clore, pas "quand on y pense"** : dès
     qu'un chantier est livré (le commit qui termine une tâche, un bug ou une
     décision de conception), écrire l'entrée dans `docs/journal/journal.md`
     avant de committer. Le récit complet (décisions, bugs, vérifications,
     chiffres réels) va dans le journal ; seule une règle durable et générale
     qui en ressortirait — une ou deux lignes — va ici, dans CLAUDE.md. Dès
     que **deux sujets récurrents distincts** émergent dans le journal,
     scinder en plusieurs fichiers par **sujet** (jamais par date de
     travail — un chantier peut toucher un sujet déjà établi) et ajouter ici
     une table sujet → fichier pour que ce choix reste traçable.

   <!-- Si frontend : -->
   - **Mockup avant implémentation** : pour tout changement visuel notable
     (nouvelle mise en page, nouveau composant, nouvel écran, refonte d'une
     section existante — pas un correctif mineur sur l'existant), créer un
     mockup HTML autonome dans `docs/mockups/` en repartant des mockups déjà
     présents pour les conventions visuelles établies, le faire valider par
     Tim avant d'écrire du code, puis implémenter en **relisant** le fichier
     validé plutôt que de mémoire. Les mockups validés ne sont jamais
     supprimés.
   ```

5. **Confirmer à Tim** ce qui a été créé, en particulier le choix "un seul
   fichier de journal pour l'instant" — pour qu'il sache que la table
   sujet→fichier viendra plus tard, pas maintenant.
