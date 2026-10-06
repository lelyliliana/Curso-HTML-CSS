# Solución razonada: Tipografía legible

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad15-flujo-display/README.md)

## Razonamiento

El multiplicador escala con cada tamaño. La columna necesita limitar ancho, no altura. Si una palabra o URL larga desborda, aplica overflow-wrap al contenido que lo requiere; no reduzcas toda la fuente para ocultar el problema.

## Comportamiento de referencia

La columna mantiene una longitud razonable en una pantalla amplia. La entrada es mayor que los párrafos. Al aumentar zoom, el contenido se reacomoda sin una altura fija que lo recorte.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

Usa altura automática y, si hace falta un mínimo visual, min-height. Prueba contenido variable antes de decidir límites.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad15-flujo-display/README.md)
