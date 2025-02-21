## Розширюй та тестуй - Візерунок

Настав час зібрати повноцінний візерунок!

![Приклади готових проєктів, в яких мотив використовується багаторазово, утворюючи повноцінний візерунок.](images/second.gif)


--- task ---

Move, resize and repeat the motif you have created to make a repeating pattern. Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

**Test:** Run the code to see how your pattern looks.

--- /task ---




### Moving, rotating and resizing

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
title: Випадкові позиції
---

Якщо ти використовуєш вже намальований мотив, він може бути неправильного розміру.

Ти можеш використовувати `scale()` перед викликом функції, яка малює мотив, щоб змінити його розмір. Using an input bigger than '1' will make the motif bigger, using an input smaller than '1' will make it smaller.

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
title: Випадкові позиції
---

Для використання функції `randint` необхідно викликати її у своєму коді.

Один із способів використання рандому - це переміщення мотиву у випадкову позицію кожного разу, коли він малюється:

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

Ти також можеш використовувати випадковий порядок для зміни кольорів твого мотиву під час його малювання.

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
title: Зміна розміру мотиву
---

Переконайся, що ти використовуєш функцію `radian()` для перетворення градусів у радіани.

--- /collapse ---

--- collapse ---
---
title: Зміна розміру мотиву
---

Переконайся, що ти використовуєш функцію `radian()` для перетворення градусів у радіани.

У тебе обертається більше одного елемента? Тобі може знадобитися використати `push_matrix()` та `pop_matrix()`, щоб екран обертався одночасно в різних точках.

--- /collapse ---

--- collapse ---
---
title: Здається, мій мотив не обертається
---

Переглянь наведені вище пункти про `rotate()` та `translate()`. Експериментуй, поки не отримаєш бажаного результату, і пам'ятай, що помилки - це сила!

--- /collapse ---

--- collapse ---
---
title: Ротація виглядає дивно
---

Перевір синтаксис свого коду. Чи не пропущені якісь дужки `(` або `)`, або двокрапка `:` після визначення функції? Щось неправильно написано? Чи правильно розставлені у коді відступи?

--- /collapse ---

