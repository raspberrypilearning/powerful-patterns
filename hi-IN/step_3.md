## Create a motif

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Most patterns have one design (called the **motif**) that repeats to create a pattern. 
</div>
<div>
![An example of a motif using various shapes to create the motif.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Draw shapes to create your motif. Use the tips at the bottom of the page if you need help.

--- /task ---

--- task ---

**Test:** Run your code to see what your design looks like.

--- /task ---

### Shapes

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]


### Colours and effects

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Position and transform

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

### Bugs

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

Computer graphics are made of layers. In your motif, each shape is a layer. Objects on higher layers sit in front of objects on lower layers. सोचिये सभी आकृतियों को कागज़ से आपको काटना है। इस पर निर्भर करते हुए कि आप उस पेपर को कैसे व्यवस्थित और ओवरलैप करते हैं, अंतिम परिणाम बहुत अलग दिख सकता है।

--- /collapse ---

--- collapse ---
---
title: My circles/squares are not equal
---

The third and fourth numbers in `ellipse` and `rect` are the width and height. If you make them the same, you will get a circle or square.

--- /collapse ---



