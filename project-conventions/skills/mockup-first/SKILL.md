---
name: mockup-first
description: >
  Valider un mockup HTML avant d'écrire le moindre code d'implémentation,
  pour tout changement visuel notable sur le frontend d'un projet — nouvelle
  mise en page, nouveau composant, nouvel écran, refonte d'une section
  existante. Utiliser ce skill dès qu'une demande implique de "concevoir",
  "redessiner", ou "ajouter un écran/panneau/vue pour" quelque chose sur un
  projet qui a un dossier docs/mockups/ (créé par le skill bootstrap de ce
  même plugin), même si l'utilisateur ne dit pas explicitement "mockup" —
  pas nécessaire pour un correctif visuel mineur (couleur, espacement,
  alignement d'un élément déjà existant). Une fois le mockup validé,
  l'implémentation se fait en RELISANT le fichier, jamais de mémoire, puis se
  vérifie dans un vrai navigateur avant d'annoncer que c'est fait.
---

# Mockup avant implémentation

## Pourquoi

Un mockup HTML statique est bon marché à produire et à corriger ; du code
frontend déjà branché sur le reste de l'app (état, données, interactions)
est cher à reprendre après coup. Sur un projet cousin (GameTracker), sauter
cette étape une fois — implémenter "de mémoire" sans repasser par un mockup
validé puis relu — a coûté quatre passes de correction sur une seule
fonctionnalité.

## Quand

Avant tout changement visuel **notable** : nouvelle mise en page, nouveau
composant, nouvel écran ou nouvelle vue, refonte d'une section existante. Pas
nécessaire pour un correctif ciblé (une couleur, un espacement, un
alignement cassé) sur quelque chose qui existe déjà.

## Étapes

1. **Regarder ce qui a déjà été tranché** — avant de concevoir quoi que ce
   soit, chercher si l'idée a déjà été essayée puis refusée : section
   "Décisions déjà tranchées" du CLAUDE.md du projet si elle existe, sinon le
   journal. Re-proposer une approche déjà rejetée coûte du temps à Tim et
   donne l'impression de ne pas avoir écouté.
2. **Regarder les mockups existants** dans `docs/mockups/` de **ce** projet
   pour repartir des conventions déjà établies (palette, typographie,
   patterns de mise en page) plutôt que d'improviser à chaque fois. S'il n'y
   en a pas encore (premier mockup du projet), s'appuyer sur le reste du
   frontend existant (styles.css ou équivalent) pour rester cohérent avec ce
   qui est déjà en place.
   Si le projet **consigne ses conventions visuelles par écrit** (polices,
   variables CSS, principes de thème — son CLAUDE.md indique en général où),
   lire ce fichier d'abord : c'est plus fiable que de les déduire des mockups
   existants, et ça évite d'inventer une variante de la palette à chaque
   nouveau mockup.
3. **Créer un nouveau fichier HTML autonome** dans `docs/mockups/` (nom
   descriptif, ex. `mockup-<sujet>.html`) — pas besoin de le brancher aux
   vraies données ni au reste de l'app, il doit se suffire à lui-même
   visuellement.
   En revanche, y mettre des **valeurs réalistes** plutôt que du Lorem ipsum
   ou des nombres ronds inventés : reprendre de vrais libellés et de vraies
   longueurs de texte du projet fait apparaître tout de suite les problèmes
   de mise en page qu'un contenu factice masque.
4. **Soumettre pour validation** avant d'écrire une seule ligne de code
   d'implémentation frontend. Attendre une confirmation explicite, pas juste
   l'absence d'objection.

   **Au premier mockup validé du projet**, si les conventions visuelles ne
   sont écrites nulle part (pas de `docs/mockups/README.md` ni d'équivalent
   désigné par le CLAUDE.md), les consigner maintenant : c'est le moment où
   la palette et la typographie viennent d'être choisies **et approuvées**,
   donc le premier moment où il y a quelque chose de vrai à écrire. Relever
   les valeurs depuis le mockup validé lui-même — polices et graisses,
   couleurs et leur rôle, fond de page — et ajouter dans le CLAUDE.md la
   ligne qui désigne le fichier. Les mockups suivants repartiront de là au
   lieu de redécider à chaque fois.

5. **Ne jamais supprimer le fichier après validation** — les mockups validés
   restent dans `docs/mockups/` comme référence durable pour de futurs
   changements dans la même zone.
6. **Implémenter en relisant le fichier mockup validé**, pas de mémoire —
   rouvrir le fichier au moment d'écrire le code, même si la validation date
   de plusieurs messages plus tôt dans la conversation.

   Si plusieurs écarts au mockup sont trouvés après coup, relire le fichier
   **en entier** plutôt que corriger écart par écart — ils arrivent rarement
   seuls.
7. **Vérifier dans un vrai navigateur, puis rapporter avec la preuve.**
   Implémenter n'est pas terminer. Charger la page, zéro erreur console,
   contrôler les valeurs qui comptent avec `getComputedStyle` plutôt qu'à
   l'œil, tester les états (survol, actif, vide) et le responsive si la mise
   en page change. Finir par une capture d'écran, en disant ce qui a été
   vérifié **et ce qui ne l'a pas été**.

   Piège classique avant de suspecter le code : un serveur statique simple
   n'envoie aucun en-tête de cache, donc CSS et JS peuvent être servis
   périmés. Si un changement "ne s'affiche pas", vérifier ça d'abord.
