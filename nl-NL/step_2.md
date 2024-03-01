## Jouw idee

Gebruik deze stap om je krachtige patroon te plannen. Je kunt het plannen door erover na te denken, te knutselen, te tekenen of te schrijven, of hoe je maar wilt!

![Een geanimeerde gif van drie verschillende voorbeelden die verschillende vormen gebruiken om de motieven en animaties te creëren om het patroon te doen groeien.](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Patronen hebben vaak een <span style="color: #0faeb0">culturele of religieuze betekenis</span>. Bepaalde geometrische vormen en posities kunnen symbolische of heilige betekenissen hebben. Of het patroon zich nu in architectuur, stof, kunst, koken of iets anders bevindt, het proces van het maken van het patroon kan ook belangrijk zijn.</p>

### Waarom maak je jouw krachtige patroon?

--- task ---

Denk na over het doel van het patroon dat je gaat maken.

Dat kan zijn:
- Om iets belangrijks uit jouw cultuur of die van je familie uit te drukken
- Een geometrisch patroon na te maken dat iets voor je betekent
- Iets wat je met een groep mensen maakt om een bepaald boodschap te sturen (bijvoorbeeld een quilt)
- Iets boeiends over een hobby laten zien (bijvoorbeeld kunst, wetenschap, natuur, muziek)

**Tip:** Patronen zijn overal! Je kunt ervoor kiezen om inspiratie op te doen door op patronenjacht te gaan in je omgeving of online.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Naast een symbolische betekenis, laten patronen de wiskunde zien die overal om ons heen is. Wiskunde helpt ons de wereld om ons heen te begrijpen en we kunnen wiskundige patronen vinden in kunst, literatuur en de natuur. </p>

### Voor wie is het?

--- task ---

Bedenk voor wie je je patroon gaat maken (je **doelgroep**).

Wat is de betekenis van je patroon? Zullen de kleuren, vormen of manier waarop het patroon wordt herhaald iets speciaals voor jou of je publiek betekenen?

Het delen van je patroon is een geweldige manier om iets over jezelf of je cultuur uit te drukken.

Als je als groep een patroon maakt, moet je motief dan een bepaalde afmeting of vorm hebben om bij andere delen van een groter patroon te passen?

--- /task ---

### Aan de slag

--- task ---

Open het [Krachtige patronen startersproject](https://editor.raspberrypi.org/nl-NL/projects/powerful-patterns-starter){:target="_blank"} project. De code-editor wordt geopend in een ander browsertabblad.

Als je een Raspberry Pi-account hebt, kun je op de **Save** knop klikken om een kopie op te slaan in je **Projects**.

--- /task ---

### Je project opzetten

--- task ---

Voeg code toe aan `setup()` om je project klaar te maken.

--- collapse ---

---
title: De schermgrootte instellen wanneer het programma wordt gestart
---

**Kies:** Voeg een afmeting toe die past bij het patroon dat je wilt maken. Je kunt dit later altijd wijzigen naarmate je project evolueert.

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 6
line_highlights: 7
---
def setup():
    size(400, 400) #Kies een afmeting

--- /code ---

--- /collapse ---

--- collapse ---

---
title: De achtergrondkleur instellen wanneer het programma wordt gestart
---

Bedenk waar je je achtergrond wilt tekenen. Jij kunt:
+ Voeg code toe aan `setup()` zodat de achtergrond één keer wordt getekend wanneer je het project uitvoert
+ Voeg code toe aan `draw()` zodat de achtergrond telkens opnieuw wordt getekend als de functie `draw()` wordt uitgevoerd

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 6
line_highlights: 8
---
def setup():
    size(400, 400)
    background(255, 255, 255)  # Probeer andere getallen om de kleur te veranderen

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Debug:** Mogelijk vindt je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

--- collapse ---

---
title: Ik heb mijn grootte en kleur bijgewerkt, maar het uitvoergebied blijft hetzelfde
---

Nadat je de code hebt gewijzigd, moet je je project `uitvoeren` om de wijzigingen in het uitvoergebied te zien.

--- /collapse ---

--- collapse ---

---
title: Ik heb verschillende getallen geprobeerd, maar de achtergrondkleur verandert niet
---

De maximale hoeveelheid rood, groen of blauw is `255`. Zorg ervoor dat alle `achtergrond` kleurwaarden tussen `0` en `255` liggen.

--- /collapse ---

--- /task ---


--- save ---
