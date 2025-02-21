## Create a motif

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Most patterns have one design (called the **motif**) that repeats to create a pattern. 
</div>
<div>
![przykład motywu używającego różnych kształtów do tworzenia motywu.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Draw shapes to create your motif. Use the tips at the bottom of the page if you need help.

--- /task ---

--- task ---

**Test:** Run your code to see what your design looks like.

--- /task ---

### Kształty

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]


### Kolory i efekty

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Pozycjonowanie i przekształcanie

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

### Bugs

--- collapse ---
---
Title: Kształty nie są wyrównane tak, jak się spodziewałem
---

Jeśli chcesz, aby kształty były wyrównane, przyjrzyj się bliżej swoim punktom współrzędnych. Eksperymentuj z liczbami, aż będziesz mieć pożądany układ.

--- /collapse ---

--- collapse ---
---
Title: Nie widzę niektórych kształtów w moim motywie
---

Kolejność rysowania rzeczy jest bardzo ważna.

Grafika komputerowa składa się z warstw. W Twoim motywie każdy kształt jest warstwą. Obiekty na wyższych warstwach znajdują się przed obiektami na niższych warstwach. Wyobraź sobie wycinanie wszystkich kształtów z papieru. W zależności od tego, jak układasz i nakładasz ten papier, końcowy wynik może wyglądać bardzo inaczej.

--- /collapse ---

--- collapse ---
---
Title: Moje kółka/kwadraty nie są równe
---

Trzecia i czwarta liczba w ` ` i ` ` to szerokość i wysokość. Jeśli uczynisz je takimi samymi, otrzymasz okrąg lub kwadrat.

--- /collapse ---



