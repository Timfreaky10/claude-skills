---
name: bootstrap
description: >
  Initialiser la structure de travail d'un nouveau projet (ou d'un projet
  existant qui n'a pas encore ces conventions) — un dépôt git avec son
  .gitignore si le dossier n'est pas encore versionné, un fichier de journal,
  un dossier de mockups (avec ses conventions visuelles si une feuille de styles
  existe déjà) si le projet a une interface visuelle, un graphe de
  connaissances graphify tenu à jour par des hooks git, et un CLAUDE.md
  avec les sections de base et les conventions "journal", "mockup-first"
  et "graphe graphify".
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
- **Le dossier est-il déjà versionné ?** `git rev-parse --is-inside-work-tree`.
  Si oui — y compris parce qu'un dossier *parent* est un dépôt — sauter toute
  l'étape git ci-dessous et le dire, ne jamais créer un dépôt imbriqué dans un
  autre : c'est pénible à défaire et ça casse le suivi des deux côtés.
- Sinon (dossier neuf ou CLAUDE.md minimal/absent), continuer normalement.

## Étapes

1. **Poser deux questions courtes à Tim** (une seule fois, pas besoin de
   ré-interroger à chaque usage du skill sur ce projet) :
   - Le nom du projet et une phrase qui résume ce qu'il fait.
   - Le projet a-t-il une interface visuelle (frontend, dashboard, appli) ?
     La réponse détermine si le mockup-first ci-dessous s'applique.

2. **Initialiser le dépôt git** — seulement si le contrôle ci-dessus a montré
   que le dossier n'est pas déjà versionné. Sans dépôt, la convention "journal
   avant le commit" écrite plus bas dans le CLAUDE.md n'a rien à quoi
   s'accrocher.

   - `git init -b master` — branche `master`, comme les autres projets solo de
     Tim (pas de branche de travail, pas de PR sauf demande explicite).
   - **Écrire le `.gitignore` tout de suite, avant le moindre `git add`.**
     L'ordre n'est pas cosmétique : un secret entré dans l'historique n'en
     ressort pas d'un `rm`, il faut réécrire l'historique et faire tourner le
     secret. Base minimale, à compléter dès que la stack est connue :

     ```
     .env
     .venv/
     __pycache__/
     node_modules/
     logs/
     .DS_Store

     # Graphe graphify : régénéré sur chaque machine. Seul le cache
     # d'extraction des documents est versionné (étape 7).
     graphify-out/*
     !graphify-out/cache/
     graphify-out/cache/*
     !graphify-out/cache/semantic/
     ```

   - `git config --local core.autocrlf false` : le cache graphify est indexé
     par un hachage des octets bruts de chaque fichier, un clone sorti en CRLF
     sur une autre machine changerait toutes les clés.

   Ne **pas** committer à ce stade — le premier commit vient à l'étape 6, une
   fois les fichiers de structure écrits, pour qu'il ait un contenu réel.

3. **Créer `docs/journal/journal.md`** — un seul fichier de départ, pas de
   table sujet→fichier pré-remplie. Un projet neuf n'a pas encore assez
   d'historique pour savoir quels sujets reviendront ; imposer une table dès
   le jour 1 serait deviner plutôt que refléter l'usage réel. Le fichier
   commence simplement avec un titre.

4. **Si le projet a un frontend** : créer `docs/mockups/`, puis regarder s'il
   y a déjà une feuille de styles (`styles.css`, un fichier de thème, des
   tokens — bootstrap tourne aussi sur des projets en cours).

   - **Une feuille de styles existe** → créer `docs/mockups/README.md` en
     **relevant les valeurs dans le code** (polices et leurs graisses,
     variables CSS avec leurs vraies valeurs et l'usage de chacune, fond de
     page) — jamais de mémoire ni d'après ce qu'on croit être la charte. Y
     écrire aussi que **le CSS fait foi** en cas de divergence, sinon le
     fichier devient un doublon qui dérive en silence.
   - **Aucune feuille de styles** (projet vraiment neuf) → laisser le dossier
     vide. **Ne pas créer de README à trous** : un fichier de conventions
     vide donnerait l'illusion que les conventions sont écrites, et
     `mockup-first` irait le lire pour n'y trouver que des rubriques vides.
     C'est ce skill-là qui le créera au premier mockup validé, quand la
     palette existera vraiment.

