## Créer un motif

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
La plupart des modèles ont un seul dessin (appelé le **motif**) qui se répète pour créer un motif. 
</div>
<div>
![Un exemple de motif utilisant différentes formes pour créer le motif.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Dessine des formes pour créer ton motif. Utilise les astuces en bas de la page si tu as besoin d’aide.

--- /task ---

--- task ---

**Test :** exécute ton code pour voir à quoi ressemble ton design.

--- /task ---

### Formes

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]


### Couleurs et effets

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Position et transformation

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

### Bogues

--- collapse ---
---
title: Les formes ne sont pas alignées comme prévu
---

Si tu souhaites que les formes soient alignées, examine de plus près tes points de coordonnées. Expérimente avec les nombres jusqu'à ce que tu aies la disposition souhaitée.

--- /collapse ---

--- collapse ---
---
title: Je ne vois pas certaines des formes de mon motif
---

L'ordre dans lequel tu dessines les choses est très important.

L'infographie est composée de calques. Dans ton motif, chaque forme est un calque. Les objets des calques supérieurs se placent devant les objets des calques inférieurs. Imagine découper toutes les formes dans du papier. Selon la façon dont tu organises et superposes ce papier, le résultat final peut être très différent.

--- /collapse ---

--- collapse ---
---
title: Mes cercles/carrés ne sont pas égaux
---

Les troisième et quatrième nombres dans `ellipse` et `rect` sont la largeur et la hauteur. Si tu les fais identiques, tu obtiendras un cercle ou un carré.

--- /collapse ---



