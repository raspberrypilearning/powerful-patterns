## Développer et tester : motif

Now that you have a **motif**, you can repeat it to make a pattern

![Exemples de projets finis dont le motif est utilisé à plusieurs reprises pour former un motif complet.](images/second.gif)


--- task ---

Move, resize and repeat the motif you have created to make a repeating pattern. Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

**Test :** montre ton projet à quelqu'un d'autre pour avoir son avis.

--- /task ---




### Moving, rotating and resizing

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

### Repeating

[[[generic-python-for-loop-repeat]]]

### Randomness

--- collapse ---
---
title: Positions aléatoires
---

Tu peux ajouter `from random import randint` en haut de **main.py**, cela te permet d'utiliser la fonction `randint` pour générer des nombres aléatoires.

Pour utiliser la fonction `randint`, tu dois l'appeler dans ton code.

Une façon d'utiliser l'aléatoire est de déplacer ton motif à une position aléatoire à chaque fois qu'il est dessiné :

--- code ---
---
language: python filename: main.py - draw()

---

    push_matrix()  # Start transformation
    translate(randint(0, 400), randint(0, 400))
    draw_motif()
    pop_matrix()  # Reset transformation

--- /code ---

Tu peux également utiliser l'aléatoire pour modifier les couleurs de ton motif au fur et à mesure qu'il est redessiné.

--- code ---
---
language: python filename: main.py - draw()

---

    BLUE = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

### Bugs

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

