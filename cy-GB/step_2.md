## Eich syniad

Defnyddiwch y cam hwn i gynllunio eich patrwm pwerus. Fe allwch chi gynllunio drwy feddwl, rhoi cynnig ar bethau, darlunio neu ysgrifennu, neu sut bynnag dymunwch chi!

![Gif wedi'i animeiddio o dair enghraifft wahanol yn defnyddio amryw o siapiau i greu'r motiffau a'r animeiddiadau i ehangu'r patrwm.](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Mae gan batrymau <span style="color: #0faeb0">arwyddocâd diwylliannol neu grefyddol</span> yn aml. Mae ystyr symbolaidd neu gysegredig i rai siapiau a safleoedd geometrig. Mae'r broses o wneud y patrwm yn gallu bod yn arwyddocaol hefyd, a hynny mewn patrymau ym maes pensaernïaeth, ffabrig, celf, coginio neu rywbeth arall.</p>

### Pam ydych chi'n gwneud eich patrwm pwerus?

--- task ---

Meddyliwch am bwrpas y patrwm rydych chi'n ei greu.

Fe allai fod:
- I fynegi rhywbeth arwyddocaol o ddiwylliant eich teulu
- I ailgreu patrwm geometrig sy'n golygu rhywbeth i chi
- Yn rhywbeth rydych chi'n ei greu â grŵp o bobl i anfon neges benodol (er enghraifft cwilt)
- I ddangos rhywbeth diddorol am hobi (er enghraifft celf, gwyddoniaeth, byd natur, cerddoriaeth)

**Cyngor:** Mae patrymau bob man! Efallai byddwch chi'n dewis mynd ar drywydd ysbrydoliaeth drwy chwilio am batrymau yn eich amgylchedd ffisegol neu ar-lein.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Yn ogystal â chael ystyr symbolaidd, mae patrymau'n dangos y fathemateg sydd o'n cwmpas. Mae mathemateg yn ein helpu i wneud synnwyr o'r byd o'n cwmpas ac mae patrymau mathemategol i'w gweld mewn celf, llenyddiaeth a byd natur. </p>

### Ar gyfer pwy mae'r patrwm?

--- task ---

Meddyliwch i bwy byddwch chi'n gwneud eich patrwm (eich **cynulleidfa**).

Beth yw arwyddocâd eich patrwm? A fydd y lliwiau, y siapiau, neu'r ffordd mae'r patrwm yn cael ei ailadrodd yn golygu rhywbeth arbennig i chi neu eich cynulleidfa?

Mae rhannu eich patrwm yn ffordd wych o fynegi rhywbeth amdanoch chi eich hun neu eich diwylliant.

Os ydych chi'n creu patrwm mewn grŵp, oes angen i'ch motiff fod yn faint neu'n siâp penodol i gyd-fynd â rhannau eraill o batrwm mwy?

--- /task ---

### Dechrau arni

--- task ---

Agorwch y [prosiect dechreuol Patrymau pwerus](https://trinket.io/python/6c4a0c6406){:target=blank } a chlicio'r botwm Remix.

--- /task ---

### Gosod eich prosiect

--- task ---

Ychwanegwch god at `setup()` i baratoi eich prosiect.

--- collapse ---

---
title: Gosod maint y sgrin pan fydd eich rhaglen yn dechrau
---

**Dewis:** Ychwanegwch faint sy'n addas i'r patrwm rydych chi am ei greu. Fe allwch chi newid hyn nes 'mlaen wrth i'ch prosiect ddatblygu beth bynnag.

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup(): size(400, 400) #Choose a size

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Gosod y lliw cefndir pan fydd eich rhaglen yn dechrau
---

Meddyliwch ble ydych chi am lunio eich cefndir. Fe allwch chi:
+ Ychwanegu cod at `setup()` fel bod y cefndir yn cael ei lunio pan fyddwch chi'n rhedeg eich prosiect
+ Ychwanegu cod at `draw()` fel bod y cefndir yn cael ei ail-lunio bob tro mae'r swyddogaeth `draw()` yn rhedeg

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
line_highlights: 9
---

    background(255, 255, 255) #Try different numbers to change the colour

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Difa chwilod:** Efallai bydd angen i chi drwsio chwilod yn eich prosiect. Dyma rai chwilod cyffredin.

--- collapse ---

---
title: Dwi wedi diweddaru fy maint a fy lliw ond mae'r ardal allbwn yn dal yr un fath
---

Ar ôl newid y cod, bydd angen i chi redeg eich prosiect gyda `run` i weld y newidiadau yn yr ardal allbwn.

--- /collapse ---

--- collapse ---

---
title: Dwi wedi rhoi cynnig ar wahanol rifau ond dydy'r lliw cefndir ddim yn newid
---

Y lefel uchaf o goch, gwyrdd neu las yw `255`. Gwnewch yn siŵr bod eich holl werthoedd lliw `background` rhwng `0` a `255`.

--- /collapse ---

--- /task ---


--- save ---
