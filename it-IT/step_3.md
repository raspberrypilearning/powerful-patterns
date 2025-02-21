## Realizza e testa - Il tema (o motivo)

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Most patterns have one design (called the **motif**) that repeats to create a pattern. 
</div>
<div>
![Un esempio di un motivo che utilizza varie forme per creare il modulo.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Draw shapes to create your motif. Use the tips at the bottom of the page if you need help.

--- /task ---

--- task ---

**Test:** Mostra a qualcun altro il tuo progetto e ascolta i suoi commenti.

--- /task ---

### Forme

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]


### Colori ed effetti

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Posizionamento e trasformazioni

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

### Bugs

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



