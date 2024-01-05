## Tu idea

Usa este paso para planificar tu patrón poderoso. ¡Puedes planificar con solo pensar, retocar, dibujar, escribir o como desees!

![Un gif animado de tres ejemplos diferentes que usan varias formas para crear los motivos y animaciones para hacer crecer el patrón.](images/ideas-1.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Los patrones a menudo tienen un <span style="color: #0faeb0">significado cultural o religioso</span>. Ciertas posiciones y formas geométricas pueden tener significados simbólicos o sagrados. Ya sea que el patrón esté en la arquitectura, la tela, el arte, la cocina o cualquier otra cosa, el proceso de creación del patrón también puede ser significativo.</p>

### ¿Por qué estás creando tu patrón poderoso?

--- task ---

Piensa en el propósito del patrón que estás creando.

Podría ser:
- Para expresar algo significativo de tu cultura o la de tu familia
- Para recrear un patrón geométrico que signifique algo para ti
- Algo que creas junto con un grupo de personas para enviar un mensaje determinado (por ejemplo, una colcha)
- Para mostrar algo fascinante sobre un pasatiempo (por ejemplo, arte, ciencia, naturaleza, música)

**Sugerencia:** ¡Los patrones están en todas partes! Puedes elegir inspirarte buscando patrones en tu entorno físico o en línea.

--- /task ---

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">Además de tener un significado simbólico, los patrones muestran las matemáticas que nos rodean. Las matemáticas nos ayudan a darle sentido al mundo que nos rodea y podemos encontrar patrones matemáticos en el arte, la literatura y la naturaleza. </p>

### ¿Para quién?

--- task ---

Piensa para quién crearás tu patrón (tu **audiencia**).

¿Cuál es el significado de tu patrón? ¿Los colores, las formas o la forma de repetición del patrón significarán algo especial para ti o tu audiencia?

Compartir tu patrón es una excelente manera de expresar algo sobre ti mismo o tu cultura.

Si están creando un patrón como grupo, ¿tu motivo debe tener un tamaño o forma determinados para encajar con otras partes de un patrón más grande?

--- /task ---

### Empezar

--- task ---

Abre el proyecto de inicio [Patrones poderosos](https://trinket.io/python/362bc749c3){:target=blank} y haz clic en el botón Remix. The code editor will open in another browser tab.

If you have a Raspberry Pi account, you can click on the **Save** button to save a copy to your **Projects**.

--- /task ---

### Configura tu proyecto

--- task ---

Agrega código a `setup()` para preparar tu proyecto.

--- collapse ---

---
title: Configurar el tamaño de la pantalla cuando se inicia el programa
---

**Elige:** Agrega un tamaño (size) que se adapte al patrón que quieres crear. Siempre puedes cambiar esto más adelante a medida que tu proyecto evolucione.

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup(): size(400, 400) #Elige un tamaño (size)

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Configurar el color de fondo cuando se inicia el programa
---

Piensa dónde quieres dibujar tu fondo. Puedes:
+ Agregar código a `setup ()` para que el fondo se dibuje una vez cuando ejecutes tu proyecto
+ Agrega código a `draw()` para que el fondo se vuelva a dibujar cada vez que se ejecute la función `draw()`

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 9
line_highlights: 9
---
background(255, 255, 255) #Prueba diferentes números para cambiar el color

--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Depurar:** Es posible que encuentres algunos errores en tu proyecto que necesites corregir. A continuación, se muestran algunos errores comunes.

--- collapse ---

---
title: he cambiado el tamaño y el color, pero el resultado permanece igual
---

Después de cambiar el código, deberás `run` (ejecutar) tu proyecto para poder visualizar los cambios.

--- /collapse ---

--- collapse ---

---
title: Probé diferentes números, pero el color de fondo no cambia
---

La cantidad máxima de rojo, verde o azul es `255`. Asegurate de que todos los valores de `background` (color de fondo) estén entre `0` y `255`.

--- /collapse ---

--- /task ---


--- save ---
