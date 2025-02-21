## Expande y prueba - Patrón

Now that you have a **motif**, you can repeat it to make a pattern

![Ejemplos de proyectos terminados que tienen el motivo usado repetidamente para formar un patrón completo.](images/second.gif)


--- task ---

Move, resize and repeat the motif you have created to make a repeating pattern. Use the tips at the bottom of the page if you need help.

--- /task ---


--- task ---

**Prueba:** Muéstrale tu proyecto a otra persona y pídele su opinión. ¿Quieres hacerle algún cambio a tu patrón?

--- /task ---




### Moving, rotating and resizing

[[[processing-matrix]]]

[[[processing-translation]]]

[[[processing-rotation]]]

[[[python-operators]]]

--- collapse ---

---
title: Cambiar el tamaño de tu motivo
---

Si usas un motivo que ya has dibujado antes, podría no ser del tamaño correcto.

Puedes usar `scale()` antes de llamar a la función que dibuja tu motivo para cambiar su tamaño. Usar una entrada mayor que '1' hará que el motivo sea más grande, usar una entrada menor que '1' lo hará más pequeño.

--- code ---
---
language: python
filename: main.py - draw()
---

    scale(0.5) #Mitad del tamaño

--- /code ---

--- /collapse ---

### Repeating

[[[generic-python-for-loop-repeat]]]

### Randomness

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

### Bugs

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

