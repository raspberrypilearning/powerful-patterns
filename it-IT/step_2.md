## La tua idea

Usa questo passaggio per progettare il tuo magnifico motivo geometrico. Puoi pianificare semplicemente pensando, armeggiando, disegnando o scrivendo, o come preferisci!

![Una gif animata di tre diversi esempi che utilizzano varie forme per creare motivi e le animazioni per la creazione del motivo completo.](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">I motivi hanno spesso un <span style="color: #0faeb0">significato culturale o religioso</span>. Alcune forme e posizioni geometriche possono avere significati simbolici o sacri. Che il modello riguardi l'architettura, del tessuto, l'arte, la cucina o qualcos'altro, anche il processo di creazione del motivo può essere significativo.</p>

### Perché stai creando il tuo motivo magnifico?

--- task ---

Pensa allo scopo del motivo geometrico che stai creando.

Può servire a:
- Esprimere qualcosa di significativo della tua cultura o di quella della tua famiglia
- Ricreare un motivo geometrico che significhi qualcosa per te
- Qualcosa che crei con un gruppo di persone per inviare un determinato messaggio (ad esempio, una trapunta)
- Per mostrare qualcosa di affascinante riguardo a un hobby (ad esempio arte, scienza, natura, musica)

**Suggerimento:** I motivi sono ovunque! Potresti scegliere di trarre ispirazione andando alla ricerca di motivi presenti intorno a te oppure online.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Oltre ad avere un significato simbolico, i motivi mostrano la matematica che ci circonda. La matematica ci aiuta a dare un senso al mondo che ci circonda e possiamo trovare modelli matematici nell'arte, nella letteratura e nella natura. </p>

### Per chi è?

--- task ---

Pensa alla persona per cui realizzerai il tuo motivo (il tuo **pubblico**).

Qual è il significato del tuo motivo? I colori, le forme o il modo in cui il modulo viene ripetuto significheranno qualcosa di speciale per te o per il tuo pubblico?

Condividere il tuo motivo è un ottimo modo per esprimere qualcosa su te stesso o sulla tua cultura.

Se stai creando un motivo geometrico in gruppo, il motivo deve avere una certa dimensione o forma per adattarsi ad altre parti di un disegno più grande?

--- /task ---

### Per cominciare

--- task ---

Apri il [progetto iniziale Meravigliosi motivi](https://editor.raspberrypi.org/it-IT/projects/powerful-patterns-starter){:target="_blank"}. L'editor del codice si aprirà in un'altra scheda del browser.

Se hai un account Raspberry Pi, puoi fare clic sul pulsante **Salva** per salvare una copia nei tuoi **Progetti**.

--- /task ---

### Imposta il tuo progetto

--- task ---

Aggiungi il codice a `setup()` per iniziare il tuo progetto.

--- collapse ---

---
title: Impostare le dimensioni dello schermo all'avvio del programma
---

**Scegli:** Aggiungi una dimensione adatta al motivo che desideri creare. Puoi sempre modificarla in seguito man mano che il progetto cresce.

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 6
line_highlights: 7
---
def setup():
    size(400, 400)  # Scegli una dimensione

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Impostare il colore dello sfondo iniziale del programma
---

Decidi dove vuoi disegnare il tuo sfondo. Puoi:
+ Aggiungere il codice a `setup()` in modo che lo sfondo venga disegnato una volta sola quando esegui il progetto
+ Aggiungere il codice a `draw()` in modo che lo sfondo venga ridisegnato ogni volta che viene eseguita la funzione `draw()`

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
    background(255, 255, 255)  # Prova diversi numeri per cambiare il colore

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Debug:** Potresti trovare alcuni bug nel tuo progetto, che dovrai correggere. Ecco alcuni bug comuni.

--- collapse ---

---
title: Ho aggiornato dimensione e colore ma l'area di output rimane la stessa
---

Dopo aver modificato il codice, dovrai premere `Run` per vedere le modifiche nell'area di output.

--- /collapse ---

--- collapse ---

---
title: Ho provato diversi numeri, ma il colore dello sfondo non cambia
---

La quantità massima di rosso, verde o blu è `255`. Assicurati che tutti i valori del colore dello `sfondo` siano compresi tra `0` e `255`.

--- /collapse ---

--- /task ---


--- save ---
