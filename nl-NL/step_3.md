## Bouwen en testen: het Motief

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Nu is het tijd om je motief te maken, het eerste element van je patroon.
</div>
<div>
![Een voorbeeld van een motief waarbij verschillende vormen worden gebruikt om het motief te maken.](images/motif.png){:width="300px"}
</div>
</div>

Het proces van het maken van je motief weerspiegelt wat computerwetenschappers vaak doen als ze een programma of oplossing voor een probleem maken. Dit proces wordt **decompositie** genoemd en je zult decompositie gebruiken om je motief te maken.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">Decompositie</span> is iets opsplitsen in kleinere en gemakkelijker te begrijpen delen. Dit betekent dat je een patroon deel per deel kunt bouwen totdat het compleet is.</p>

Kijk naar het patroon dat je wilt namaken. Hoe kun je het opsplitsen in één enkel element (het motief) dat zich herhaalt?

In dit voorbeeld werd een art deco-behangpapier patroon ontleed tot de basis verzameling van vormen (vijf cirkels over elkaar gelegd) die het motief vormen:

![Een enkel motief van vijf cirkels naast een afbeelding van het volledige art deco patroon met veel kopieën van het motief.](images/motif-pattern.png)

**Tip:** Denk eraan om je project elke keer dat je iets toevoegt, te testen. Het is veel gemakkelijker om fouten te vinden en op te lossen voordat je meer wijzigingen aanbrengt.

--- task ---

Je hebt een aantal echt nuttige vaardigheden opgebouwd. Hier is een geheugensteuntje om je te helpen bij het maken van jouw motief:

### Vormen

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

### Kleuren en effecten

[[[generic-theory-simple-colours]]]

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Positie en transformatie

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- task ---

**Test:** Laat iemand anders jouw project zien en vraag feedback. Wil je iets aan je motief veranderen?

--- /task ---

--- task ---

**Debug:** Mogelijk vindt je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

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

Mogelijk vind je een bug die hier niet wordt vermeld. Kun je erachter komen hoe je het kunt oplossen?

We horen graag over je fouten en hoe je ze hebt opgelost. Gebruik de feedback knop onderaan deze pagina als je een andere bug in je project hebt gevonden.

--- /task ---

--- save ---
