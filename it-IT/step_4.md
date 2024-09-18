## Espandi e prova: motivo geometrico

Ora è il momento di realizzare il tuo motivo completo!

![Esempi di progetti finiti in cui il motivo viene utilizzato ripetutamente per formare un modello completo.](images/second.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">L'astrazione</span> è la risoluzione dei problemi eliminando i dettagli non necessari. 

</p>

--- task ---

Guarda questa torta a strati malese (torta a strati Sarawak). Come varia il modulo per creare il motivo finale?

![Il motivo del progetto della torta a strati Sarawak, accanto al modello completo.](images/kek-motif.png)

Guarda questo sfondo Art Dèco. Come varia il modulo per creare il motivo finale?

![Il modulo dello sfondo Art Dèco accanto al modello completo.](images/spirals-motif.png)

Pensa al motivo che stai realizzando. Come varia il modulo per creare il motivo finale? Usa queste domande per aiutarti ad astrarre:
- Il motivo ruota tutto o in parte?
- In che direzione ruota? E di quanto?
- Ci sono strati nel modello che si sovrappongono?
- Quante volte si ripete il modulo?
- Come è organizzata la ripetizione (su quante righe/colonne)?
- I colori cambiano?
- Ci sono dettagli che non sono inclusi nel modulo (ad esempio la glassa nella torta a strati malese)?

--- /task ---

--- task ---

Ora che sai di più su come il modulo si trasforma in un disegno completo, puoi programmarlo utilizzando le risposte alle domande precedenti.

**Suggerimento:** Puoi "copiare" e "incollare" il codice da qualsiasi esempio tra quelli che trovi nell'introduzione al tuo progetto. Gli sviluppatori professionisti lo fanno continuamente!

Hai acquisito alcune abilità davvero utili. Ecco un promemoria per aiutarti a realizzare il tuo motivo ripetuto:

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

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

--- collapse ---

---
title: Modificare la dimensione del modulo
---

Se utilizzi un modulo che hai già disegnato, potrebbe non essere della dimensione giusta.

Puoi usare `scale()` prima di chiamare la funzione che disegna il tuo modulo per cambiarne le dimensioni. Usare un valore di input più grande di '1' renderà il modulo più grande, usare un input più piccolo di '1' lo renderà più piccolo.

--- code ---
---
language: python filename: main.py - draw()

---

    scale(0.5)  # Half size

--- /code ---

--- /collapse ---

--- /task ---

Ora puoi animare il tuo modello per mostrare come lo hai realizzato. Spesso i motivi hanno un potente significato culturale nel modo in cui vengono realizzati o nel processo.

--- task ---

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---


--- task ---

**Test:** Mostra a qualcun altro il tuo progetto e ascolta i suoi commenti. Vuoi apportare modifiche al tuo motivo?

--- /task ---

--- task ---

**Debug:** Potresti trovare alcuni bug nel tuo progetto, dovrai correggerli. Ecco alcuni bug comuni.

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
title: Il mio motivo non si anima
---

Verifica di aver utilizzato `frame_count()` correttamente in un ciclo.

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

--- collapse ---
---
title: L'animazione è troppo veloce/troppo lenta
---

Cambia il numero dopo `frame_rate =` nella chiamata alla funzione `run()` alla fine del programma per portarlo alla velocità che preferisci.

--- /collapse ---

Potresti trovare un bug non elencato qui. Riesci a capire come risolverlo?

Ci piace conoscere i tuoi bug e come li hai risolti. Utilizza il pulsante di feedback in fondo a questa pagina, se hai trovato un bug diverso nel tuo progetto.

--- /task ---


--- save ---
