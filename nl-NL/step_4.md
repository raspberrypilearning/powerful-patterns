## Uitbreiden en testen - Patroon

Now that you have a **motif**, you can repeat it to make a pattern

![Voorbeelden van voltooide projecten waarbij het motief herhaaldelijk is gebruikt om een volledig patroon te vormen.](images/second.gif)


--- task ---

Move, resize and repeat the motif you have created to make a repeating pattern. Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

**Test:** Laat iemand anders je project zien en vraag feedback.

--- /task ---




### Moving, rotating and resizing

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
title: De grootte van je motief wijzigen
---

Als je een motief gebruikt dat je al hebt getekend, is het misschien niet de juiste grootte.

Je kunt `scale()` gebruiken voordat je de functie aanroept die je motief tekent om de grootte te wijzigen. Als je invoer groter is dan '1', wordt het motief groter, als je invoer kleiner is dan '1', wordt het kleiner.

--- code ---
---
language: python
filename: main.py - draw()
---

    scale(0.5)  # Half size

--- /code ---

--- /collapse ---

### Repeating

[[[generic-python-for-loop-repeat]]]

### Randomness

--- collapse ---
---
title: Willekeurige posities
---

Je kunt `from random import randint` toevoegen bovenaan **main.py**, dit staat je toe om de `randint` functie te gebruiken om willekeurige getallen te genereren.

Om de `randint` functie te gebruiken, moet je deze in je code aanroepen.

Een manier om random te gebruiken is door je motief naar een willekeurige positie te verplaatsen iedere keer dat het getekend wordt:

--- code ---
---
language: python filename: main.py - draw()

---

    push_matrix()  # Start transformation
    translate(randint(0, 400), randint(0, 400))
    draw_motif()
    pop_matrix()  # Reset transformation

--- /code ---

Je kunt random ook gebruiken om de kleuren in je motief te veranderen wanneer het opnieuw getekend wordt.

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
title: Mijn patroon ziet er niet uit zoals ik het wil
---

Bekijk de secties hierboven over `rotate()` en `translate()`. Experimenteer totdat het er uitziet zoals je het wilt, en onthoud dat fouten waardevol zijn!

--- /collapse ---

--- collapse ---
---
title: Ik krijg een foutmelding
---

Controleer de syntax van je code. Missen er haakjes `(` of `)` of een dubbele punt `:` na het definiëren van een functie? Is er iets verkeerd gespeld? Is je code correct ingesprongen?

--- /collapse ---

