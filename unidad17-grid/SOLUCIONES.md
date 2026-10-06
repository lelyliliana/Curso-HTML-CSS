# Solución razonada: Grid adaptable

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad18-posicionamiento/README.md)

## Razonamiento

auto-fill mantiene huecos de columnas; auto-fit colapsa los vacíos. min-width:0 y overflow-wrap permiten que el título se ajuste, mientras la definición fluida impide imponer un mínimo mayor que el contenedor.

## Comportamiento de referencia

Hay una, dos o tres columnas según el ancho disponible. Todas mantienen espacio entre tarjetas. Con una sola tarjeta en pantalla grande, auto-fit permite que ocupe el espacio disponible.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

El mínimo de 300 px es una restricción real. Reduce el mínimo para ese contexto o usa min(100%,300px) para permitir una sola columna estrecha.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad18-posicionamiento/README.md)
