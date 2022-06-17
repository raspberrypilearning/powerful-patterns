## Construye y prueba: Motivo

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ha llegado el momento de crear tu motivo, el primer elemento de tu patrón.
</div>
<div>

![Un ejemplo de un motivo que usa varias formas para crearse.](images/motif.png){:width="300px"}

</div>
</div>

El proceso de creación de tu motivo refleja lo que suelen hacer los científicos de la computación cuando crean un programa o una solución a un problema. Este proceso se llama **descomponer en partes** y la usarás para crear tu motivo.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">Descomponer en partes</span> es dividir algo en partes más pequeñas y más fáciles de entender. Esto significa que puedes crear un patrón una parte a la vez hasta que lo hayas completado.</p>

Mira el patrón que quieres recrear. ¿Cómo puedes descomponerlo en un solo elemento (el motivo) que se repite?

En este ejemplo, un patrón de papel tapiz art déco se ha descompuesto en una colección básica de formas (cinco círculos superpuestos) que forman el motivo:

![Un solo motivo de cinco círculos junto a una imagen del patrón completo art déco con muchas copias del motivo.](images/motif-pattern.png)

**Sugerencia:** Recuerda probar tu proyecto cada vez que agregues algo. Es mucho más fácil encontrar y corregir errores antes de hacer más cambios.

--- task ---

Has desarrollado algunas habilidades realmente útiles. Aquí hay un recordatorio para ayudarte a crear tu motivo:

### Formas e imágenes

[[[processing-python-ellipse]]]

[[[processing-python-rect]]]

[[[processing-python-triangle]]]

[[[processing-add-image]]]

### Colores y efectos

[[[generic-theory-simple-colours]]]

[[[processing-opacity]]]

[[[processing-stroke]]]

[[[processing-tint]]]

### Posicionar y transformar

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---

--- task ---

**Prueba:** Muéstrale tu proyecto a otra persona y pídele su opinión. ¿Quieres hacerle algún cambio a tu motivo?

--- /task ---

--- task ---

**Depurar:** Es posible que encuentres algunos errores en tu proyecto que necesites corregir. A continuación, se muestran algunos errores comunes.

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

Es posible que encuentres un error que no se incluye aquí. ¿Puedes averiguar cómo solucionarlo?

Nos encanta conocer tus errores y cómo los solucionaste. Usa el botón Enviar comentarios en la parte inferior de esta página si encontraste un error diferente en tu proyecto.

--- /task ---

--- save ---
