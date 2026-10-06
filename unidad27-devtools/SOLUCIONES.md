# Solución razonada: Diagnóstico en DevTools

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad28-rendimiento/README.md)

## Razonamiento

Ruta: Network y URL solicitada. Clase: Elements/Styles y selector sin coincidencia. Regla posterior: Styles y declaración descartada. Cada fallo requiere una corrección distinta; repetir !important no arregla una ruta inexistente.

## Comportamiento de referencia

La nota tiene fondo claro. Puedes encontrar .tarjeta .nota en Styles, desactivar background y ver el cambio. Al recargar vuelve el estilo del archivo guardado.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

Tras confirmar la hipótesis, aplica la modificación en styles.css, guarda y recarga. Comprueba que el resultado persiste con una carga nueva.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad28-rendimiento/README.md)
