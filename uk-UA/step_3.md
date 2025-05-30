## Створи мотив

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Більшість візерунків мають один елемент («мотив»), який повторюється багато разів і таким чином створює візерунок. 
</div>
<div>
![Приклад мотиву з використанням різних форм.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Намалюй якісь фігури, щоб створити свій мотив. Якщо тобі потрібна допомога, прочитай поради внизу сторінки.

--- /task ---

--- task ---

**Протестуй:** запусти код і подивись, як виглядає твій мотив.

--- /task ---

### Фігури

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

### Налагодження

--- collapse ---
---
title: Фігури вирівняні не так, як потрібно
---

Якщо ти хочеш, щоб фігури були вирівняні, — придивись уважніше до точок координат. Спробуй різні числа, поки не отримаєш потрібне тобі розташування.

--- /collapse ---

--- collapse ---
---
title: Я бачу не всі фігури у своєму мотиві
---

Порядок, у якому ти малюєш деталі, дуже важливий.

Комп'ютерна графіка побудована з шарів. У твоєму мотиві кожна фігура — це шар. Об'єкти на вищих шарах знаходяться перед об'єктами на нижчих шарах. Уяви, що ти вирізаєш всі фігури з паперу. Залежно від того, як ти розташуєш паперові деталі одна зверху іншої, кінцевий результат може виглядати по-різному.

--- /collapse ---

--- collapse ---
---
title: Кола чи квадрати не рівні
---

Третій та четвертий числа в `ellipse` та `rect` — це ширина й висота. Якщо зробити їх однаковими — вийде коло або квадрат.

--- /collapse ---



