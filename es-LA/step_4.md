## Expande y prueba: Patrón

¡Ha llegado el momento de hacer tu patrón completo!

![Ejemplos de proyectos terminados que tienen el motivo usado repetidamente para formar un patrón completo.](images/second.gif)

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;"><span style="color: #0faeb0">Abstracción</span> es la resolución de problemas mediante la reducción de detalles innecesarios. 

</p>

--- task ---

Mira este pastel de capas de Malasia (kek lapis Sarawak). ¿Cómo cambia el motivo para formar el patrón general?

![El motivo del proyecto kek lapis Sarawak junto al patrón completo.](images/kek-motif.png)

Mira este papel tapiz art déco. ¿Cómo cambia el motivo para formar el patrón general?

![El motivo del proyecto de papel tapiz art déco junto al patrón completo.](images/spirals-motif.png)

Piensa en el patrón que estás creando. How does your motif change to make the overall pattern? Usa estas preguntas para ayudarte a resumirlo:
- ¿La totalidad o parte del motivo gira?
- ¿En qué dirección gira? ¿Y cuánto?
- ¿Hay capas en el patrón que se superponen?
- ¿Cuántas veces se repite el motivo?
- ¿Cómo se organiza la repetición (es decir, cuántas filas/columnas)?
- ¿Cambian los colores?
- ¿Hay detalles que no están incluidos en el motivo (es decir, la guinda del pastel de capas de Malasia)?

--- /task ---

--- task ---

Ahora que sabes más acerca de cómo el motivo se convierte en el patrón completo, puedes programarlo usando tus respuestas a las preguntas anteriores.

**Sugerencia:** No olvide que puede 'Ver el interior' de cualquiera de los ejemplos en la introducción y 'copiar' y 'pegar' el código en su proyecto. ¡Los desarrolladores profesionales hacen esto todo el tiempo!

Has desarrollado algunas habilidades realmente útiles. Aquí hay un recordatorio para ayudarte a crear tu patrón repetido:

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

[[[generic-python-for-loop-repeat]]]

--- collapse ---

---
title: Posiciones aleatorias
---

Puedes agregar `from random import randint` en la parte superior de **main.py**, esto te permitirá usar la función `randint` para generar números aleatorios.

Para usar la función `randint`, deberás llamarla en tu código.

Una forma de usar random es mover tu motivo a una posición aleatoria cada vez que se dibuja:

--- code ---
---
language: python filename: main.py - draw()

---

    push_matrix() #Inicia la transformación 
    translate(randint(0, 400), randint(0, 400)) 
    dibujar_motivo() 
    pop_matrix() #Restablece la transformación

--- /code ---

También puedes usar random para cambiar los colores en tu motivo a medida que se vuelve a dibujar.

--- code ---
---
filename: main.py - draw()

---

    dibujar_motivo = color(randint(0, 50), randint(0, 100), randint(150, 255))

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Cambiar el tamaño de tu motivo
---

Si usas un motivo que ya has dibujado antes, podría no ser del tamaño correcto.

Puedes usar `scale()` antes de llamar a la función que dibuja tu motivo para cambiar su tamaño. Usar una entrada mayor que '1' hará que el motivo sea más grande, usar una entrada menor que '1' lo hará más pequeño.

--- code ---
---
filename: main.py - draw()

---

    scale(0.5) #Mitad del tamaño

--- /code ---

--- /collapse ---

--- /task ---

Ahora puedes animar tu patrón para mostrar cómo lo hiciste. A menudo, los patrones tienen un significado cultural poderoso en la forma en que se hacen o en el proceso.

--- task ---

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[generic-python-for-loop-repeat]]]

--- /task ---


--- task ---

**Prueba:** Muéstrale tu proyecto a otra persona y pídele su opinión. ¿Quieres hacerle algún cambio a tu patrón?

--- /task ---

--- task ---

**Depurar:** Es posible que encuentres algunos errores en tu proyecto que necesites corregir. A continuación, se muestran algunos errores comunes.

--- collapse ---

---
title: Mi motivo no parece girar
---

Asegurate de estar usando la función `radian()` para convertir grados a radianes.

--- /collapse ---

--- collapse ---
---
title: La rotación se ve extraña
---

¿Has comprobado que estás usando `translate()` desde y hacia las coordenadas correctas?

¿Tienes más de una cosa girando? Es posible que tengas que usar `push_matrix()` y `pop_matrix()` para que la pantalla gire en diferentes puntos a la vez.

--- /collapse ---

--- collapse ---
---
title: Mi patrón no se anima
---

Comprueba que has utilizado `frame_count()` correctamente en un bucle.

--- /collapse ---

--- collapse ---
---
title: Mi patrón no luce como yo quiero
---

Revisa las secciones anteriores `rotate()` y `translate()`. Experimenta con estas funciones hasta que luzca como quieres, y recuerda que, ¡los errores son poderosos!

--- /collapse ---

--- collapse ---
---
title: Me sale un error
---

Comprueba la sintaxis de tu código. ¿Falta algún paréntesis `(` o `)` o dos puntos `:` después de definir una función? ¿Algo está mal escrito? ¿Tu código está correctamente indentado (tiene sangría)?

--- /collapse ---

--- collapse ---
---
title: La animación es demasiado rápida/demasiado lenta
---

Cambia el `frame_rate()` al comienzo de tu programa para que alcance la velocidad que quieras.

--- /collapse ---

Es posible que encuentres un error que no se incluye aquí. ¿Puedes averiguar cómo solucionarlo?

Nos encanta conocer tus errores y cómo los solucionaste. Usa el botón Enviar comentarios en la parte inferior de esta página si encontraste un error diferente en tu proyecto.

--- /task ---


--- save ---
