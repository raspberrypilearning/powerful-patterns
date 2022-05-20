## فكرتك

استخدم هذه الخطوة لتخطيط نمطك القوي. يمكنك التخطيط بمجرد التفكير أو الإصلاح أو الرسم أو الكتابة ، أو كيفما تشاء!

![An animated gif of three different examples using various shapes to create the motifs and animations to grow the pattern.](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">غالبًا ما يكون للأنماط <span style="color: #0faeb0">دلالات ثقافية أو دينية</span>. يمكن أن يكون لبعض الأشكال والمواقف الهندسية معاني رمزية أو مقدسة. سواء كان النمط في الهندسة المعمارية أو النسيج أو الفن أو الطهي أو أي شيء آخر، فإن عملية صنع النمط يمكن أن تكون مهمة أيضًا.</p>

### لماذا تصنع نمطك القوي؟

--- task ---

فكر في الغرض من النمط الذي تقوم بإنشائه.

من الممكن أن تكون:
- للتعبير عن شيء مهم من ثقافتك أو ثقافات عائلتك
- لإعادة إنشاء نمط هندسي يعني لك شيئًا
- شيء تقوم بإنشائه مع مجموعة من الأشخاص لإرسال رسالة معينة (على سبيل المثال ، لحاف)
- لإظهار شيء رائع حول هواية (على سبيل المثال ، الفن ، والعلوم ، والطبيعة ، والموسيقى)

**نصيحة:** الأنماط موجودة في كل مكان! You might choose to get inspiration by going on a pattern hunt around your physical environment or online.

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

Open the [Powerful patterns starter project](https://trinket.io/python/6c4a0c6406){:target=blank } and click on the remix button.

--- /task ---

### Setup your project

--- task ---

Add code to `setup()` to get your project ready.

--- collapse ---

---
title: Setting the screen size when your programme starts
---

**Choose:** Add a size that suits the pattern you want to create. You can always change this later as your project evolves.

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup(): size(400, 400) #Choose a size

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Setting the background colour when your programme starts
---

Think about where you want to draw your background. You can:
+ Add code to `setup()` so that the background is drawn once when you run your project
+ Add code to `draw()` so that the background is redrawn each time the `draw()` function runs

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
line_highlights: 9
---

    background(255, 255, 255) #Try different numbers to change the colour

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
