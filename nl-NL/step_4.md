## Uitbreiden en testen - Patroon

Nu is het tijd om je volledige patroon te maken!

![Voorbeelden van voltooide projecten waarbij het motief herhaaldelijk is gebruikt om een volledig patroon te vormen.](images/second.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceBLAUW; padding: 10px;"><span style="color: #0faeb0">Abstractie</span> is het oplossen van problemen door geen rekening te houden met onnodige details. 

</p>

--- task ---

Kijk naar deze Maleisische laagjescake (kek lapis Sarawak). Hoe verandert het motief om het gehele patroon te maken?

![Het motief uit het kek lapis Sarawak project naast het volledige patroon.](images/kek-motif.png)

Kijk eens naar dit art deco behang. Hoe verandert het motief om het gehele patroon te maken?

![Het motief uit het art deco behangpapier project naast het volledige patroon.](images/spirals-motif.png)

Denk na over het patroon dat je aan het maken bent. Hoe verandert het motief om het gehele patroon te maken. Gebruik deze vragen om je te helpen bij de abstractie:
- Roteert het gehele of een deel van het motief?
- In welke richting draait het? En met hoeveel?
- Zijn er lagen in het patroon die elkaar overlappen?
- Hoe vaak herhaalt het motief zich?
- Hoe is de herhaling georganiseerd (dwz hoeveel rijen/kolommen)?
- Veranderen de kleuren?
- Zijn er details die niet in het motief zijn verwerkt (bijv. de kers op de Maleisische laagcake)?

--- /task ---

--- task ---

Nu je meer weet over hoe het motief het hele patroon gaat vormen, kun je het programmeren met je antwoorden op de bovenstaande vragen.

**Tip:** Vergeet niet dat je de voorbeelden in de inleiding "van binnen" kan bekijken en de code kan 'kopiëren" en "plakken" in jouw project. Professionele ontwikkelaars doen dit altijd zo!

Je hebt een aantal echt nuttige vaardigheden opgebouwd. Hier is een geheugensteuntje om je te helpen bij het maken van je herhaalde patroon:

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]


--- collapse ---

---
title: Willekeurige posities
---

Je kan `from random import randint` toevoegen bovenaan **main.py**, dit laat je te om de `randint` functie te gebruiken om willekeurige getallen te genereren.

Om de `randint` functie te gebruiken, moet je deze in je code aanroepen.

Een manier om random te gebruiken is door je motief naar een willekeurige positie te verplaatsen iedere keer dat het getekend wordt:

--- code ---
---
language: python 
filename: main.py - draw()
---

push_matrix() #Transformatie starten 
translate(randint(0, 400), randint(0, 400)) 
teken_motief() 
pop_matrix() #Transformatie resetten

--- /code ---

Je kan random ook gebruiken om de kleuren in je motief te veranderen wanneer het opnieuw getekend wordt.

--- code ---
---
language: python 
filename: main.py - draw()
---

BLAUW = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

--- collapse ---

---
title: De grootte van je motief wijzigen
---

Als je een motief gebruikt dat je al hebt getekend, is het misschien niet de juiste grootte.

Je kunt `scale()` gebruiken voordat je de functie oproept die je motief tekent om de grootte te wijzigen. Als je input groter is dan '1', wordt het motief groter, als je input kleiner is dan '1', wordt het kleiner.

--- code ---
---
language: python 
filename: main.py - draw()
---

scale(0.5) #Halve grootte

--- /code ---

--- /collapse ---

--- /task ---

Nu kan je jouw patroon animeren om te laten zien hoe je het hebt gemaakt. Vaak hebben patronen een krachtige culturele betekenis in de manier waarop ze worden gemaakt of in het proces.

--- task ---

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---


--- task ---

**Test:** Laat iemand anders je project zien en vraag feedback. Wil je iets aan je motief veranderen?

--- /task ---

--- task ---

**Debug:** Mogelijk vind je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

--- collapse ---

---
title: Mijn motief lijkt niet te roteren
---

Zorg ervoor dat je de `radian()` functie gebruikt om graden naar radialen te converteren.

--- /collapse ---

--- collapse ---
---
title: De rotatie ziet er vreemd uit
---

Heb je gecontroleerd of je `translate()` van en naar de juiste coördinaten gebruikt?

Is er meer dan 1 ding dat draait? Mogelijk moet je `push_matrix()` en `pop_matrix()` gebruiken, zodat het scherm op verschillende punten tegelijk draait.

--- /collapse ---

--- collapse ---
---
title: Mijn patroon animeert niet
---

Controleer of je `frame_count()` correct in een lus hebt gebruikt.

--- /collapse ---

--- collapse ---
---
title: Mijn patroon ziet er niet uit zoals ik het wil
---

Herbekijk de secties hierboven over `rotate()` en `translate()`. Experimenteer totdat het er uitziet zoals je het wilt, en onthoud dat fouten waardevol zijn!

--- /collapse ---

--- collapse ---
---
title: Ik krijg een foutmelding
---

Controleer de syntax van je code. Missen er haakjes `(` of `)` of een dubbele punt `:` na het definiëren van een functie? Is er iets verkeerd gespeld? Is je code correct ingesprongen?

--- /collapse ---

--- collapse ---
---
title: De animatie is te snel/te langzaam
---

Verander de `frame_rate()` aan het begin van je programma om de gewenste snelheid te krijgen.

--- /collapse ---

Mogelijk vind je een bug die hier niet wordt vermeld. Kun je erachter komen hoe je het kunt oplossen?

We horen graag over je fouten en hoe je ze hebt opgelost. Gebruik de feedback knop onderaan deze pagina als je een andere bug in je project hebt gevonden.

--- /task ---


--- save ---
