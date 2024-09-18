## Costruisci e prova: moduli

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
È arrivato il momento di realizzare il tuo modulo, il primo elemento del tuo motivo geometrico.
</div>
<div>
![Un esempio di un motivo che utilizza varie forme per creare il modulo.](images/motif.png){:width="300px"}
</div>
</div>

Il processo di creazione del tuo modulo è lo stesso che spesso fanno gli informatici quando creano un programma o cercano la soluzione a un problema. Questo processo è chiamato **scomposizione** e ora lo utilizzerai per creare il tuo modulo.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">La decomposizione</span> consiste nello scomporre qualcosa in parti più piccole e più facili da comprendere. Ciò significa che puoi costruire un motivo un pezzp alla volta, fino al suo completamento.</p>

Guarda il motivo che vuoi ricreare. Come puoi scomporlo in un unico elemento (il modulo) che si ripeterà?

In questo esempio, un motivo di sfondo Art Dèco è stato scomposto nella gruppo base di forme (cinque cerchi sovrapposti) che costituisce il modulo:

![Un singolo motivo a cinque cerchi accanto a un'immagine del modello completo Art Dèco con molte copie del modulo.](images/motif-pattern.png)

**Suggerimento:** Ricordati di testare il tuo progetto ogni volta che aggiungi qualcosa. È molto più semplice trovare e correggere i bug, se lo fai prima di aggiungere ulteriori modifiche.

--- task ---

Hai acquisito alcune abilità davvero utili. Ecco un promemoria per aiutarti a realizzare il tuo modulo:

### Forme

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

### Colori ed effetti

[[[generic-theory-simple-colours]]]

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Posizionamento e trasformazioni

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- task ---

**Test:** Mostra a qualcun altro il tuo progetto e ascolta i suoi commenti. Vuoi apportare modifiche al tuo modulo?

--- /task ---

--- task ---

**Debug:** Potresti trovare alcuni bug nel tuo progetto che dovrai correggere. Ecco alcuni bug comuni.

--- collapse ---
---
title: Le forme non sono allineate come mi sarei aspettato
---

Se vuoi che le forme siano allineate, dai un'occhiata più da vicino alle tue coordinate. Sperimenta con i numeri finché non ottieni il layout che desideri.

--- /collapse ---

--- collapse ---

---
title: Non riesco a vedere alcune forme nel mio modulo
---

L'ordine in cui disegni le cose è molto importante.

La grafica computerizzata è fatta di strati (layer). Nel tuo modulo, ogni forma è uno strato. Gli oggetti sugli strati superiori si trovano davanti, e coprono, gli oggetti degli strati sottostanti. Immagina di ritagliare le forme nella carta. A seconda di come disponi e sovrapponi i pezzi di carta, il risultato finale potrebbe apparire molto diverso.

--- /collapse ---

--- collapse ---

---
title: I miei cerchi/quadrati non hanno lati uguali
---

Il terzo e il quarto numero nell'`ellisse` e nel `rettangolo` sono la larghezza e l'altezza. Se li rendi uguali, otterrai un cerchio o un quadrato.

--- /collapse ---

Potresti trovare un bug non elencato qui. Riesci a capire come risolverlo?

Ci piace conoscere i tuoi bug e come li hai risolti. Utilizza il pulsante di feedback in fondo a questa pagina se hai trovato un bug diverso nel tuo progetto.

--- /task ---

--- save ---
