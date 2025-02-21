## Ehangu a phrofi - Patrwm

Amser creu eich patrwm llawn!

![Enghreifftiau o brosiectau gorffenedig sy'n defnyddio'r motiff dro ar ôl tro i ffurfio patrwm llawn.](images/second.gif)


--- task ---

Move, resize and repeat the motif you have created to make a repeating pattern. Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

'Drychwch ar y papur wal Art Deco hwn. Sut mae'r motiff yn newid i wneud y patrwm cyflawn?

--- /task ---




### Moving, rotating and resizing

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
title: Newid maint eich motiff
---

Rydych chi wedi meithrin sgiliau defnyddiol iawn. Dyma eich atgoffa i'ch helpu chi i greu eich patrwm sy'n ailadrodd:

Fe allwch chi ddefnyddio `scale()` cyn galw'r swyddogaeth sy'n llunio eich motiff i newid ei faint. Using an input bigger than '1' will make the motif bigger, using an input smaller than '1' will make it smaller.

--- code ---
---
language: python
title: Newid maint eich motiff
---

    scale(0.5)  # Half size

--- /code ---

--- /collapse ---

### Repeating

[[[generic-python-for-loop-repeat]]]

### Randomness

--- collapse ---
---
title: Safleoedd ar hap
---

Fe allwch chi ychwanegu `from random import randint` ar frig **main.py**, mae hyn yn gadael i chi ddefnyddio'r swyddogaeth `randint` i gynhyrchu rhifau ar hap.

I ddefnyddio'r swyddogaeth `randint`, mae angen i chi ei galw yn eich cod.

Un ffordd o ddefnyddio nodwedd ar hap yw symud eich motiff i safle ar hap bob tro mae'n cael ei lunio:

--- code ---
---
language: python filename: main.py - draw()

---

    push_matrix()  # Start transformation
    translate(randint(0, 400), randint(0, 400))
    draw_motif()
    pop_matrix()  # Reset transformation

--- /code ---

Fe allech chi hefyd ddefnyddio nodwedd ar hap i newid lliwiau eich motiff wrth iddo gael ei ail-lunio.

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
title: Dydy fy motiff ddim i weld yn cylchdroi
---

Gwnewch yn siŵr eich bod yn defnyddio'r swyddogaeth `radian()` i drosi graddau'n radianau.

--- /collapse ---

--- collapse ---
---
title: Mae'r cylchdro'n edrych yn rhyfedd
---

Gwnewch yn siŵr eich bod yn defnyddio'r swyddogaeth `radian()` i drosi graddau'n radianau.

Oes mwy nag un peth yn cylchdroi? Efallai bydd angen i chi ddefnyddio `push_matrix()` a `pop_matrix()` fel bod y sgrin yn cylchdroi ar wahanol bwyntiau ar unwaith.

--- /collapse ---

--- collapse ---
---
title: Dydy fy mhatrwm ddim yn edrych fel yr ydw i eisiau iddo edrych
---

Tarwch olwg arall ar yr adrannau uchod ynghylch `rotate()` a `translate()`. Arbrofwch nes ei fod yn edrych fel rydych chi eisiau iddo edrych a chofiwch, mae camgymeriadau'n bwerus!

--- /collapse ---

--- collapse ---
---
title: Dwi'n cael gwall
---

Gwiriwch gystrawen eich cod. Oes unrhyw gromfachau `(` neu `)` ar goll, neu efallai colon `:` ar ôl diffinio swyddogaeth? Oes rhywbeth wedi'i sillafu'n anghywir? A yw eich cod wedi'i fewnoli'n gywir?

--- /collapse ---

