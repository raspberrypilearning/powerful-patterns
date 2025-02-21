## قم بالتوسيع والاختبار - النمط

Now that you have a **motif**, you can repeat it to make a pattern

![أمثلة على المشاريع المنجزة التي تم استخدامها بشكل متكرر لتشكيل نمط كامل.](images/second.gif)


--- task ---

Move, resize and repeat the motif you have created to make a repeating pattern. Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

**اختبار:** اعرض مشروعك على شخص آخر واطلب منه إبداء الرأي.

--- /task ---




### Moving, rotating and resizing

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
title: تغيير حجم التصميم الخاص بك
---

إذا كنت تستخدم تصميم رسمته بالفعل ، فقد لا تكون بالحجم الصحيح.

يمكنك استخدام Scale `()` قبل استدعاء الدالة التي ترسم الشكل الخاص بك لتغيير حجمها. استخدام مُدخل أكبر من "1" سيجعل الشكل أكبر ، واستخدام مُدخل أقل من "1" سيجعله أصغر.

--- code ---
---
language: python
filename: main.py - draw()
---

    scale(0.5) #نصف الحجم

--- /code ---

--- /collapse ---

### Repeating

[[[generic-python-for-loop-repeat]]]

### Randomness

--- collapse ---
---
title: مواقع عشوائية
---

يمكنك إضافة `من Randint الاستيراد العشوائي` في الجزء العلوي من **main.py**، وهذا يسمح لك باستخدام وظيفة `randint` لتوليد أرقام عشوائية.

لاستخدام وظيفة `randint` ، تحتاج إلى استدعائها في الكود الخاص بك.

احدى استخدامات الطرق العشوائية هو تحريك العنصر الخاص بك إلى موضع عشوائي في كل مرة يتم رسمه فيها:

--- code ---
---
language: python filename: main.py - draw()

---

    push_matrix() #ابدأ التحول 
    translate(randint(0, 400), randint(0, 400)) 
    draw_motif() 
    pop_matrix() #إعادة تعيين التحول

--- /code ---

يمكنك أيضًا استخدام عشوائي لتغيير الألوان في الشكل الخاص بك أثناء إعادة رسمه.

--- code ---
---
filename: main.py - draw()

---

    BLUE = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

### Bugs

--- collapse ---
---
title: لا يبدو أن الشكل الخاص بي يدور
---

تأكد من أنك تستخدم دالة `radian()` لتحويل الدرجات إلى راديان.

--- /collapse ---

--- collapse ---
---
title: الاستدارة تبدو غريبة
---

هل تحققت من أنك تستخدم `translate()` من وإلى الإحداثيات الصحيحة؟

هل لديك أكثر من شيء يدور؟ قد تحتاج إلى استخدام `push_matrix()` و `pop_matrix()` بحيث تدور الشاشة في نقاط مختلفة في وقت واحد.

--- /collapse ---

--- collapse ---
---
title: نمطي لا يبدو بالشكل الذي أريده
---

راجع الأقسام أعلاه في `rotate()` و `translate()`. جرب حتى يبدو أنك تريد ذلك ، وتذكر أن الأخطاء قوية!

--- /collapse ---

--- collapse ---
---
title: لدي خطأ
---

تحقق من صياغة التعليمات البرمجية الخاصة بك. هل تفتقد أي أقواس `(` أو `)` أو نقطتان `:` بعد تحديد دالة؟ هل شيء مكتوب بشكل غير صحيح؟ هل مسافة بادئة التعليمات البرمجية الخاصة بك بشكل صحيح؟

--- /collapse ---

