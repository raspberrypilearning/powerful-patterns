## Make the pattern

Now that you have a **motif**, you can repeat it to make a pattern

![Examples of finished projects that have the motif used repeatedly to form a full pattern.](images/second.gif)


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
title: Changing the size of your motif
---

If you use a motif you have already drawn, it might not be the right size. 

You can use `scale()` before calling the function that draws your motif to change its size. Using an input bigger than '1' will make the motif bigger, using an input smaller than '1' will make it smaller. 

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
title: Random positions
---

You can add `from random import randint` at the top of **main.py**, this allows you to use the `randint` function to generate random numbers.

To use the `randint` function, you need to call it in your the code. 

One way to use random is to move your motif to a random position each time it is drawn:

--- code ---
---
language: python
filename: main.py - draw()

---

    push_matrix()  # Start transformation
    translate(randint(0, 400), randint(0, 400))
    draw_motif()
    pop_matrix()  # Reset transformation

--- /code ---

You could also use random to change the colours in your motif as it is redrawn. 

--- code ---
---
language: python
filename: main.py - draw()

---

    BLUE = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

### Bugs

--- collapse ---
---
title: My motif does not appear to rotate
---

Make sure you are using the `radian()` function to convert degrees to radians.

--- /collapse ---

--- collapse ---
---
title: The rotation looks strange
---

Have you checked that you are using `translate()` from and to the right coordinates? 

Do you have more than one thing rotating? You may need to use `push_matrix()` and `pop_matrix()` so the screen rotates at different points at once.

--- /collapse ---

--- collapse ---
---
title: My pattern does not look the way I want it to
---

Review the sections above on `rotate()` and `translate()`. Experiment until it looks like you want it to, and remember, mistakes are powerful!

--- /collapse ---

--- collapse ---
---
title: I get an error
---

Check the syntax of your code. Are you missing any brackets `(` or `)` or a colon `:` after defining a function? Is something spelled incorrectly? Is your code indented correctly?

--- /collapse ---

