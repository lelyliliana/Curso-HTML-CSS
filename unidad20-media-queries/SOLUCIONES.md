# Solución razonada: Media query por necesidad

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad21-imagenes-responsive/README.md)

## Razonamiento

La query debe reflejar el contenido. En una fuente raíz habitual de 16 px, 42rem se aproxima a 672 px para esta condición, pero no debes basar la enseñanza en un dispositivo concreto. Conserva una columna como base y documenta por qué el espacio permite dos.

## Comportamiento de referencia

Debajo del umbral hay una columna; por encima, dos. La separación y bordes existen en ambas distribuciones porque pertenecen a las reglas base.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

Comprueba la condición en DevTools y la anchura actual. min-width activa a partir del mínimo; max-width hasta el máximo. Revisa también el orden de las reglas.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad21-imagenes-responsive/README.md)
