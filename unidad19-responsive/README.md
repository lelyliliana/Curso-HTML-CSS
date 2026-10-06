# Unidad 19: Diseño responsive y mobile-first

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Construir interfaces que se adapten al espacio y al contenido antes de añadir breakpoints.

# 1. Responsive no significa tres versiones

No diseñamos obligatoriamente:
```text
móvil / tablet / escritorio
```

Diseñamos un sistema que funciona a través de un continuo de tamaños.

# 2. Mobile-first

Empieza con reglas que funcionen en espacio estrecho y añade cambios cuando haya espacio suficiente.

No significa diseñar solo para teléfono.

# 3. Primero lo fluido

Antes de media queries prueba:

- max-width;
- min()/max()/clamp();
- Flex wrap;
- Grid auto-fit/minmax;
- imágenes fluidas;
- tamaños intrínsecos.

Muchos componentes pueden adaptarse sin breakpoint.

# 4. Contenedor

```css
.container {
  width: min(100% - 2rem, 70rem);
  margin-inline: auto;
}
```

Crea margen flexible y ancho máximo.

# 5. Contenido que decide

Una tarjeta necesita cambio cuando su contenido ya no cabe cómodamente, no porque el dispositivo se llame “tablet”.

Redimensiona lentamente y observa el punto de tensión.

# 6. Reflow

A zoom alto o viewport estrecho, el contenido debería reacomodarse sin exigir scroll horizontal general para lectura ordinaria.

Excepciones como tablas/código ancho pueden necesitar scroll localizado.

# 7. Orden

Responsive no debe depender de reordenar visualmente elementos de manera que DOM/teclado tengan otra secuencia lógica.

# 8. Touch

No dependas de hover para revelar información imprescindible.

Los controles deben tener áreas de interacción razonables y separación suficiente.

# 9. Práctica guiada

Construye landing sin media queries usando:

- container;
- Grid auto-fit;
- Flex wrap;
- clamp.

Solo después identifica qué parte realmente necesita cambiar de composición.

# 10. Errores frecuentes

- breakpoints por modelo de teléfono;
- ancho fijo;
- ocultar contenido para que “quepa”;
- hover como única interacción;
- reordenar visualmente contra DOM.

# 11. Reto
Página funcional desde 320px hasta pantalla amplia con el menor número de breakpoints justificables.

# 12. Autoevaluación

1. ¿Responsive = tres tamaños?
2. ¿Qué es mobile-first?
3. ¿Qué probar antes de media query?
4. ¿Quién debería determinar breakpoint?
5. ¿Hover basta en touch?

# 13. Checklist

- [ ] Diseño fluido.
- [ ] Contenido guía cambios.
- [ ] Pruebo continuo de tamaños.
- [ ] Mantengo orden lógico.

Continúa con media queries.



## Laboratorio completo: Diseño fluido

### Comprender antes de modificar

Responsive significa que contenido e interacción se mantienen útiles cuando cambian espacio y preferencias. No consiste en tres capturas fijas llamadas móvil, tableta y escritorio. Antes de añadir media queries, usa ancho máximo, wrapping, imágenes fluidas y alturas automáticas.

flex-basis expresa una base de distribución, no una obligación de ancho final. flex-grow permite aprovechar espacio y flex-shrink participar en reducción; los mínimos intrínsecos todavía importan. min-width:0 permite encoger la caja del hijo, mientras overflow-wrap ayuda a partir contenido largo. Ambas reglas tienen responsabilidades distintas. Prueba una ventana estrecha y otra amplia, pero también valores intermedios donde el contenido empieza a fallar. Un diseño que cabe visualmente puede seguir teniendo un menú imposible de usar con teclado.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Las dos tarjetas se distribuyen según el espacio y pueden ocupar líneas distintas. El contenedor deja de crecer al llegar a 64rem. No se impone altura fija a los párrafos.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main class="contenedor"><h1>Contenido que se adapta</h1><div class="columnas"><article><h2>Propósito</h2><p>Un sitio se lee en distintos tamaños y con distintas preferencias.</p></article><article><h2>Prueba</h2><p>Alarga el contenido, cambia el ancho y conserva todas las acciones.</p></article></div></main>
```

Las reglas específicas del tema son:

```css
.contenedor { width: min(100%, 64rem); margin-inline: auto; box-sizing: border-box; }
.columnas { display: flex; flex-wrap: wrap; gap: 1rem; }
.columnas article { flex: 1 1 18rem; min-width: 0; border: 2px solid #075985; padding: 1rem; box-sizing: border-box; overflow-wrap: anywhere; }

```

### Experimento y explicación

Introduce un título de 15 palabras y un párrafo tres veces más largo. Prueba 320, 768 y 1440 px, y arrastra lentamente entre esos tamaños. Registra el primer punto problemático si aparece.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Solo pruebas el ancho de tu monitor y declaras terminado el diseño.

**Cómo resolver:** Verifica extremos, tamaños intermedios, teclado y zoom. Usa contenido real y largo para que las restricciones aparezcan antes de publicar.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 18: Posicionamiento y capas](../unidad18-posicionamiento/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 20: Media queries y container queries](../unidad20-media-queries/README.md)
