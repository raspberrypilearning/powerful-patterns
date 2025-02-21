## Bouwen en testen - Patroon

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Most patterns have one design (called the **motif**) that repeats to create a pattern. 
</div>
<div>
![Een voorbeeld van een motief waarbij verschillende vormen worden gebruikt om het motief te maken.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Draw shapes to create your motif. Use the tips at the bottom of the page if you need help.

--- /task ---

--- task ---

**Test:** Laat iemand anders jouw project zien en vraag feedback.

--- /task ---

### Vormen

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]


### Kleuren en effecten

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Positie en transformatie

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

### Bugs

--- collapse ---
---
title: Vormen zijn niet uitgelijnd zoals ik had verwacht
---

Als je wilt dat de vormen worden uitgelijnd, kijk dan eens goed naar je coördinaatpunten. Experimenteer met de getallen totdat je de gewenste lay-out hebt.

--- /collapse ---

--- collapse ---
---
title: Ik kan sommige vormen in mijn motief niet zien
---

De volgorde waarin je dingen tekent is erg belangrijk.

Computerafbeeldingen bestaan uit lagen. In je motief is elke vorm een laag. Objecten op hogere lagen zitten voor objecten op lagere lagen. Stel je voor dat je alle vormen uit papier knipt. Afhankelijk van hoe je dat papier rangschikt en overlapt, kan het eindresultaat er heel anders uitzien.

--- /collapse ---

--- collapse ---
---
titel: Mijn cirkels/vierkanten zijn niet gelijk
---

Het derde en vierde cijfer in `ellips` en `rect` zijn de breedte en hoogte. Als je ze hetzelfde maakt, krijg je een cirkel of vierkant.

--- /collapse ---



