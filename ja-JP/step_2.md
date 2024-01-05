## あなたのアイデア

このステップを使用して、あなたの迫力のある模様を計画してみてください。 ただ考えるだけでもいいし、いろいろ試したり、描いたりなど好きなようにやってみましょう。

![いろいろな形を使ってモチーフとアニメーションを作成し、パターンを広げる３つの例を紹介するアニメーションGIF](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">繰り返し模様には、よく<span style="color: #0faeb0">伝統的な色合いや宗教的な意味</span>があります。 幾何学模様が、シンボル的な意味や、神聖な意味をもつことがあります。 建築物、生地、芸術、料理など、模様を作成するプロセスも重要なことがあります。</p>

### なぜあなたは魅力的な模様を作ろうとしているのですか？

--- task ---

模様を作る目的を考えてみましょう。

例えば:
- あなたやあなたの家族の文化などの重要な何かを表現するため
- あたなにとって何か意味のある幾何学模様を再現するため
- ある種のメッセージを送るために、人々の集団と作成するもの(例えば、キルト)
- 趣味について魅力的なことを示すため(たとえば、芸術、科学、自然、音楽など)

**ヒント：** 繰り返し模様は色々なところにあります！ あなたの周りやオンラインで繰り返し模様を探すことで、インスピレーションを得ることができます。

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">繰り返し模様はシンボル的な意味を持つだけでなく、私たちの身近にある数学的な意味をあらわします。 数学は私たちが周りの世界を理解するのを助けてくれます。また、私たちは芸術、文学、自然の中で数学的な繰り返し模様を見つけることができます。 </p>

### 誰のためですか？

--- task ---

誰のために繰り返し模様を作るのかを考えてください。(あなたの**作品を見る人**).

あなたの繰り返し模様の重要なところはどこですか？ 色、形、またはパターン模様の繰り返し方法は、あなたやあなたの作品を見る人にとって特別な何かを意味しますか？

自分の繰り返し模様を紹介することは、あなた自身やあなたの文化について表現するための素晴らしい方法です。

グループで繰り返し模様を作成する場合、より大きな繰り返し模様の他の部分と合わせるために、モチーフは特定のサイズまたは形状にする必要がありますか？

--- /task ---

### 始めましょう

--- task ---

Open the [Powerful patterns starter project](https://editor.raspberrypi.org/en/projects/powerful-patterns-starter){:target="_blank"} project. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

### プロジェクトの設定

--- task ---

プロジェクトを準備するために`setup()`というコードを追加します。

--- collapse ---

---
title: プログラム開始時の画面サイズの設定
---

**選択：** 作成したいパターン模様に合ったサイズを追加します。 プロジェクトの進展に応じて、後でいつでもこれを変更できます。

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup(): size(400, 400) #サイズを選ぶ

--- /code ---

--- /collapse ---

--- collapse ---

---
title: プログラム開始時の背景色を設定
---

どのタイミングで背景を描きたいかを考えてください。 やり方は以下のとおりです。
+ プロジェクトの実行時に背景が1回描画されるようにするには、`setup()` にコードを追加します。
+ `draw()` 関数が実行されるたびに背景を再描画するには、`draw()` にコードを追加します。

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 9
---
background(255, 255, 255) #色を変えるために別の数字を試す

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**デバッグ：** プロジェクトに修正が必要なバグが見つかる場合があります。 一般的なバグは次のとおりです。

--- collapse ---

---
title: サイズと色を変更したのに、出力エリアの表示が変わらない。
---

コードを変更した後、出力エリアで変更内容を確認するには`実行`する必要があります。

--- /collapse ---

--- collapse ---

---
title: 数字を変えたのに、背景の色が変更されない。
---

赤、緑、青それぞれの最大値は`255`です。 `backgroud`に指定したそれぞれの値が`0`から`255`の間であることを確認してください。

--- /collapse ---

--- /task ---


--- save ---
