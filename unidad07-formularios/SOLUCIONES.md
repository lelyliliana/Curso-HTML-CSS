# Solución razonada: Formulario de práctica

[Volver a la práctica](PRACTICA.md) · [Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad08-accesibilidad/README.md)

## Razonamiento

required controla ausencia y minlength la longitud en entrada del usuario. type=email comprueba formato. Sin name el correo puede seguir validándose, pero no se incorpora a los datos enviados. id no lo sustituye. Restablece name="correo" después del experimento.

## Comportamiento de referencia

Enviar vacío activa validación. Un correo como persona no cumple el tipo email. Con nombre Ana, correo ana@example.com y un taller, se abre resultado.html con parámetros de consulta. Esa página advierte que no hubo inscripción real.

Los archivos de [ejemplo](ejemplo/index.html) constituyen una versión completa de referencia. Tu modificación puede usar otros textos y decisiones visuales si conserva el contrato de la actividad. No es necesario copiar exactamente los colores o el contenido para demostrar comprensión.

## Diagnóstico

Añade label visible y describe el alcance real. El placeholder desaparece al escribir y no debe ser la única instrucción. Una página estática de resultado no prueba entrega de mensajes.

## Qué revisar en tu explicación

Identifica el elemento o regla que intervino, las condiciones de la prueba y el resultado. Si solo escribiste funcionó, completa la explicación: otra persona debe poder repetir el experimento sin adivinar qué cambiaste.

[Lección](README.md) · [Índice del curso](../README.md) · [Siguiente unidad](../unidad08-accesibilidad/README.md)
