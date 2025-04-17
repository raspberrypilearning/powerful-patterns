## Maak een motief

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
De meeste patronen hebben één ontwerp (het **motief**) dat zich herhaalt om een patroon te creëren. 
</div>
<div>
![Een voorbeeld van een motief waarbij verschillende vormen worden gebruikt om het motief te maken.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Teken vormen om je eigen motief te maken. Als je hulp nodig hebt, kun je de tips onderaan de pagina gebruiken.

--- /task ---

--- task ---

**Test:** Voer je code uit om te zien hoe je ontwerp eruitziet.

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

### Fouten

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
title: Mijn cirkels/vierkanten zijn niet gelijk
---

Het derde en vierde cijfer in `ellipse` en `rect` zijn de breedte en de hoogte. Als je ze hetzelfde maakt, krijg je een cirkel of vierkant.

--- /collapse ---



