---
name: learning-session
description: Workflow complet de suivi des sessions d'apprentissage de Tim (DaVinci Resolve, Unity, Claude Cowork+Code, Vibe Coding, Unreal Engine). Utilise ce skill dès que Tim dit "je lance la session", "j'ai fait les leçons X-Y", "je termine pour aujourd'hui", ou demande à mettre à jour son log/curriculum/TickTick. Gère la création du log Obsidian, la mise à jour du curriculum, et la synchronisation TickTick (tâche récurrente + tâches par section).
---

# Learning Session — procédure

Ce skill porte la **procédure**. Il ne connaît aucun cours, aucun chemin, aucun ID : tout cela vit
dans le vault et se lit au moment voulu.

| Fichier | Contenu | Quand le lire |
|---|---|---|
| `02_Learning/_registre.md` | un bloc par cours : chemins, emoji, tags, wikilink, projet TickTick + IDs, statut | **toujours, en premier** |
| `02_Learning/_templates/log.md` | gabarit du log + numérotation + remplissage | création ou mise à jour d'un log |
| `02_Learning/_templates/curriculum.md` | procédure de mise à jour du curriculum et calcul de progression | fin de session |

## Étape 0 — résoudre les chemins

Il faut `02_Learning`. Où le trouver dépend de l'environnement — **déterminer lequel avant tout accès** :

- **Cowork** — les dossiers sont montés sous `$HOME/mnt/<nom>` et **le chemin change à chaque
  session** : lister `$HOME/mnt/`, ne jamais coder un chemin de session en dur.
- **Claude Code** — rien n'est monté (`$HOME/mnt/` n'existe pas) : lire le dossier directement à son
  emplacement Proton Drive, voir « Emplacements » ci-dessous.

**S'il est introuvable, le dire à Tim et s'arrêter.** Sans le registre, ce skill n'a aucune donnée :
ne pas reconstituer un chemin ni un ID de mémoire, même s'ils semblent connus.

## Le registre fait foi

Lire `_registre.md` et en tirer le bloc du cours concerné. Trois règles :

- **Un champ `—` est un trou connu.** Ne rien inventer à la place : soit on le comble (voir plus bas),
  soit on demande à Tim.
- **Le nom du projet TickTick est la vérité, l'ID n'est qu'un cache.** Si un appel échoue sur un ID,
  re-résoudre le projet par son nom (`list_projects`), agir, puis **réécrire l'ID dans le registre**.
- **Cours inconnu du registre** : demander à Tim plutôt que de deviner une arborescence. S'il s'agit
  d'un nouveau cours, créer son bloc avec ce qu'on sait et laisser `—` sur le reste.

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

## Étape 1 — début de session

*Déclencheur : « je lance la session [cours] », « je commence [cours] ».*

Déterminer le numéro de session et créer le log selon `_templates/log.md`, dans le dossier `Logs/` du
cours indiqué au registre.

## Étape 2 — fin de session (totale ou partielle)

*Déclencheur : « j'ai fait LX-LY », « j'ai fini la section X », « je m'arrête là ».*

Trois mises à jour, dans cet ordre :

1. **Le log** — cocher, marquer la reprise, mettre `📌 À faire` à jour (voir le gabarit)
2. **Le curriculum** — voir `_templates/curriculum.md`
3. **TickTick** — ci-dessous

### TickTick

**Tâche récurrente** (si le registre en donne une) : mettre son `content` à jour — sections terminées
en `✅`, prochaine session en `🗓 date → LX–LY — Description`, lien Udemy toujours en tête.

**Tâches par section** (si le projet en a) : récupérer les tâches avec `get_project_with_undone_tasks`
**juste avant d'écrire** — les etags changent à chaque modification et un etag périmé fait échouer le
batch. Puis `batch_update_tasks` : section terminée → tous les items `status: 1` + `columnId` vers la
colonne Fait ; section en cours → items faits `status: 1`, `← reprise` sur le prochain item non fait.

**Si la colonne Fait manque au registre** (`—`), ne pas déplacer les tâches : les cocher suffit.
Proposer à Tim de créer la colonne, et si elle est créée, **inscrire son ID au registre**.

## Étape 3 — recueillir les réflexions

Quand Tim raconte sa session, remplir `🧠 Ce que j'ai appris` et `⚡ Ce qui m'a surpris ou bloqué`.
Ce sont ses mots : ne pas les produire à sa place, demander s'il n'a rien dit.

## Fin de cours

Cours à 100 % → archiver le sous-projet TickTick (`update_project`, `closed: true`). Le groupe parent
reste intact. Puis mettre le registre à jour : statut du cours, statut du projet, et déplacer le bloc
dans la section « Cours terminés et archivés ».

## Tenir le registre vivant

Le registre est la seule mémoire de ce workflow — s'il dérive, tout dérive. À chaque fois qu'une de ces
choses change, l'y inscrire **dans la même session**, et mettre `updated:` à jour :

- un ID re-résolu, une colonne ou une tâche récurrente créée
- un curriculum qui n'existait pas et qui vient d'être écrit
- un cours terminé, archivé, ou nouvellement commencé

Ne jamais laisser cette information uniquement dans la conversation : la session suivante ne la verra
pas.
