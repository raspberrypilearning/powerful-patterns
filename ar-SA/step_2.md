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

**نصيحة:** الأنماط موجودة في كل مكان! قد تختار الحصول على الإلهام من خلال البحث عن أنماط حول بيئتك المادية أو عبر الإنترنت.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">بالإضافة إلى وجود معنى رمزي ، الأنماط تُظهر الرياضيات الموجودة في كل مكان حولنا. تساعدنا الرياضيات في فهم العالم من حولنا ويمكننا العثور على أنماط رياضية في الفن والأدب والطبيعة. </p>

### لمن هذا؟

--- task ---

فكر حول لمن سوف تعد نمطك من اجل (**جمهورك**).

ما هي أهمية النمط الخاص بك؟ هل الألوان أو الأشكال أو الطريقة التي يتكرر بها النمط تعني شيئًا خاصًا لك أو لجمهورك؟

تعد مشاركة نمطك طريقة رائعة للتعبير عن شيء ما عنك أو عن ثقافتك.

إذا كنت تقوم بإنشاء نمط كمجموعة ، فهل يحتاج التصميم الخاص بك إلى حجم أو شكل معين ليناسب الأجزاء الأخرى من نمط أكبر؟

--- /task ---

### البدء

--- task ---

افتح [مشروع بداية الأنماط القوية](https://trinket.io/python/6c4a0c6406){: target = blank } وانقر على زر ريمكس.

--- /task ---

### قم بإعداد مشروعك

--- task ---

أضف الكود إلى `setup ()` لتجهيز مشروعك.

--- collapse ---

---
title: ضبط حجم الشاشة عند بدء البرنامج
---

**اختر:** أضف مقاسًا يناسب النمط الذي تريد إنشاءه. يمكنك دائمًا تغيير هذا لاحقًا مع تطور مشروعك.

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
title: ضبط لون الشاشة عند بدء البرنامج
---

فكر في المكان الذي تريد رسم خلفيتك فيه. تستطيع:
+ أضف الكود إلى `setup ()` بحيث يتم رسم الخلفية مرة واحدة عند تشغيل مشروعك
+ أضف الكود إلى `draw ()` بحيث يتم إعادة رسم الخلفية في كل مرة يتم فيها تشغيل وظيفة `draw ()`

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

**تصحيح:** قد تجد بعض الأخطاء في مشروعك والتي تحتاج إلى إصلاحها. فيما يلي بعض الأخطاء الشائعة.

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
