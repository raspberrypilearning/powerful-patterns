## Your idea

Use this step to plan your powerful pattern. You can plan by just thinking, tinkering, drawing or writing, or however you like!

![An animated gif of three different examples using various shapes to create the motifs and animations to grow the pattern.](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Patterns often have <span style="color: #0faeb0">cultural or religious significance</span>. Certain geometric shapes and positions can have symbolic or sacred meanings. Whether the pattern is in architecture, fabric, art, cooking, or something else, the process of making the pattern can also be significant.</p>

### Why are you making your powerful pattern ?

--- task ---

Think about the purpose of the pattern you are creating.

It could be:
- To express something significant from your or your family's culture(s)
- To recreate a geometric pattern that means something to you
- Something you create with a group of people to send a certain message (for example, a quilt)
- To show something fascinating about about a hobby (for example, art, science, nature, music)

**Tip:** Patterns are everywhere! You might choose to get inspiration by going on a pattern hunt around your physical environment or online.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">As well as having symbolic meaning, patterns show the mathematics that is all around us. Mathematics helps us make sense of the world around us and we can find mathematical patterns in art, literature, and nature. </p>

### Who is it for?

--- task ---

Think about who you will make your pattern for (your **audience**).

What is the significance of your pattern? Will the colours, shapes, or way the pattern is repeated mean something special to you or your audience?

Sharing your pattern is a great way to express something about yourself or your culture.

If you are are creating a pattern as a group, does your motif need to be a certain size or shape to fit with other parts of a bigger pattern?

--- /task ---

### Get started

--- task ---

Open the [Powerful patterns starter project](https://editor.raspberrypi.org/en/projects/powerful-patterns-starter){:target="_blank"} project. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

### Setup your project

--- task ---

Add code to `setup()` to get your project ready.

--- collapse ---

---
title: Setting the screen size when your program starts
---

**Choose:** Add a size that suits the pattern you want to create. You can always change this later as your project evolves.

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup(): size(400, 400)  # Choose a size

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Setting the background colour when your program starts
---

Think about where you want to draw your background. You can:
+ Add code to `setup()` so that the background is drawn once when you run your project
+ Add code to `draw()` so that the background is redrawn each time the `draw()` function runs

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 8
---
def setup(): size(400, 400) background(255, 255, 255)  # Try different numbers to change the colour

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: I've updated my size and colour but the output area stays the same
---

After changing the code, you will need to `run` your project to see the changes in the output area.

--- /collapse ---

--- collapse ---

---
title: I've tried different numbers, but the background colour doesn't change
---

The maximum amount of red, green, or blue is `255`. Make sure all your `background` colour values are between `0` and `255`.

--- /collapse ---

--- /task ---


--- save ---
