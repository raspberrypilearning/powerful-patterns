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

**Tip:** Remember to test your project each time you add something. अधिक बदलाव करने से पहले गलती को खोजना और ठीक करना बहुत आसान है।

--- task ---

आपने वास्तव में कुछ उपयोगी कौशल बनाए हैं। Here is a reminder to help you make your motif:

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

**डीबग:** आपको अपने प्रोजेक्ट में कुछ बग मिल सकते हैं जिन्हें आपको ठीक करने की आवश्यकता है। यहाँ कुछ सामान्य बग हैं।

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

आपको एक बग मिल सकता है जो यहाँ सूचीबद्ध नहीं है। क्या आप इसे ठीक करने का तरीका समझ सकते हैं?

हमें आपके बग्स के बारे में सुनना अच्छा लगता है और आपने उन्हें कैसे ठीक किया है। यदि आपको अपने प्रोजेक्ट में एक अलग बग मिलता है, तो इस पेज के नीचे प्रतिक्रिया बटन का उपयोग करें।

--- /task ---

--- save ---
