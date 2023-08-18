## Expandir e testar: Padrão

Agora é hora de fazer o seu padrão completo!

![Exemplos de projetos finalizados que têm o motivo usado repetidamente para formar um padrão completo.](images/second.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">Abstração</span> é a solução de problemas reduzindo detalhes desnecessários. 

</p>

--- task ---

Olhe para este bolo de camadas da Malásia (kek lapis Sarawak). Como o motivo modifica a formar do padrão em geral?

![O motivo do projeto kek lapis Sarawak ao lado do padrão completo.](images/kek-motif.png)

Olhe para este papel de parede art déco. Como o motivo modifica a formar do padrão em geral?

![O motivo do projeto de papel de parede art déco ao lado do padrão completo.](images/spirals-motif.png)

Pense no padrão que você está fazendo. Como seu motivo muda para fazer o padrão geral. Use estas perguntas para ajudá-lo a abstrair:
- Tudo ou parte do motivo gira?
- Em que direção ele gira? E quanto?
- Existem camadas no padrão que se sobrepõem?
- Quantas vezes o motivo se repete?
- Como a repetição é organizada (ou seja, quantas linhas/colunas)?
- As cores mudam?
- Existem detalhes que não estão incluídos no motivo (ou seja, a cobertura do bolo de camadas da Malásia)?

--- /task ---

--- task ---

Agora que você conhece mais como o motivo se transforma em todo o padrão, você pode programá-lo usando suas respostas às perguntas acima.

**Dica:** Não esqueça que você pode 'Ver Dentro' qualquer um dos exemplos na introdução e 'copiar' e 'colar' código em seu projeto. Desenvolvedores profissionais fazem isso o tempo todo!

Você desenvolveu algumas habilidades realmente úteis. Aqui está um lembrete para ajudá-lo a fazer seu padrão repetido:

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

--- collapse ---

---
title: Posição aleatórias
---

Você pode adicionar `from random import randint` no topo de **main.py**, isso permite que você use a função `randint` para gerar números aleatórios.

Para usar a função `randint` você precisa chamá-la no seu código.

Uma maneira de usar random é mover seu motivo para uma posição aleatória toda vez que ele for desenhado:

--- code ---
---
language: python
filename: main.py - draw()

---

    push_matrix()  # Iniciar transformação
    translate(randint(0, 400), randint(0, 400))
    desenho_motivo()
    pop_matrix()  # Redefinir transformação

--- /code ---

Você também pode usar random para alterar as cores do seu motivo conforme ele é redesenhado.

--- code ---
---
language: python
filename: main.py - draw()

---

AZUL = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

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

--- /task ---

Agora você pode animar seu padrão para mostrar como você o fez. Muitas vezes, os padrões têm um grande significado cultural na maneira como são feitos ou no processo.

--- task ---

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---


--- task ---

**Teste:** Mostre seu projeto a outra pessoa e peça sua opinião. Deseja fazer alguma alteração em seu padrão?

--- /task ---

--- task ---

**Depurar:** Você pode encontrar alguns bugs em seu projeto que precisa corrigir. Aqui estão alguns bugs comuns.

--- collapse ---

---
title: Meu motivo não parece girar
---

Certifique-se de estar usando a função `radian()` para converter graus em radianos.

--- /collapse ---

--- collapse ---
---
title: A rotação parece estranha
---

Você verificou se está usando `translate()` com início e fim das coordenadas corretas?

Você tem mais de uma coisa girando? Você pode precisar usar `push_matrix()` e `pop_matrix()` para que a tela gire em diferentes pontos ao mesmo tempo.

--- /collapse ---

--- collapse ---
---
title: Meu padrão não anima
---

Confira se você usou `frame_count()` corretamente em um loop.

--- /collapse ---

--- collapse ---
---
title: Meu padrão não está do jeito que eu quero
---

Revise as seções acima em `rotate()` e `translate()`. Experimente até parecer como o que você quer, e lembre-se, aprendemos com os erros!

--- /collapse ---

--- collapse ---
---
title: Eu recebo um erro
---

Verifique a sintaxe do seu código. Está faltando algum colchete `(` ou `)` ou dois pontos `:` depois de definir uma função? Algo está escrito incorretamente? Seu código está recuado corretamente?

--- /collapse ---

--- collapse ---
---
title: A animação é muito rápida/muito lenta
---

Altere o `frame_rate()` no início do seu programa para obter a velocidade que você gosta.

--- /collapse ---

Você pode encontrar um bug que não está listado aqui. Você consegue descobrir como consertá-lo?

Adoraríamos saber sobre seus bugs e como você os corrigiu. Use o botão Enviar comentários na parte inferior desta página e nos diga se você encontrou um bug diferente em seu projeto.

--- /task ---


--- save ---
