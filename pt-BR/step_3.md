## Construir e testar — Motivo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Most patterns have one design (called the **motif**) that repeats to create a pattern. 
</div>
<div>
![Um exemplo de um motivo usando várias formas para criar ele.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Draw shapes to create your motif. Use the tips at the bottom of the page if you need help.

--- /task ---

--- task ---

**Teste:** Mostre seu projeto a outra pessoa e peça sua opinião.

--- /task ---

### Formas

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]


### Cores e efeitos

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Posicione e transforme

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

### Bugs

--- collapse ---
---
title: As formas não estão alinhadas como eu esperava
---

Se você quiser que as formas sejam alinhadas, dê uma olhada mais de perto em seus pontos de coordenadas. Experimente com os números até que você tenha uma layout que você goste.

--- /collapse ---

--- collapse ---
---
title: Não consigo ver algumas das formas no meu motivo
---

A ordem em que você desenha as coisas é muito importante.

A computação gráfica é feita de camadas. Em seu motivo, cada forma é uma camada. Objetos em camadas superiores ficam na frente de objetos em camadas inferiores. Imagine recortar formas de papel. Dependendo de como você posiciona e sobrepõe esse papel, o resultado pode ser muito diferente.

--- /collapse ---

--- collapse ---
---
title: Meus círculos/quadrados não são iguais
---

O terceiro e quarto números em `elipse` e `rect` são a largura e a altura. Se você os fizer iguais, obterá um círculo ou quadrado.

--- /collapse ---



