# Unidad 31: Taller integrador de interfaces

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Propósito

Construir interfaces sin que el enunciado diga “usa Flexbox”, “usa Grid” o “pon un breakpoint en 768px”.

Debes elegir la técnica y justificarla.

# Método

Para cada reto:

1. analiza contenido;
2. estructura HTML sin pensar primero en apariencia;
3. define estados/interacción;
4. diseña móvil/fluido;
5. elige layout;
6. añade breakpoints solo si hacen falta;
7. prueba teclado/zoom;
8. diagnostica con DevTools;
9. mide recursos;
10. documenta decisiones.

# Reto 1: Landing

Incluye:

- header/nav;
- hero;
- beneficios;
- CTA;
- footer.

Decide qué es section/article/div.

# Reto 2: Galería

Debe adaptarse sin breakpoint por cada número de columnas.

Elige Grid/Flex y justifica.

# Reto 3: Formulario

Incluye labels, grupos, estados inválidos, focus y responsive.

No hay backend; documenta qué validación seguiría siendo necesaria en servidor.

# Reto 4: Tabla

Datos realmente tabulares.

Debe conservar asociaciones de encabezado y tener estrategia para viewport estrecho.

# Reto 5: Dashboard

Combina layout de página y componentes.

Decide Grid vs Flex en cada nivel.

# Reto 6: Navegación adaptable

Debe funcionar con teclado y no depender solo de hover.

Sin JavaScript, diseña solo interacciones que HTML/CSS puedan sostener correctamente; no simules un menú complejo inaccesible.

# Reto 7: Biblioteca

Button, card, alert y field con tokens, variantes y estados.

Úsalos en dos contextos.

# Reto 8: Artículo

Optimiza:

- jerarquía;
- ancho de lectura;
- imágenes;
- metadatos;
- rendimiento.

# Evidencia por reto

Entrega:

- captura o URL;
- estructura;
- decisión de layout;
- prueba teclado;
- prueba zoom;
- DevTools;
- problema encontrado/corrección.

# Autoevaluación

1. ¿Puedo elegir Grid/Flex?
2. ¿Sé cuándo no necesito breakpoint?
3. ¿Puedo explicar alt?
4. ¿Puedo diagnosticar cascada?
5. ¿Puedo probar foco/zoom?
6. ¿Puedo justificar una optimización?

# Checklist

- [ ] Semántica.
- [ ] Responsive.
- [ ] Accesibilidad.
- [ ] Diagnóstico.
- [ ] Rendimiento.
- [ ] Justificación.

Continúa con proyecto final.



## Taller desarrollado: biblioteca del barrio

Completa el [registro de práctica y aceptación](PRACTICA.md) para comprobar las cinco etapas.

### Enunciado

Una biblioteca ficticia necesita un sitio para explicar tres actividades, mostrar su horario y permitir consultar información. La persona que visita debe llegar al taller elegido desde Inicio, leer materiales y reconocer que el contacto es una demostración. La información se conservará al cambiar ancho o ampliar texto.

Trabaja primero con un wireframe sencillo de Inicio, Talleres y Contacto. Dibuja el orden de lectura para un ancho estrecho y para uno amplio. No ocultes navegación en un menú que necesite JavaScript: mantén enlaces visibles que puedan envolver.

### Datos de trabajo

| Taller | Día | Hora | Duración |
|---|---|---|---|
| Lectura | Martes | 15:00 | 60 minutos |
| Robótica | Jueves | 16:00 | 90 minutos |
| Arte | Sábado | 10:00 | 60 minutos |

Todos los datos son ficticios. Usa los textos de [sitio-final](../ejemplos/sitio-final/README.md) como material de contenido y escribe tu propia estructura antes de consultar su implementación.

### Etapa 1: estructura sin CSS

Construye las tres páginas con header, nav, main y footer. Cada una necesita title y h1 propios. En Inicio escribe una propuesta breve y tres artículos con enlaces al taller correspondiente. En Talleres identifica cada actividad con un id y añade materiales, tabla con caption/encabezados y preguntas con details/summary. En Contacto incluye aviso de demostración, labels y un grupo de radio con legend.

**Aceptación:** puedes recorrer las páginas sin CSS y llegar al destino de cada tarjeta. Una imagen rota no sustituye texto alternativo y ninguna ruta depende de tu equipo.

### Etapa 2: sistema visual

Define tokens de color, espacio y radio. Implementa una tarjeta base y una destacada. Aplica tipografía del sistema y limita longitud de párrafos. La distribución de tarjetas debe soportar una cuarta actividad sin duplicar CSS.

**Aceptación:** las variantes cambian solo lo necesario; el contenido largo no se corta por una altura fija. Explica qué reglas pertenecen a colección y cuáles a tarjeta.

### Etapa 3: adaptación

Resuelve el diseño estrecho primero. Prueba el ancho disponible antes de añadir una media query para la portada. Si la tabla no cabe, conserva sus asociaciones y ofrece desplazamiento dentro de una región identificada, sin desbordar toda la página.

**Aceptación:** a 320 px CSS el contenido principal puede leerse sin scroll horizontal accidental. La tabla, si lo requiere, se desplaza en su propio contenedor; los enlaces de navegación permanecen disponibles.

### Etapa 4: interacción y límites

El formulario utilizará únicamente datos ficticios y GET hacia resultado.html para demostrar validación. La página de resultado debe aclarar que no procesa, almacena ni envía. La validación nativa rechaza ausencia, correo sin formato válido y mensaje corto en los casos definidos. No implementes un botón que prometa enviar cuando no hay servicio.

**Aceptación:** vacío no navega; datos válidos abren resultado y muestran parámetros en URL. El contenido de resultado también tiene sentido si se abre directamente.

### Etapa 5: auditoría

Comprueba foco, orden de Tab, salto a main, details, ampliación, contraste, recursos y metadatos. Anota condiciones y al menos tres problemas/correcciones reales. No inventes problemas si no aparecieron: realiza también los experimentos controlados de la Unidad 27.

**Aceptación:** cada observación explica situación, evidencia, cambio y comprobación posterior.

### Solución de referencia

Consulta [la explicación de la solución](SOLUCIONES.md) después de construir tu propuesta. El sitio completo está en [ejemplos/sitio-final](../ejemplos/sitio-final/README.md); su README explica ejecución, decisiones y pruebas manuales.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 30: Publicación de un sitio estático](../unidad30-publicacion/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 32: Proyecto final](../unidad32-proyecto-final/README.md)
