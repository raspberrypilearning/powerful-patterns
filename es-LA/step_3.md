## Construye y prueba - Motivo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Most patterns have one design (called the **motif**) that repeats to create a pattern. 
</div>
<div>
![Un ejemplo de un motivo que usa varias formas para crearse.](images/motif.png){:width="300px"}
</div>
</div>

--- task ---

Draw shapes to create your motif. Use the tips at the bottom of the page if you need help.

--- /task ---

--- task ---

**Prueba:** Muéstrale tu proyecto a otra persona y pídele su opinión.

--- /task ---

### Formas e imágenes

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]


### Colores y efectos

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Posicionar y transformar

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

### Bugs

--- collapse ---
---
title: Las formas no están alineadas como yo esperaba
---

Si quieres que las formas estén alineadas, mira más de cerca tus puntos de coordenadas. Experimenta con los números hasta que tengas un diseño que te guste.

--- /collapse ---

--- collapse ---
---
title: No puedo ver algunas de las formas en mi motivo
---

El orden en que dibujas las cosas es muy importante.

Los gráficos por computadora están hechos de capas. En tu motivo, cada forma es una capa. Los objetos de las capas superiores se ubican delante de los objetos de las capas inferiores. Imagina cortar todas las formas en papel. Dependiendo de cómo organices y superpongas ese papel, el resultado final podría verse muy diferente.

--- /collapse ---

--- collapse ---
---
title: Mis círculos/cuadrados no son iguales
---

Los números tercero y cuarto en `ellipse` y `rect` son el ancho y el alto. Si los haces iguales, obtendrás un círculo o un cuadrado.

--- /collapse ---



