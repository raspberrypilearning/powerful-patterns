## Build and test: Motif

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now it's time to make your motif, the first element of your pattern.
</div>
<div>
![An example of a motif using various shapes to create the motif.](images/motif.png){:width="300px"}
</div>
</div>

The process of making your motif is the same as what computer scientists often do when they create a program or solution to a problem. This process is called **decomposition** and you will use decomposition to create your motif.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">Decomposition</span> is breaking something down into parts that are smaller and easier to understand. This means that you can build a pattern one part at a time until it is complete.</p>

Look at the pattern you want to recreate. How can you break it down into one single element (the motif) that repeats?

In this example, an art deco wallpaper pattern has been decomposed into the basic collection of shapes (five circles overlayed) that makes the motif:

![A single five circle motif next to an image of the art deco complete pattern with many copies of the motif.](images/motif-pattern.png)

**Tip:** ನೀವು ಏನನ್ನಾದರೂ ಸೇರಿಸಿದಾಗ ನಿಮ್ಮ ಯೋಜನೆಯನ್ನು ಪರೀಕ್ಷಿಸಲು ಮರೆಯದಿರಿ. ನೀವು ಹೆಚ್ಚು ಬದಲಾವಣೆಗಳನ್ನು ಮಾಡುವ ಮೊದಲು ದೋಷಗಳನ್ನು ಕಂಡುಹಿಡಿಯುವುದು ಮತ್ತು ಸರಿಪಡಿಸುವುದು ತುಂಬಾ ಸುಲಭ.

--- task ---

You have built up some really useful skills. Here is a reminder to help you make your motif:

### Shapes

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

### Colours and effects

[[[generic-theory-simple-colours]]]

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Position and transform

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- task ---

**Test:** Show someone else your project and get their feedback. Do you want make any changes to your motif?

--- /task ---

--- task ---

**Debug:** ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನಲ್ಲಿ ನೀವು ಸರಿಪಡಿಸಬೇಕಾದ ಕೆಲವು ದೋಷಗಳನ್ನು ನೀವು ಕಾಣಬಹುದು. Here are some common bugs.

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

ನಿಮ್ಮ ದೋಷಗಳ ಬಗ್ಗೆ ಮತ್ತು ನೀವು ಅವುಗಳನ್ನು ಹೇಗೆ ಸರಿಪಡಿಸಿದ್ದೀರಿ ಎಂದು ಕೇಳಲು ನಾವು ಇಷ್ಟಪಡುತ್ತೇವೆ. Use the feedback button at the bottom of this page if you found a different bug in your project.

--- /task ---

--- save ---
