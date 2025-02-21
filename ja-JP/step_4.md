## あなたが作っているパターンについて考えてみてください。

Now that you have a **motif**, you can repeat it to make a pattern

![モチーフを繰り返し使用してパターン全体を形成したプロジェクト完成版の例。](images/second.gif)


--- task ---

繰り返し模様の完成版を作りましょう。 Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

**テスト：** プロジェクトを他の人に見せて、フィードバックをもらいます。

--- /task ---




### Moving, rotating and resizing

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
title: モチーフのサイズを変化させる
---

すでに描いたモチーフを使用すると、サイズが合わない場合があります。

モチーフを描く関数を呼び出す前に`scale()` を使うことで、サイズを変更することができます。 「1」より大きい数字を入力するとモチーフが大きくなり、「1」より小さい数字を入力するとモチーフが小さくなります。

--- code ---
---
language: python
filename: main.py - draw()
---

    scale(0.5) #半分の大きさ

--- /code ---

--- /collapse ---

### Repeating

[[[generic-python-for-loop-repeat]]]

### Randomness

--- collapse ---
---
title: ランダムな位置
---

`from random import randint` を **main.py**の先頭に入れることで、 乱数を生成する`randint` 関数を使えるようになります。

`randint` 関数を使うためには、コードの中で呼び出す必要があります。

乱数は、モチーフを描画するたびにランダムな位置にモチーフを移動するような場合に使います。

--- code ---
---
language: python filename: main.py - draw()

---

    push_matrix() #トランスフォーメーションの開始
    translate(randint(0, 400), randint(0, 400))
    draw_motif()
    pop_matrix() #トランスフォーメーションのリセット

--- /code ---

色を変えてモチーフを再描画する場合にも使うことができます。

--- code ---
---
language: python filename: main.py - draw()

---

    BLUE = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

### Bugs

--- collapse ---
---
title: モチーフが回転しない
---

度（degree）をラジアン（radian）に変換するのに、`radian()` 関数を使用していることを確認してください。

--- /collapse ---

--- collapse ---
---
title: 回転がおかしい
---

`translate()` を使用するとき、正しい座標点を指定しているか確認しましたか？

回転しているものが複数ありますか？ 同時に異なる場所で回転させるためには、`push_matrix()` と `pop_matrix()` を使用する必要があります。

--- /collapse ---

--- collapse ---
---
title: パターンが思い通りにできない
---

`rotate()` と `translate()`について、これまでのセクションを確認してください。 思い通りになるまで試行してください。 間違いから学ぶことができます。

--- /collapse ---

--- collapse ---
---
title: エラーが発生します。
---

コードの構文を確認してください。 関数の定義のあと、括弧 `(` や `)`、コロン `:` を忘れていませんか？ スペルが間違っていませんか？ コードを正しくインデントしていますか？

--- /collapse ---

