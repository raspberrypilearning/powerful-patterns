## Espandi e prova - Modello geometrico

Now that you have a **motif**, you can repeat it to make a pattern

![Esempi di progetti finiti in cui il motivo viene utilizzato ripetutamente per formare un modello completo.](images/second.gif)


--- task ---

Move, resize and repeat the motif you have created to make a repeating pattern. Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

**Test:** Mostra a qualcun altro il tuo progetto e ascolta i suoi commenti.

--- /task ---




### Moving, rotating and resizing

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
title: Modificare la dimensione del modulo
---

Se utilizzi un modulo che hai già disegnato, potrebbe non essere della dimensione giusta.

Puoi usare `scale()` prima di chiamare la funzione che disegna il tuo modulo per cambiarne le dimensioni. Usare un valore di input più grande di '1' renderà il modulo più grande, usare un input più piccolo di '1' lo renderà più piccolo.

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
title: Posizioni casuali
---

Puoi aggiungere `from random import randint` nella parte superiore di **main.py**, questo ti consentirà di utilizzare la funzione `randint` per generare numeri casuali.

Per utilizzare la funzione `randint`, devi chiamarla nel codice.

Un modo per usare la casualità è spostare il modulo in una posizione casuale ogni volta che viene disegnato:

--- code ---
---
language: python filename: main.py - draw()

---

    push_matrix()  # Start transformation
    translate(randint(0, 400), randint(0, 400))
    draw_motif()
    pop_matrix()  # Reset transformation

--- /code ---

Puoi anche usare la modalità casuale per cambiare i colori del tuo motivo mentre viene ridisegnato.

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
title: Il mio modulo non sembra ruotare
---

Assicurati di utilizzare la funzione `radian()` per convertire i gradi in radianti.

--- /collapse ---

--- collapse ---
---
title: La rotazione sembra strana
---

Hai verificato di utilizzare `translate()` da e verso le coordinate corrette?

Hai più di un oggetto che ruota? Potrebbe essere necessario utilizzare `push_matrix()` e `pop_matrix()` in modo che lo schermo ruoti in punti diversi contemporaneamente.

--- /collapse ---

--- collapse ---
---
title: Il mio modello non è come vorrei
---

Rivedi le sezioni precedenti su `rotate()` e `translate()`. Sperimenta finché non è come tu vuoi e ricorda, sbagliando si impara!

--- /collapse ---

--- collapse ---
---
title: C'è un errore
---

Controlla la sintassi del tuo codice. Mancano delle parentesi `(` o `)` o i due punti `:` dopo aver definito una funzione? Qualcosa è scritto in modo sbagliato? Il tuo codice è indentato correttamente?

--- /collapse ---

