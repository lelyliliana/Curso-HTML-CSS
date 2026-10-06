# Solución razonada: Selección de imágenes

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad22-variables/README.md)

## Razonamiento

La media de source decide la composición. El ancho visible depende del contenedor y CSS. No se inventan variantes de archivos ni se etiqueta una imagen de 800 px como 400w: el descriptor debe coincidir con el recurso real.

## Comportamiento de referencia

A 320 px se ve composición cuadrada; en pantalla amplia, horizontal. En DevTools puedes consultar currentSrc del img para reconocer el recurso elegido. No hay una imagen rota como fallback.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

Evalúa si es candidata a LCP. La imagen principal visible suele necesitar carga temprana; reserva lazy para imágenes fuera de la vista inicial cuando corresponda.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad22-variables/README.md)
