## Make the pattern

Now that you have a **motif**, you can repeat it to make a pattern

![Przykłady ukończonych projektów, w których motyw jest wielokrotnie używany do utworzenia pełnego wzoru.](images/second.gif)


--- task ---

Move, resize and repeat the motif you have created to make a repeating pattern. Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

**Test:** Run the code to see how your pattern looks.

--- /task ---




### Moving, rotating and resizing

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
Title: Zmiana rozmiaru motywu
---

Jeśli używasz już narysowanego motywu, może to być niewłaściwy rozmiar.

Możesz użyć skali `()` przed wywołaniem funkcji rysującej motyw, aby zmienić jego rozmiar. Użycie wejścia większego niż "1" spowoduje, że motyw będzie większy, a użycie wejścia mniejszego niż "1" sprawi, że będzie mniejszy.

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
Title: Losowe pozycje
---

Możesz dodać ` from random import ` u góry **.**, dzięki czemu możesz użyć funkcji ` ` do generowania liczb losowych.

Aby użyć funkcji ` `, musisz wywołać ją w swoim kodzie.

Jednym ze sposobów użycia losowego jest przesunięcie motywu do losowej pozycji za każdym razem, gdy jest rysowany:

--- code ---
---
language: python filename: main.py - draw()

---

    push_matrix()  # Start transformation
    translate(randint(0, 400), randint(0, 400))
    draw_motif()
    pop_matrix()  # Reset transformation

--- /code ---

Możesz również użyć losowego, aby zmienić kolory w swoim motywie podczas jego ponownego rysowania.

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
Title: Mój motyw nie wydaje się obracać
---

Upewnij się, że używasz funkcji ` radian()` do konwersji stopni na radiany.

--- /collapse ---

--- collapse ---
---
Title: Obrót wygląda dziwnie
---

Czy sprawdziłeś, że używasz ` TRANSLATE()` z i do właściwych współrzędnych?

Czy masz więcej niż jedną rzecz obracającą się? Być może będziesz musiał użyć ` push_matrix()` i ` pop_matrix()`, aby ekran obracał się w różnych punktach naraz.

--- /collapse ---

--- collapse ---
---
Title: Mój wzór nie wygląda tak, jak chcę
---

Przejrzyj powyższe sekcje na temat ` rotate()` i ` TRANSLATE()`. Eksperymentuj, aż będzie wyglądało na to, że chcesz i pamiętaj, błędy są potężne!

--- /collapse ---

--- collapse ---
---
Title: Dostaję błąd
---

Sprawdź składnię swojego kodu. Czy po zdefiniowaniu funkcji brakuje Ci nawiasów `(` lub `)` lub dwukropka `:`? Czy coś jest napisane nieprawidłowo? Czy Twój kod jest wcięty prawidłowo?

--- /collapse ---

