## Будуй та тестуй - Мотив

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Настав час створити мотив - перший елемент твого візерунка. 
</div>
<div>
![Приклад мотиву з використанням різних форм для створення мотиву.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Draw shapes to create your motif. Use the tips at the bottom of the page if you need help.

--- /task ---

--- task ---

**Test:** Run your code to see what your design looks like.

--- /task ---

### Фігури та зображення

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]


### Кольори та ефекти

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Розташування та перетворення

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

### Bugs

--- collapse ---
---
title: Фігури вирівняні не так, як я очікував(-ла)
---

Якщо ти хочеш, щоб фігури були вирівняні - придивись уважніше до своїх координатних точок. Експериментуй з цифрами, поки не отримаєш потрібний тобі варіант.

--- /collapse ---

--- collapse ---
---
title: Я не бачу деякі фігури на моєму мотиві
---

Порядок, в якому ти малюєш деталі, дуже важливий.

Комп'ютерна графіка побудована з багатьох шарів. У твоєму мотиві кожна фігура - це шар. Об'єкти на вищих шарах знаходяться перед об'єктами на нижчих шарах. Уяви, що ти вирізаєш всі фігури з паперу. Залежно від того, як ти будеш розташовувати та накладати цей папір, кінцевий результат може виглядати зовсім по-різному.

--- /collapse ---

--- collapse ---
---
title: Кола/квадрати не рівні
---

Третій та четвертий номери у `ellipse` та `rect` - це ширина та висота. Якщо зробити їх однаковими - вийде коло або квадрат.

--- /collapse ---



