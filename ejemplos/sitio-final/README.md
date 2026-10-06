# Sitio final de referencia: biblioteca del barrio

[Índice del curso](../../README.md) · [Taller integrador](../../unidad31-taller/README.md) · [Proyecto final](../../unidad32-proyecto-final/README.md)

## Propósito y alcance

Sitio estático completo sobre una biblioteca ficticia. Se puede abrir localmente sin compilar ni instalar paquetes. No representa una organización real ni acepta inscripciones. El formulario demuestra etiquetas, grupos, validación nativa y navegación GET; no envía correo y no tiene backend.

## Abrir

Descarga o clona el curso y abre index.html de esta carpeta con el navegador. Para observar solicitudes HTTP utiliza [el servidor local de la guía](../../docs/ENTORNO.md). Puedes copiar la carpeta sitio-final entera a un proyecto independiente: todas sus dependencias están dentro.

| Archivo | Responsabilidad |
|---|---|
| index.html | Presentación y accesos a actividades |
| talleres.html | Actividades, tabla y preguntas frecuentes |
| contacto.html | Formulario de demostración con datos ficticios |
| resultado.html | Explicación del resultado sin prometer envío |
| 404.html | Contenido para una dirección inexistente al publicar |
| styles.css | Tokens, distribución, componentes y preferencias |
| img/aula.svg | Ilustración propia de distribución del aula |

## Decisiones

La barra utiliza Flexbox porque distribuye marca y enlaces sobre un eje y permite envolver. La colección usa Grid para coordinar tarjetas y aprovechar columnas disponibles. La portada cambia a dos columnas cuando tiene espacio suficiente para texto e imagen; no detecta modelos de teléfono.

El orden HTML coincide con lectura y teclado. La navegación indica la página actual con aria-current; el enlace de salto permite llegar al contenido. Cada página tiene h1, title y description propios. Los destinos internos existen y las imágenes tienen alternativa contextual y dimensiones. La tabla mantiene encabezados y ofrece un contenedor desplazable enfocable cuando sea necesario. Los formularios tienen etiquetas visibles, ayudas asociadas y legend para el grupo.

CSS tiene tokens y variantes sin !important. La única transición de color se activa bajo no-preference; no hay animaciones continuas ni interacción dependiente de hover. Las fuentes del sistema evitan descargas. La imagen principal no usa lazy porque aparece en la vista inicial.

## Qué comprobar

1. Abre Inicio, Talleres y Contacto; vuelve desde cada página.
2. Activa los tres enlaces de tarjetas y confirma su fragmento de destino.
3. Usa Tab, Shift+Tab y Enter para navegación, salto y preguntas desplegables.
4. En Contacto, prueba vacío, correo inválido, mensaje corto y datos ficticios válidos.
5. En el envío válido se abre resultado.html con parámetros: no hubo correo ni almacenamiento.
6. Revisa 320, 768 y 1440 px y tamaños intermedios. La tabla puede desplazarse dentro de su región; la página no debe tener desbordamiento accidental.
7. Amplía texto/zoom y verifica que no se recorte contenido ni foco.
8. Emula movimiento reducido y comprueba que no se aplica transición.
9. Desactiva CSS: el contenido debe mantener sentido.
10. Tras publicar, revisa páginas secundarias directamente, HTTPS y recursos en Network.

## Adaptar

Cambiar un nombre exige revisar contenido, title, description y textos de enlaces. Si añades una actividad, actualiza tarjeta, destino y horario. Un cuarto taller no exige duplicar reglas CSS. Para agregar envío real necesitarías un servicio, contrato, validación de servidor y manejo de estados; esa ampliación corresponde a otro curso.

[Continuar con el proyecto final](../../unidad32-proyecto-final/README.md)
