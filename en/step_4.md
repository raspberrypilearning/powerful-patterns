## Expand and test: pattern

Now it's time to make your full pattern!

Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">Abstraction</span> is problem solving by reducing unnecessary detail. 

</p>

--- task ---

Look at this Malaysian layer cake (Kek Lapis Sarawak):

![The motif from the Kek lapis Sarawak project next to the complete pattern.](images/kek-motif.png)

How does the motif change to make the overall pattern? It looks as though the motif rotates counter clockwise around the top right corner of the motif

ANOTHER DIAGRAM?

Think about the pattern you are making. How does your motif change to make the overall pattern. Use these questions to help you abstract:
- Does the whole motif rotate?
- Does part of the motif rotate?
- What direction does it rotate? And how much does it rotate?
- Are there layers to the pattern? (like in the McEwan Tartan)
- How many times does the motif repeat itself?
- How is the repetition organised (i.e. how many rows/columns)?
- Do the colours change?
- Are there details that are not included in the motif (i.e. the icing and jam in the Malaysian layer cake)?

--- /task ---

--- task ---

Now that you know more about how the motif turns into the whole pattern, you can program it using your answers to the questions above.

You have built up some really useful skills. Here is a reminder to help you make your repeated pattern: 

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

<mark>add ingredient on loops PH doing </mark>


--- collapse ---

---
title: Random positions
---

You can add `from random import randint` at the top of **main.py**, this allows you to use the `randint` function to generate random numbers.

To use the `randint`function you need to call it your the code. 

One way to use random is to move your motif to a random position each time it draws:

--- code ---
---
language: python
filename: main.py - draw()

---

translate(randint(0, 400), randint(0, 400))

--- /code ---

You could also use random to change colours in your motif as it is redrawn. 

--- code ---
---
language: python
filename: main.py - draw()

---

BLUE = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

--- /task ---

Now you can animate your pattern to show how you made it. Often, patterns have powerful cultural significance in the way that they are made, or the process.

<mark>canva thing with picture and blurb https://www.atlasobscura.com/articles/kek-lapis-sarawak To my family, baking layer cake is a tradition that brings everyone together on special occassions. Sometimes the colours will represent a significant day. In general, we have recipes that are passed down through the generations that are unique to the family</mark>

--- task ---

[[[processing-translation]]]

[[[processing-rotation]]]

--- /task ---


--- task ---

**Test:** Show someone else your project and get their feedback. Do you want make any changes to your pattern? 

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: My motif does not appear to rotate
---

Make sure you are using the radian() function to convert degrees to radians.

--- /collapse ---

--- collapse ---
---
title: The rotation looks strange
---

Have you checked that you are using translate() from and to the right coordinates? 

Do you have more than one thing rotating? You may need to use push_matrix() and pop_matrix() so the screen rotates at different points at once.

--- /collapse ---

--- collapse ---
---
title: My pattern does not animate
---

Check you have used frame_count() properly in a loop.

--- /collapse ---

--- collapse ---
---
title: My pattern does not animate how I want it to
---

Review the collapses above on rotation() and translation(). Experiment until it looks like you want it to, and remember, mistakes are powerful!

--- /collapse ---

--- collapse ---
---
title: I get an error
---

Check the syntax of your code. Are you missing any brackets or a colon `:` after defining a function? Is something spelled incorrectly?

--- /collapse ---

--- collapse ---
---
title: The animation is too fast/too slow
---

Change the frame_rate() at the beginning of your program to get it to the speed you like.

--- /collapse ---

You might find a bug not listed here. Can you figure out how to fix it?

We love hearing about your bugs and how you fixed them. Use the feedback button at the bottom of this page if you found a different bug in your project.

--- /task ---


--- save ---
