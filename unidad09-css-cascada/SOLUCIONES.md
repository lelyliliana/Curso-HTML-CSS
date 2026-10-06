# Solución razonada: Cascada observable

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad10-selectores/README.md)

## Razonamiento

Al mover .destacado al principio, gana la última .aviso porque tienen la misma especificidad. .aviso.destacado tiene dos selectores de clase, supera las reglas de una clase en el mismo contexto y gana aunque aparezca antes. Solo color cambia: fondo y padding conservan sus declaraciones.

## Comportamiento de referencia

El primer aviso es rojizo y el segundo verde, ambos con fondo claro. En Styles, la primera declaración color de .aviso está tachada. En Computed puedes consultar el color final.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

Inspecciona el elemento, comprueba coincidencias y orden, y elimina conflictos innecesarios. Una regla con !important añade otra prioridad y puede hacer más difícil diagnosticar la siguiente modificación.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad10-selectores/README.md)
