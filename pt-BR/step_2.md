## A sua ideia

Use esta etapa para planejar seu super padrão. Você pode planejar apenas pensando, mexendo, desenhando, escrevendo, ou como quiser!

![Um gif animado de três exemplos diferentes usando várias formas para criar os motivos e as animações para aumentar o padrão.](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Os padrões geralmente têm <span style="color: #0faeb0">significado cultural ou religioso</span>. Certas formas geométricas e posições podem ter significados simbólicos ou até sagrados. Seja o padrão em arquitetura, tecido, arte, culinária ou qualquer outra coisa, o processo de criação do padrão também pode ser importante.</p>

### Por que você está fazendo seu padrão poderoso?

--- task ---

Pense no propósito do padrão que você está criando.

Pode ser:
- Para expressar algo sobre sua cultura ou da sua familia
- Para recriar um padrão geométrico que tenha significado para você
- Algo que você cria com um grupo de pessoas para enviar uma determinada mensagem (por exemplo, uma colcha)
- Para mostrar algo fascinante sobre um hobby (por exemplo, arte, ciência, natureza, música)

**Dica:** Padrões estão em toda parte! Você pode escolher por se inspirar com uma observando por padrões ao seu redor ou pela internet.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Além de ter um significado para nós, os padrões mostram como matemática pode descrever o ambiente ao nosso redor. A matemática nos ajuda a entender o mundo e como podemos encontrar certos padrões na arte, na literatura e na natureza. </p>

### Para quem é isso?

--- task ---

Pense para quem você fará seu padrão (seu **público**).

Qual é o significado do seu padrão? As cores, as formas ou como o padrão é repetido significam algo especial para você ou seu público?

Compartilhar seu padrão é uma ótima maneira de expressar algo sobre você ou sua cultura.

Se você estiver criando um padrão em grupo, seu motivo precisa ter um determinado tamanho ou forma para se encaixar em outras partes de um padrão maior?

--- /task ---

### Iniciar

--- task ---

Abra o [projeto inicial super padrões](https://trinket.io/python/6c4a0c6406){:target=blank} e clique no botão remix.

--- /task ---

### Prepare seu projeto

--- task ---

Adicione código no `setup()` para preparar seu projeto.

--- collapse ---

---
title: Configurando o tamanho da tela quando o programa é iniciado
---

**Escolha:** Adicione um tamanho adequado ao padrão que deseja criar. Você sempre pode alterar isso mais tarde à medida que seu projeto evolui.

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
title: Configurando a cor de fundo da tela quando o programa é iniciado
---

Escolha onde você quer desenhar o plano de fundo. Você pode:
+ Adicione código no `configurar()` para que o plano de fundo seja desenhado uma vez quando você executar seu projeto
+ Adicione código no `desenhar()` para que o plano de fundo seja redesenhado toda vez que a função `desenhar()` for executada

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

**Depurar:** Você pode encontrar alguns bugs em seu projeto que precisa corrigir. Aqui estão alguns bugs comuns.

--- collapse ---

---
title: Atualizei o tamanho e cor, mas a janela do programa permanece a mesma
---

Depois de alterar o código, você precisará `executar` seu projeto para ver as alterações na tela.

--- /collapse ---

--- collapse ---

---
title: Eu tentei diferentes números, mas a cor de fundo não se altera
---

O valor máxima de vermelho, verde ou azul é `255`. Tenha certeza de que todos os valores de cor de`fundo` estejam entre `0` e `255`.

--- /collapse ---

--- /task ---


--- save ---