5. **Écrire/compléter `CLAUDE.md`** avec ces sections (ne pas ajouter de
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

   <!-- Si docs/mockups/README.md a été créé à l'étape 4 : -->
   - **Vocabulaire visuel** : polices, variables CSS et fond de page sont
     dans `docs/mockups/README.md`, à ouvrir avant de construire un mockup.
     Le CSS fait foi si les deux divergent.

   <!-- Si le graphe a été construit à l'étape 7 : -->
   - **Graphe graphify — l'interroger avant de fouiller** : toute question
     sur le code ou la doc (où vit X, qui appelle Y, quelle décision touche
     Z) passe d'abord par le MCP `graphify` — `query_graph` (régler
     `token_budget`), puis `get_node` / `get_neighbors` / `shortest_path` —
     et seulement ensuite par `grep` et la lecture des fichiers qu'il
     désigne. Le code se remet à jour seul (hooks git, sans modèle) ; les
     documents gardent leur dernière extraction : `/graphify . --update` sur
     demande de Tim, puis committer `graphify-out/cache/semantic/`.
     `graph_stats` dit si le graphe suit `HEAD`.
   ```

6. **Premier commit** (si le dépôt vient d'être créé à l'étape 2) — une fois
   le `.gitignore` et les fichiers de structure en place. Vérifier ce qui part
   avec `git status` avant de committer : si un fichier qui n'aurait pas dû
   être suivi apparaît, compléter le `.gitignore` plutôt que de committer et
   corriger après.

7. **Graphe graphify** — après le premier commit : les hooks s'accrochent au
   dépôt, et le graphe retient le commit sur lequel il a été construit. Sur
   un projet déjà versionné (étape git sautée), le faire quand même.

   - **Vérifier l'outillage d'abord** : `graphify --version` (paquet
     `graphifyy`), et le MCP — des outils `mcp__graphify__*` disponibles
     dans la session (la CLI `claude` n'est pas toujours sur le PATH du
     shell, `claude mcp list` ne suffit pas à conclure). S'il
     manque quelque chose, donner les commandes à Tim — `pip install
     graphifyy`, `graphify install`, `claude mcp add --scope user graphify
     -- graphify-mcp` — sans rien installer sans son oui, et sauter cette
     étape sans bloquer les autres. Le serveur se déclare **une fois, au
     niveau utilisateur** : il lit `graphify-out/graph.json` du dossier où
     la session démarre, rien à configurer par projet.
   - **Exclure avant de construire** : un fichier généré, volumineux et sans
     rien à apprendre (export, page de relecture, données brutes) va dans un
     `.graphifyignore` — il coûterait à chaque extraction.
   - **Construire** : `/graphify .` (skill `graphify`). Le code passe par
     l'AST, sans modèle ; les documents passent par le modèle. Sur un projet
     neuf, c'est négligeable. Sur un projet en cours riche en documents,
     **annoncer l'ordre de grandeur avant** (repère GameTracker : ~2 M de
     tokens pour ~190 documents) et laisser Tim choisir entre tout et
     `graphify update .` (code seul, gratuit).
   - **`graphify hook install`** : `post-commit`, `post-checkout`,
     `post-merge` et `post-rewrite` refont la partie code après chaque
     commit, changement de branche ou pull.
   - **Committer `graphify-out/cache/semantic/`** (le `.gitignore` de
     l'étape 2 laisse passer ce seul dossier) : l'autre machine reconstruit
     le graphe par `/graphify .` sans repayer l'extraction des documents.
     Conditions : les mêmes octets des deux côtés (`core.autocrlf false`) et
     la même version de graphify, sinon le dossier de cache change de nom.
   - **Vérifier** par le MCP : `graph_stats` doit renvoyer des nœuds et
     « matches HEAD ». Si la session a démarré avant que le graphe existe,
     passer `project_path` (chemin absolu du projet).

8. **Proposer le dépôt distant — ne rien créer sans un oui explicite.** Le
   dépôt local de l'étape 2 est déjà pleinement utilisable ; publier est un
   geste séparé, qui expose quelque chose sous le compte de Tim. Donc :
   demander, et s'arrêter là s'il ne répond pas ou décline.

   - Proposer un **slug** dérivé du nom du *dossier*, pas de la phrase donnée
     à l'étape 1 ("Suivi de mes finances" n'est pas un nom de dépôt), et le
     faire valider.
   - **Privé par défaut.** Ne basculer en public que si Tim le demande
     explicitement, jamais comme suggestion.
   - S'il accepte : `gh repo create <slug> --private --source=. --push`.

9. **Confirmer à Tim** ce qui a été créé, en particulier le choix "un seul
   fichier de journal pour l'instant" — pour qu'il sache que la table
   sujet→fichier viendra plus tard, pas maintenant. Dire aussi si un dépôt a
   été initialisé, et s'il est resté local ou non, et si le graphe est
   construit (code seul ou documents compris) ou ce qui manquait pour le
   faire.
