## Expandir e testar — Padrão

Now that you have a **motif**, you can repeat it to make a pattern

![Exemplos de projetos finalizados que têm o motivo usado repetidamente para formar um padrão completo.](images/second.gif)


--- task ---

Move, resize and repeat the motif you have created to make a repeating pattern. Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

**Teste:** Mostre seu projeto a outra pessoa e peça sua opinião.

--- /task ---




### Moving, rotating and resizing

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
title: Mudando o tamanho do seu motivo
---

Se você usar um motivo que já desenhou, pode não ser do tamanho certo.

Você pode usar `scale()` antes de chamar a função que desenha seu motivo para corrigir seu tamanho. Usar uma entrada maior que '1' tornará o motivo maior, usar uma entrada menor que '1' o tornará menor.

--- code ---
---
language: python
filename: main.py - draw()
---

    scale(0.5)  # Metade do tamanho

--- /code ---

--- /collapse ---

### Repeating

[[[generic-python-for-loop-repeat]]]

### Randomness

--- collapse ---
---
title: Posição aleatórias
---

Você pode adicionar `from random import randint` no topo de **main.py**, isso permite que você use a função `randint` para gerar números aleatórios.

Para usar a função `randint` você precisa chamá-la no seu código.

Uma maneira de usar random é mover seu motivo para uma posição aleatória toda vez que ele for desenhado:

--- code ---
---
language: python filename: main.py - draw()

---

    push_matrix()  # Start transformation
    translate(randint(0, 400), randint(0, 400))
    draw_motif()
    pop_matrix()  # Reset transformation

--- /code ---

Você também pode usar random para alterar as cores do seu motivo conforme ele é redesenhado.

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
title: Meu motivo não parece girar
---

Certifique-se de estar usando a função `radian()` para converter graus em radianos.

--- /collapse ---

--- collapse ---
---
título: A rotação parece estranha
---

Você verificou se está usando `translate()` com início e fim das coordenadas corretas?

Você tem mais de uma coisa girando? Você pode precisar usar `push_matrix()` e `pop_matrix()` para que a tela gire em diferentes pontos ao mesmo tempo.

--- /collapse ---

--- collapse ---
---
title: Meu padrão não está do jeito que eu quero
---

Revise as seções acima em `rotate()` e `translate()`. Experimente até parecer como o que você quer, e lembre-se, aprendemos com os erros!

--- /collapse ---

--- collapse ---
---
título: Eu recebo um erro
---

Verifique a sintaxe do seu código. Está faltando algum colchete `(` ou `)` ou dois pontos `:` depois de definir uma função? Algo está escrito incorretamente? Seu código está recuado corretamente?

--- /collapse ---

