## Розширюй та тестуй - Візерунок

Настав час зібрати повноцінний візерунок!

![Приклади готових проєктів, в яких мотив використовується багаторазово, утворюючи повноцінний візерунок.](images/second.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">Абстракція</span> - це вирішення проблем шляхом зменшення непотрібних деталей. 

</p>

--- task ---

Подивись на цей Малайзійський листковий торт (kek lapis Sarawak). Як змінюється його мотив, щоб утворився загальний візерунок?

![Мотив з проєкту Малайзійський листковий торт поруч з повним візерунком.](images/kek-motif.png)

Подивись на ці шпалери в стилі арт-деко. Як змінюється його мотив, щоб утворився загальний візерунок?

![Мотив з проєкту шпалер в стилі арт-деко поруч з повним візерунком.](images/spirals-motif.png)

Подумай про візерунок, який ти створюєш. How does your motif change to make the overall pattern? Використовуй ці питання, які допоможуть тобі зробити висновки:
- Мотив обертається повністю або тільки його частина?
- В який бік він обертається? І на скільки?
- Чи має малюнок шари, які накладаються один на одного?
- Скільки разів повторюється мотив?
- Як відбувається повторення (тобто скільки рядків/стовпчиків)?
- Чи змінюються кольори?
- Чи є якісь інші деталі, які не входять до мотиву (наприклад, глазур у Малайзійському листковому торті)?

--- /task ---

--- task ---

Тепер, коли ти знаєш більше про перетворення мотиву в цілий візерунок - запрограмуй свій мотив, використовуючи свої відповіді на питання, наведені вище.

**Tip:** You can 'copy' and 'paste' code from any of the examples in the introduction into your project. Професійні девелопери роблять це постійно!

Ти здобув(-ла) дійсно дуже корисні навички. Ось нагадування, яке допоможе тобі створити повторення візерунка:

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

--- collapse ---

---
title: Випадкові позиції
---

Ти можеш додати `from random import randint` у верхній частині **main.py** - це дозволить використовувати функцію `randint` для генерування випадкових чисел.

Для використання функції `randint` необхідно викликати її у своєму коді.

Один із способів використання рандому - це переміщення мотиву у випадкову позицію кожного разу, коли він малюється:

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
filename: main.py - draw()
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
filename: main.py - draw()
---

Make sure you are using the `radian()` function to convert degrees to radians.

--- /collapse ---

--- collapse ---
---
title: Зміна розміру мотиву
---

Переконайся, що ти використовуєш функцію `radian()` для перетворення градусів у радіани.

Do you have more than one thing rotating? You may need to use `push_matrix()` and `pop_matrix()` so the screen rotates at different points at once.

--- /collapse ---

--- collapse ---
---
filename: main.py - draw()
---

Check you have used `frame_count()` properly in a loop.

--- /collapse ---

--- collapse ---
---
title: Здається, мій мотив не обертається
---

Review the sections above on `rotate()` and `translate()`. Experiment until it looks like you want it to, and remember, mistakes are powerful!

--- /collapse ---

--- collapse ---
---
title: Ротація виглядає дивно
---

Check the syntax of your code. Are you missing any brackets `(` or `)` or a colon `:` after defining a function? Is something spelled incorrectly? Is your code indented correctly?

--- /collapse ---

--- collapse ---
---
title: Мій візерунок не має анімації
---

Change the number after `frame_rate =` in the call to the `run()` function at the end of your program to get it to the speed you like.

--- /collapse ---

You might find a bug not listed here. Can you figure out how to fix it?

We love hearing about your bugs and how you fixed them. Use the feedback button at the bottom of this page if you found a different bug in your project.

--- /task ---


--- save ---
