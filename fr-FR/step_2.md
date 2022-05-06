## Ton idée

Utilise cette étape pour planifier ton motif puissant. Tu peux planifier simplement en pensant, en bricolant, en dessinant ou en écrivant, ou comme bon te semble !

![Un gif animé de trois exemples différents utilisant différentes formes pour créer les motifs et les animations pour développer le motif.](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Les motifs ont souvent une <span style="color: #0faeb0">signification culturelle ou religieuse</span>. Certaines formes et positions géométriques peuvent avoir des significations symboliques ou sacrées. Que le motif soit dans l'architecture, le tissu, l'art, la cuisine ou autre chose, le processus de fabrication du motif peut également être important.</p>

### Pourquoi fais-tu ton modèle puissant ?

--- task ---

Réfléchis à l'objectif du motif que tu crées.

Ça pourrait être :
- Pour exprimer quelque chose d'important de ta culture ou de celle de ta famille
- Pour recréer un motif géométrique qui signifie quelque chose pour toi
- Quelque chose que tu crées avec un groupe de personnes pour envoyer un certain message (par exemple, un quilt)
- Pour montrer quelque chose de fascinant à propos d'un passe-temps (par exemple, l'art, la science, la nature, la musique)

**Astuce :** Les motifs sont partout ! Tu peux choisir de t'inspirer en partant à la recherche de modèles dans ton environnement physique ou en ligne.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">En plus d'avoir une signification symbolique, les motifs illustrent les mathématiques qui nous entourent. Les mathématiques nous aident à donner un sens au monde qui nous entoure et nous pouvons trouver des modèles mathématiques dans l'art, la littérature et la nature. </p>

### C'est pour qui ?

--- task ---

Pense pour qui tu feras ton modèle (ton **public**).

Quelle est la signification de ton motif ? Les couleurs, les formes ou la façon dont le motif est répété signifieront-elles quelque chose de spécial pour toi ou ton public ?

Partager ton motif est un excellent moyen d'exprimer quelque chose sur toi-même ou sur ta culture.

Si tu crées un motif en groupe, ton motif doit-il avoir une certaine taille ou forme pour s'adapter aux autres parties d'un motif plus grand ?

--- /task ---

### Commencer

--- task ---

Ouvre le projet de démarrage [Motifs puissants](https://trinket.io/python/6c4a0c6406){:target=blank } et clique sur le bouton remix.

--- /task ---

### Configurer ton projet

--- task ---

Ajoute du code à `configuration()` pour préparer ton projet.

--- collapse ---

---
title: Définir la taille de l'écran au démarrage de ton programme
---

**Choisir :** Ajoute une taille adaptée au motif que tu souhaites créer. Tu pourras toujours le modifier ultérieurement au fur et à mesure de l'évolution de ton projet.

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup(): size(400, 400) #Choose a size

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Définir la couleur d'arrière-plan au démarrage de ton programme
---

Pense à l'endroit où tu veux dessiner ton arrière-plan. Tu peux :
+ Ajouter du code à `configuration()` pour que l'arrière-plan soit dessiné une fois lorsque tu exécutes ton projet
+ Ajouter du code à `dessin()` pour que l'arrière-plan soit redessiné à chaque exécution de la fonction `dessin()`

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
line_highlights: 9
---

    background(255, 255, 255) #Try different numbers to change the colour

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Débogage :** Il est possible que tu trouves des bogues dans ton projet que tu dois corriger. Voici quelques bogues assez courants.

--- collapse ---

---
title: J'ai modifié ma taille et ma couleur, mais la zone de sortie reste la même
---

Après avoir modifié le code, tu devras `exécuter` ton projet pour voir les changements dans la zone de sortie.

--- /collapse ---

--- collapse ---

---
title: J'ai essayé différents numéros, mais la couleur d'arrière-plan ne change pas
---

La quantité maximale de rouge, de vert ou de bleu est de `255`. Assure-toi que toutes tes valeurs de couleur `d'arrière-plan` sont comprises entre `0` et `255`.

--- /collapse ---

--- /task ---


--- save ---
