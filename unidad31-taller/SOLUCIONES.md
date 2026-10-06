# Solución del taller integrador

[Volver al enunciado](README.md) · [Práctica](PRACTICA.md) · [Índice](../README.md) · [Siguiente: proyecto final](../unidad32-proyecto-final/README.md)

## Estructura

La [solución completa](../ejemplos/sitio-final/README.md) utiliza tres páginas principales, una página de resultado y una página 404. Los enlaces de tarjetas apuntan a talleres.html#lectura, #robotica y #arte. Esos id están en sus respectivos artículos. El nav usa enlaces relativos y aria-current solo en la página activa.

## Distribución

Flexbox organiza marca y nav con wrapping. Grid coordina tarjetas con auto-fit y mínimo limitado por el contenedor. La portada tiene una columna como base y dos al alcanzar espacio suficiente. No se alteran órdenes con order ni se posiciona el texto mediante coordenadas de captura.

## Accesibilidad

El salto apunta a main, que puede recibir foco sin entrar en el recorrido normal de Tab. La tabla conserva th y scope y su región desplazable es identificable y enfocable. Las preguntas usan details/summary nativos. Cada campo tiene label; radios comparten name y se agrupan con fieldset/legend. El foco visible se conserva.

## Validación

required impide ausencia en el envío normal. minlength se comprueba con entrada de usuario y type=email verifica formato. Los controles tienen name para incorporarse al envío. El resultado no confirma una inscripción: no hay procesamiento de servidor. No se consideran seguras estas comprobaciones para un sistema real; un servidor tendría que validar su propio contrato.

## Cuarto taller

Agrega un artículo con id="ciencia", una tarjeta enlazada a talleres.html#ciencia, una fila de horario y un radio con value="ciencia". Conserva encabezados correctos. Las mismas clases deben presentar la tarjeta sin nuevas reglas específicas por cada taller.

## Qué alternativas son válidas

Puedes elegir otra paleta o distribución si cumple las tareas, conserva contraste y acceso y se adapta al contenido. La solución de referencia no obliga a imitar una captura; sirve para comparar decisiones y comprobar contratos.

[Continuar con proyecto final](../unidad32-proyecto-final/README.md)
