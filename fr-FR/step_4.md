## Faire le motif

Maintenant que tu as un **motif**, tu peux le répéter pour créer un motif

![Exemples de projets finis dont le motif est utilisé à plusieurs reprises pour former un motif complet.](images/second.gif)


--- task ---

Déplace, redimensionne et répète le motif que tu as créé pour créer un motif qui se répète. Utilise les astuces en bas de la page si tu as besoin d’aide.

--- /task ---


--- task ---

**Test :** exécute le code pour voir à quoi ressemble ton modèle.

--- /task ---




### Déplacer, faire une rotation et redimensionner

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
title: Modification de la taille de ton motif
---

Si tu utilises un motif que tu as déjà dessiné, il se peut qu'il ne soit pas de la bonne taille.

Tu peux utiliser `scale()` avant d'appeler la fonction qui dessine ton motif pour changer sa taille. L'utilisation d'une entrée supérieure à "1" agrandira le motif, l'utilisation d'une entrée inférieure à "1" le rendra plus petit.

--- code ---
---
language: python
filename: main.py - draw()
---

    scale(0.5) #Moitié de la taille

--- /code ---

--- /collapse ---

### Répéter

[[[generic-python-for-loop-repeat]]]

### Aléatoire

--- collapse ---
---
title: Positions aléatoires
---

Tu peux ajouter `from random import randint` en haut de **main.py**, cela te permet d'utiliser la fonction `randint` pour générer des nombres aléatoires.

Pour utiliser la fonction `randint`, tu dois l'appeler dans ton code.

Une façon d'utiliser l'aléatoire est de déplacer ton motif à une position aléatoire à chaque fois qu'il est dessiné :

--- code ---
---
language: python
filename: main.py - draw()

---

    push_matrix()  # Commencer la transformation
    translate(randint(0, 400), randint(0, 400))
    dessin_motif()
    pop_matrix()  # Réinitialiser la transformation

--- /code ---

Tu peux également utiliser l'aléatoire pour modifier les couleurs de ton motif au fur et à mesure qu'il est redessiné.

--- code ---
---
language: python
filename: main.py - draw()

---

    BLEU = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

### Bogues

--- collapse ---
---
title: Mon motif ne semble pas tourner
---

Assure-toi d'utiliser la fonction `radian()` pour convertir les degrés en radians.

--- /collapse ---

--- collapse ---
---
title: La rotation semble étrange
---

As-tu vérifié que tu utilises `translate()` depuis et vers les bonnes coordonnées ?

As-tu plus d'une chose en rotation ? Tu devras peut-être utiliser `push_matrix()` et `pop_matrix()` pour que l'écran tourne à différents points à la fois.

--- /collapse ---

--- collapse ---
---
title: Mon motif ne ressemble pas à ce que je veux qu'il soit
---

Passe en revue les sections ci-dessus sur `rotate()` et `translate()`. Expérimente jusqu'à ce que tu aies ce que tu veux, et rappelle-toi que les erreurs sont puissantes !

--- /collapse ---

--- collapse ---
---
title: J'obtiens une erreur
---

Vérifie la syntaxe de ton code. Te manque-t-il des parenthèses `(` ou `)` ou un deux-points `:` après avoir défini une fonction ? Est-ce que quelque chose est mal orthographié ? Ton code est-il correctement indenté ?

--- /collapse ---

