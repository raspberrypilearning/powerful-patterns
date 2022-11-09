## Construir e testar: Motivo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Agora é hora de fazer o seu motivo, o primeiro elemento do seu padrão.
</div>
<div>
![Um exemplo de um motivo usando várias formas para criar ele.](images/motif.png){:width="300px"}
</div>
</div>

O processo de fazer seu motivo se espelha o que os cientistas da computação costumam fazer quando criam um programa ou solução de problemas. Este processo é chamado **decomposição** e você usará a decomposição para criar seu motivo.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">** Decomposição **</span> é quebrar um projeto em partes que são menores e mais fáceis de entender. Isso significa que você pode construir um padrão, uma parte por vez, até concluí-lo.</p>

Olhe para o padrão que você deseja recriar. Como você pode decompô-lo em um único elemento (o motivo) que se repete?

Neste exemplo, um padrão de papel de parede art déco foi decomposto na coleção básica de formas (cinco círculos sobrepostos) que compõe o motivo:

![Um único motivo de cinco círculos ao lado de uma imagem do padrão art déco completo com muitas cópias do motivo.](images/motif-pattern.png)

**Dica:** Lembre-se de testar seu projeto sempre que adicionar algo. É muito mais fácil localizar e corrigir bugs antes de fazer mais alterações.

--- task ---

Você desenvolveu algumas habilidades realmente úteis. Aqui está um lembrete para ajudá-lo a fazer seu motivo:

### Formas e imagens

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-add-image]]]

### Cores e efeitos

[[[generic-theory-simple-colours]]]

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Posicione e transforme

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- task ---

**Teste:** Mostre seu projeto a outra pessoa e peça sua opinião. Deseja fazer alguma alteração em seu motivo?

--- /task ---

--- task ---

**Depurar:** Você pode encontrar alguns bugs em seu projeto que precisa corrigir. Aqui estão alguns bugs comuns.

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

Você pode encontrar um bug que não está listado aqui. Você consegue descobrir como consertá-lo?

Adoraríamos saber sobre seus bugs e como você os corrigiu. Use o botão enviar comentários na parte inferior desta página e nos diga se você encontrou um bug diferente em seu projeto.

--- /task ---

--- save ---
