## Build and test: motif

Now it's time to make your motif, the first element of your pattern.

![An animated gif of three different examples using various shapes to create the motifs and animations to grow the pattern.](images/ideas-2.gif)

The process of making your motif mirrors what computer scientists often do when they create a program or solution to a problem. This process is called **decomposition** and you will use decomposition to create your motif.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">Decomposition</span> is breaking something down into parts that are smaller and easier to understand. This means that you can build a pattern one part at a time until it is complete.</p>

Look at the pattern you want to recreate. How can you break it down into one single element (the motif) that repeats?

In this example, an art deco wallpaper pattern has been decomposed into the basic collection of shapes (five circles overlayed) that makes the motif:

![A single five circle motif next to an image of the art deco complete pattern with many copies of the motif.](images/motif-pattern.png)

**Tip:** Remember to test your project each time you add something. It is much easier to find and fix bugs before you make more changes.

--- task ---

You have built up some really useful skills. Here is a reminder to help you make your motif:

### Shapes and images

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-add-image]]]

### Colours and effects

[[[generic-theory-simple-colours]]]

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Position and transform

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

<mark>add ingredient on loops PH doing </mark>

--- /task ---

--- task ---

**Test:** Show someone else your project and get their feedback. Do you want make any changes to your motif? 

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: Shapes are not aligned as I expected
---

If you want the shapes to be aligned, then take a closer look at your coordinate points. Experiment with the numbers until you have the layout you want. 

--- /collapse ---

--- collapse ---

---
title: I can't see some of the shapes in my motif
---

The order in which you draw things is very important.

Computer graphics are made of layers. In your motif, each shape is a layer. Objects on higher layers sit in front of objects on lower layers. Imagine cutting all the shapes out of paper. Depending on how you arrange and overlap that paper, the final result could look very different.

--- /collapse ---

--- collapse ---

---
title: My circles/squares are not equal
---

The third and fourth numbers in `ellipse` and `rect` are the width and height. If you make them the same, you will get a circle or square. 

--- /collapse ---

You might find a bug not listed here. Can you figure out how to fix it?

We love hearing about your bugs and how you fixed them. Use the feedback button at the bottom of this page if you found a different bug in your project.

--- /task ---

--- save ---
