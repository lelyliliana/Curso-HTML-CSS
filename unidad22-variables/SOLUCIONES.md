# Solución razonada: Variables para un sistema visual

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad23-pseudo/README.md)

## Razonamiento

La nueva clase redefine tokens en su alcance. El borde y el enlace cambian porque ambos usan var(--acento). El texto del párrafo conserva el color del body. Cambiar un token no implica reescribir todas las reglas ni usar !important.

## Comportamiento de referencia

La primera tarjeta y su enlace son azules; la segunda utiliza púrpura. Espacio y radio se mantienen iguales. En Computed puedes reconocer el valor heredado de --acento.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

El nombre de una propiedad personalizada comienza por --. Comprueba sintaxis y nombre exacto: var(--acento).

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad23-pseudo/README.md)
