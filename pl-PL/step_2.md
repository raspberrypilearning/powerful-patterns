## Twój pomysł

Użyj tego kroku, aby zaplanować swój potężny wzór. Możesz planować, po prostu myśląc, majstrując, rysując lub pisząc, lub jak chcesz!

![Animowany gif z trzema różnymi przykładami, używając różnych kształtów do tworzenia motywów i animacji, aby rozwijać wzór.](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Wzory często mają znaczenie kulturowe lub religijne <span style="color: #0faeb0"> </span>. Niektóre geometryczne kształty i pozycje mogą mieć znaczenie symboliczne lub święte. Niezależnie od tego, czy wzór jest w architekturze, tkaninie, sztuce, gotowaniu, czy czymś innym, proces tworzenia wzoru może być również znaczący.</p>

### Dlaczego tworzysz swój potężny wzór?

--- task ---

Zastanów się nad celem tworzonego przez Ciebie wzoru.

To może być:
- Aby wyrazić coś znaczącego z kultury Twojej lub Twojej rodziny
- Aby odtworzyć geometryczny wzór, który coś dla Ciebie znaczy
- Coś, co tworzysz z grupą osób, aby wysłać określoną wiadomość (na przykład kołdrę)
- Aby pokazać coś fascynującego o hobby (na przykład sztuka, nauka, przyroda, muzyka)

** Wskazówka:Wzory ** są wszędzie! Możesz zainspirować się, udając się na polowanie na wzory wokół swojego środowiska fizycznego lub online.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Wzory nie tylko mają znaczenie symboliczne, ale pokazują matematykę, która jest wokół nas. Matematyka pomaga nam zrozumieć otaczający nas świat i możemy znaleźć matematyczne wzorce w sztuce, literaturze i przyrodzie. </p>

### Dla kogo to jest?

--- task ---

Zastanów się, dla kogo stworzysz swój wzór (Twój ** **).

Jakie jest znaczenie twojego wzoru? Czy kolory, kształty lub sposób powtarzania wzoru będą znaczyły coś wyjątkowego dla Ciebie lub Twoich odbiorców?

Dzielenie się swoim wzorem to świetny sposób na wyrażenie czegoś o sobie lub swojej kulturze.

Jeśli tworzysz wzór jako grupę, czy twój motyw musi mieć określony rozmiar lub kształt, aby pasował do innych części większego wzoru?

--- /task ---

### Zaczynamy

--- task ---

Otwórz projekt startowy [ Powerful Patterns ](https://editor.raspberrypi.org/en/projects/powerful-patterns-starter){:target="_blank"}. Edytor kodu otworzy się w innej karcie przeglądarki.

Jeśli masz konto Raspberry Pi, możesz kliknąć przycisk ** Saved ** , aby zapisać kopię w swoich projektach ** **.

--- /task ---

### Skonfiguruj swój projekt

--- task ---

Dodaj kod do ` setup()`, aby przygotować swój projekt.

--- collapse ---

---
Title: Ustawianie rozmiaru ekranu po uruchomieniu programu
---

** Wybierz:** Dodaj rozmiar, który pasuje do wzoru, który chcesz utworzyć. Zawsze możesz to zmienić później, gdy Twój projekt się rozwija.

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup(): size(400, 400)  # Choose a size

--- /code ---

--- /collapse ---

--- collapse ---

---
Title: Ustawianie koloru tła po uruchomieniu programu
---

Zastanów się, gdzie chcesz narysować tło. Możesz:
+ Dodaj kod do ` setup()`, aby tło było rysowane raz podczas uruchamiania projektu
+ Dodaj kod do ` draw()`, aby tło było rysowane za każdym razem, gdy uruchomiona jest funkcja ` draw()`

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 8
---
def setup(): size(400, 400) background(255, 255, 255)  # Try different numbers to change the colour

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Debugowanie:** Być może znajdziesz błędy w swoim projekcie, które musisz naprawić. Oto kilka typowych błędów.

--- collapse ---

---
Title: Zaktualizowałem swój rozmiar i kolor, ale obszar wyjściowy pozostaje taki sam
---

Po zmianie kodu, będziesz musiał uruchomić ` ` swój projekt, aby zobaczyć zmiany w obszarze wyjściowym.

--- /collapse ---

--- collapse ---

---
Title: Próbowałem różnych liczb, ale kolor tła się nie zmienia
---

Maksymalna ilość czerwonego, zielonego lub niebieskiego to ` 255 `. Upewnij się, że wszystkie wartości kolorów ` ` mieszczą się w przedziale ` 0 ` i ` 255 `.

--- /collapse ---

--- /task ---


--- save ---
