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
  l'implémentation se fait en RELISANT le fichier, jamais de mémoire.
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

1. **Regarder les mockups existants** dans `docs/mockups/` de **ce** projet
   pour repartir des conventions déjà établies (palette, typographie,
   patterns de mise en page) plutôt que d'improviser à chaque fois. S'il n'y
   en a pas encore (premier mockup du projet), s'appuyer sur le reste du
   frontend existant (styles.css ou équivalent) pour rester cohérent avec ce
   qui est déjà en place.
2. **Créer un nouveau fichier HTML autonome** dans `docs/mockups/` (nom
   descriptif, ex. `mockup-<sujet>.html`) — pas besoin de le brancher aux
   vraies données ni au reste de l'app, il doit se suffire à lui-même
   visuellement.
3. **Soumettre pour validation** avant d'écrire une seule ligne de code
   d'implémentation frontend. Attendre une confirmation explicite, pas juste
   l'absence d'objection.
4. **Ne jamais supprimer le fichier après validation** — les mockups validés
   restent dans `docs/mockups/` comme référence durable pour de futurs
   changements dans la même zone.
5. **Implémenter en relisant le fichier mockup validé**, pas de mémoire —
   rouvrir le fichier au moment d'écrire le code, même si la validation date
   de plusieurs messages plus tôt dans la conversation.
