## Rozwiń i przetestuj: Wzór

Teraz nadszedł czas, aby stworzyć swój pełny wzór!

![Przykłady ukończonych projektów, w których motyw jest wielokrotnie używany do utworzenia pełnego wzoru.](images/second.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0"> Abstrakcja </span> to rozwiązanie problemu poprzez zmniejszenie zbędnych szczegółów. 

</p>

--- task ---

Spójrz na to malezyjskie ciasto warstwowe (kek lapis Sarawak). Jak zmienia się motyw, aby stworzyć ogólny wzór?

![Motyw z projektu kek lapis Sarawak obok pełnego wzoru.](images/kek-motif.png)

Spójrz na tę tapetę w stylu art deco. Jak zmienia się motyw, aby stworzyć ogólny wzór?

![Motyw z projektu tapety art deco obok pełnego wzoru.](images/spirals-motif.png)

Pomyśl o wzorcu, który tworzysz. Jak zmienia się twój motyw, aby stworzyć ogólny wzór? Użyj tych pytań, aby pomóc Ci abstrakcyjnie:
- Czy całość lub część motywu obraca się?
- W jakim kierunku obraca się? I o ile?
- Czy w szyku są warstwy, które nakładają się na siebie?
- Ile razy motyw się powtarza?
- Jak zorganizowane jest powtórzenie (tj. ile wierszy/kolumn)?
- Czy kolory się zmieniają?
- Czy istnieją szczegóły, które nie są zawarte w motywie (tj. wisienka w malezyjskim torcie warstwowym)?

--- /task ---

--- task ---

Teraz, gdy wiesz więcej o tym, jak motyw zmienia się w cały wzór, możesz go zaprogramować, korzystając z odpowiedzi na powyższe pytania.

** Wskazówka:** Możesz "skopiować" i "wkleić" kod z dowolnego przykładu we wstępie do swojego projektu. Profesjonalni programiści robią to cały czas!

Zbudowałeś kilka naprawdę użytecznych umiejętności. Oto przypomnienie, które pomoże Ci stworzyć powtarzający się wzór:

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

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

--- collapse ---

---
Title: Zmiana rozmiaru motywu
---

Jeśli używasz już narysowanego motywu, może to być niewłaściwy rozmiar.

Możesz użyć skali `()` przed wywołaniem funkcji rysującej motyw, aby zmienić jego rozmiar. Użycie wejścia większego niż "1" spowoduje, że motyw będzie większy, a użycie wejścia mniejszego niż "1" sprawi, że będzie mniejszy.

--- code ---
---
language: python filename: main.py - draw()

---

    scale(0.5)  # Half size

--- /code ---

--- /collapse ---

--- /task ---

Teraz możesz animować swój wzór, aby pokazać, jak go stworzyłeś. Często wzory mają potężne znaczenie kulturowe w sposobie ich tworzenia lub procesie.

--- task ---

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---


--- task ---

** Test:** Pokaż komuś inny swój projekt i uzyskaj ich opinię. Czy chcesz wprowadzić jakieś zmiany w swoim szyku?

--- /task ---

--- task ---

** Debug:** Możesz znaleźć kilka błędów w swoim projekcie, które musisz naprawić. Oto kilka typowych robaków.

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
Title: Mój wzorzec nie jest animowany
---

Sprawdź, czy poprawnie użyłeś ` frame_count()` w pętli.

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

--- collapse ---
---
Title: Animacja jest zbyt szybka / zbyt powolna
---

Zmień liczbę po ` frame_rate = ` w wywołaniu do funkcji ` run()` na końcu programu, aby uzyskać żądaną prędkość.

--- /collapse ---

Możesz znaleźć robaka, którego tutaj nie ma. Czy możesz dowiedzieć się, jak to naprawić?

Uwielbiamy słyszeć o twoich robakach i o tym, jak je naprawiłeś. Użyj przycisku opinii u dołu tej strony, jeśli znalazłeś innego robaka w swoim projekcie.

--- /task ---


--- save ---
