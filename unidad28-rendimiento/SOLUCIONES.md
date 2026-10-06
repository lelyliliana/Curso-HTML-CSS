# Solución razonada: Carga y tamaño de recursos

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad29-seo/README.md)

## Razonamiento

La optimización debe modificar un recurso real y conservar información. Documenta antes/después con condiciones iguales. Si no dispones de fotografía, compara tamaños de los SVG del curso y explica por qué eso no representa el ahorro de comprimir una foto.

## Comportamiento de referencia

Bajo HTTP se cargan HTML, CSS y una imagen local. No se descargan fuentes externas ni JavaScript. La imagen reserva proporción antes de completar la carga.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

Repite con condiciones equivalentes. Network indica si el recurso viene de memoria/disco. Cambia una variable relevante por vez para que la comparación tenga sentido.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad29-seo/README.md)
