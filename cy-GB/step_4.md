## Ehangu a phrofi: Patrwm

Amser creu eich patrwm llawn!

![Enghreifftiau o brosiectau gorffenedig sy'n defnyddio'r motiff dro ar ôl tro i ffurfio patrwm llawn.](images/second.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Ystyr <span style="color: #0faeb0">echdynnu</span> yw datrys problemau drwy leihau'r manylion diangen. 

</p>

--- task ---

'Drychwch ar y gacen haenog hon o Faleisia (kek lapis Sarawak). Sut mae'r motiff yn newid i greu'r patrwm cyflawn?

![Y motiff o'r prosiect kek lapis Sarawak wrth ymyl y patrwm cyflawn.](images/kek-motif.png)

'Drychwch ar y papur wal Art Deco hwn. Sut mae'r motiff yn newid i wneud y patrwm cyflawn?

![Y motiff o'r prosiect papur wal Art Deco wrth ymyl y patrwm cyflawn.](images/spirals-motif.png)

Meddyliwch am y patrwm rydych chi'n ei wneud. How does your motif change to make the overall pattern? Defnyddiwch y cwestiynau hyn i'ch helpu chi i echdynnu:
- A yw'r motiff cyfan yn cylchdroi, neu ddim ond rhan ohono?
- I ba gyfeiriad mae'n cylchdroi? Ac o faint?
- Oes haenau'n gorgyffwrdd yn y patrwm?
- Sawl gwaith mae'r motiff yn ailadrodd ei hun?
- Sut mae'r ailadrodd wedi'i drefnu (h.y. sawl rhes/colofn)?
- A yw'r lliwiau'n newid?
- Oes manylion heb eu cynnwys yn y motiff (h.y. yr eisin yn y gacen haenog o Faleisia)?

--- /task ---

--- task ---

Nawr eich bod yn gwybod mwy am sut mae'r motiff yn troi'n batrwm cyflawn, fe allwch ei raglennu gan ddefnyddio eich atebion i'r cwestiynau uchod.

**Tip:** You can 'copy' and 'paste' code from any of the examples in the introduction into your project. Mae datblygwyr proffesiynol yn gwneud hyn drwy'r amser!

Rydych chi wedi meithrin sgiliau defnyddiol iawn. Dyma eich atgoffa i'ch helpu chi i greu eich patrwm sy'n ailadrodd:

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

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

You could also use random to change the colours in your motif as it is redrawn.

--- code ---
---
language: python filename: main.py - draw()

---

    BLUE = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Newid maint eich motiff
---

If you use a motif you have already drawn, it might not be the right size.

You can use `scale()` before calling the function that draws your motif to change its size. Using an input bigger than '1' will make the motif bigger, using an input smaller than '1' will make it smaller.

--- code ---
---
language: python filename: main.py - draw()

---

    scale(0.5)  # Half size

--- /code ---

--- /collapse ---

--- /task ---

Now you can animate your pattern to show how you made it. Often, patterns have powerful cultural significance in the way that they are made, or the process.

--- task ---

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---


--- task ---

**Test:** Show someone else your project and get their feedback. Do you want make any changes to your pattern?

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: Dydy fy motiff ddim i weld yn cylchdroi
---

Make sure you are using the `radian()` function to convert degrees to radians.

--- /collapse ---

--- collapse ---
---
title: Mae'r cylchdro'n edrych yn rhyfedd
---

Gwnewch yn siŵr eich bod yn defnyddio'r swyddogaeth `radian()` i drosi graddau'n radianau.

Do you have more than one thing rotating? You may need to use `push_matrix()` and `pop_matrix()` so the screen rotates at different points at once.

--- /collapse ---

--- collapse ---
---
title: Dydy fy mhatrwm ddim yn animeiddio
---

Oes mwy nag un peth yn cylchdroi? Efallai bydd angen i chi ddefnyddio `push_matrix()` a `pop_matrix()` fel bod y sgrin yn cylchdroi ar wahanol bwyntiau ar unwaith.

--- /collapse ---

--- collapse ---
---
title: Dydy fy mhatrwm ddim yn edrych fel yr ydw i eisiau iddo edrych
---

Review the sections above on `rotate()` and `translate()`. Experiment until it looks like you want it to, and remember, mistakes are powerful!

--- /collapse ---

--- collapse ---
---
title: Dwi'n cael gwall
---

Check the syntax of your code. Are you missing any brackets `(` or `)` or a colon `:` after defining a function? Is something spelled incorrectly? Is your code indented correctly?

--- /collapse ---

--- collapse ---
---
title: Mae'r animeiddiad yn rhy gyflym/rhy araf
---

Gwiriwch gystrawen eich cod. Oes unrhyw gromfachau `(` neu `)` ar goll, neu efallai colon `:` ar ôl diffinio swyddogaeth? Oes rhywbeth wedi'i sillafu'n anghywir? A yw eich cod wedi'i fewnoli'n gywir?

--- /collapse ---

You might find a bug not listed here. Can you figure out how to fix it?

We love hearing about your bugs and how you fixed them. Use the feedback button at the bottom of this page if you found a different bug in your project.

--- /task ---


--- save ---
