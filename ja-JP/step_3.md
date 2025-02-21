## 作成とテスト：モチーフ

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Most patterns have one design (called the **motif**) that repeats to create a pattern. 
</div>
<div>
![さまざまな形を使用して作ったモチーフの例] (images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Draw shapes to create your motif. Use the tips at the bottom of the page if you need help.

--- /task ---

--- task ---

**テスト：** プロジェクトを他の人に見せて、フィードバックをもらいます。

--- /task ---

### Shapes

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]


### 色と効果

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### 配置と展開

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

### Bugs

--- collapse ---
---
title: 形が思うように並ばない
---

形状を揃えたい場合は、座標点をよく見てください。 好きなレイアウトになるまで、数値を変えてみてください。

--- /collapse ---

--- collapse ---
---
title: モチーフの中に描いた形が見あたらない
---

描く順序は、とても大切です。

コンピュータグラフィックスはレイヤー構造になっています。 モチーフの中では、それぞれの形がレイヤーになっています。 下のレイヤーにあるオブジェクトの前に、上のレイヤーのオブジェクトが置かれるのです。 紙からすべての形を切り取ると想像してみてください。 その紙で作った形をどう並べ、どう重ねるかによって、最終的な仕上がりは大きく変わってきます。

--- /collapse ---

--- collapse ---
---
title: 描いた円/正方形の形がくずれている
---

`ellipse`や`rect`の３番目と４番目の数字で、幅と高さが決まります。 ３番目と４番目の数字を同じにすると、円や正方形を描くことができます。

--- /collapse ---



