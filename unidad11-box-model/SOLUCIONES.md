# Solución razonada: Medir el modelo de caja

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad12-unidades/README.md)

## Razonamiento

Con 10 y 2, content-box ocupa 224 px. border-box conserva 200 px y deja 176 px de contenido. Con width:100%, content-box puede superar el contenedor por padding/borde; border-box los incluye. Los márgenes exteriores siguen necesitando espacio.

## Comportamiento de referencia

La primera caja ocupa 250 px y la segunda 200 px. Inspecciona ambas: tienen el mismo padding y borde, pero distinta anchura de contenido.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

Revisa la caja que supera su contenedor y corrige box-sizing o el tamaño. Ocultar desbordamiento global puede recortar contenido y controles sin resolver la causa.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad12-unidades/README.md)
