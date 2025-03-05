## Початок роботи

--- task ---

Відкрий [стартовий проєкт «Барвисті візерунки»](https://editor.raspberrypi.org/en/projects/powerful-patterns-starter){:target="_blank"}.

--- /task ---

### Налаштуй свій проєкт

--- task ---

Вибери розмір і колір тла.

--- code ---
---
language: python line_numbers: true line_number_start: 6
line_highlights: 7-8
---
def setup(): size(400, 400)  # Вибери розмір background(255, 255, 255)  # Спробуй різні числа, щоб змінити колір

--- /code ---

--- /task ---

--- task ---

**Протестуй:** запусти свій проєкт і поглянь, що змінилося.

Максимальне значення для червоного, зеленого, або синього - `255`. Переконайся, що всі значення кольору для тла `background` знаходяться між `0` та `255`.

--- /task ---


