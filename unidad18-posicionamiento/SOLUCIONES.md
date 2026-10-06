# Solución razonada: Posición dentro de una tarjeta

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad19-responsive/README.md)

## Razonamiento

Sin el ancestro que establece referencia, el sello puede ubicarse respecto a otro bloque contenedor y salir de la tarjeta. Para contenido variable, mantener el sello en flujo es una alternativa más robusta que reservar una altura supuesta. La posición absoluta es útil solo cuando la relación lo justifica.

## Comportamiento de referencia

Nuevo permanece en la esquina superior de la tarjeta. El párrafo posterior aparece debajo y no queda cubierto. El título tiene espacio reservado por el padding.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

Regresa al flujo y utiliza Flex/Grid para relaciones de distribución. Las coordenadas de una captura no se adaptan a cambios de texto o fuente.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad19-responsive/README.md)
