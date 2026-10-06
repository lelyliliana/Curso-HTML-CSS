# Solución razonada: Unidades relativas

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad13-color/README.md)

## Razonamiento

Con raíz de 16 px, 2rem da 32 px. padding:1em en tarjeta da 32 px y padding:1rem da 16 px. Cambiar la preferencia raíz afecta ambas medidas, pero cada relación sigue siendo distinta. No deduzcas un tamaño absoluto sin conocer el contexto.

## Comportamiento de referencia

El título crece hasta su límite y el bloque de lectura no ocupa toda una pantalla grande. En pantalla pequeña cabe en el ancho disponible. El padding de la tarjeta corresponde a su propia fuente.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

100vw mide el viewport, no el espacio restante después de márgenes. Usa un ancho automático o 100% con modelo de caja apropiado y comprueba el elemento responsable.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad13-color/README.md)
