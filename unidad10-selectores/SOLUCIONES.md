# Solución razonada: Selectores con alcance

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad11-box-model/README.md)

## Razonamiento

El div rompe la relación de hijo directo, así que .panel > p deja de coincidir. .panel p funciona porque el párrafo sigue siendo descendiente. Una clase .nota aplicada al párrafo permite seleccionar por función y resistir cambios de envoltura.

## Comportamiento de referencia

Solo el párrafo directamente dentro del panel tiene fondo azul claro. Taller está en negrita. El párrafo externo no recibe el fondo del panel.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

El espacio significa descendencia. Usa .recursos.especial para ambas clases en el mismo elemento o .recursos a.especial para enlaces especiales dentro de la lista.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad11-box-model/README.md)
