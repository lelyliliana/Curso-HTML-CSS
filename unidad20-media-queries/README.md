# Unidad 20: Media queries y container queries

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Cambiar estilos según capacidades/espacio cuando el diseño realmente lo necesita.

# 1. Breakpoint por contenido

```css
@media (min-width: 48rem) {
  .layout {
    grid-template-columns: 2fr 1fr;
  }
}
```

48rem debe surgir del punto donde la composición puede sostener dos columnas, no de “tamaño tablet”.

# 2. min-width

Con mobile-first:

- estilos base para espacio estrecho;
- mejoras progresivas con min-width.

No es la única estrategia posible, pero mantiene una dirección mental sencilla.

# 3. Otras condiciones

Media queries pueden consultar:

- ancho/alto;
- orientación;
- preferencias;
- capacidades de interacción, entre otras.

No uses orientación como sustituto de medir espacio disponible.

# 4. Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* reduce movimiento no esencial */
}
```

No significa necesariamente eliminar toda transición instantáneamente; reduce/evita movimiento problemático según diseño.

# 5. Contraste/tema

Existen preferencias como `prefers-color-scheme` y otras capacidades con soporte variable.

Diseña fallback antes de depender de una feature.

# 6. Container queries

Un componente reutilizable puede necesitar responder a **su contenedor**, no al viewport.

```css
.card-list {
  container-type: inline-size;
}

@container (min-width: 30rem) {
  .card {
    grid-template-columns: 10rem 1fr;
  }
}
```

Esto desacopla el componente de dónde se ubica.

# 7. Media vs container

Media query:
> ¿cómo está el viewport/dispositivo/preferencia?

Container query:
> ¿cuánto espacio tiene este componente?

# 8. Feature queries

```css
@supports (display: grid) {
  ...
}
```

Permiten mejora progresiva cuando necesitas soportar entornos diversos.

# 9. Práctica guiada

Crea una card que aparece en sidebar estrecho y main ancho. Hazla adaptarse mediante container query sin saber el ancho del viewport.

# 10. Errores frecuentes

- breakpoints por dispositivo;
- docenas de media queries;
- viewport query para componente reutilizable;
- reduced-motion ignorado;
- depender de feature sin fallback cuando el soporte objetivo lo exige.

# 11. Reto
Layout con un breakpoint de página y un componente que responda a su contenedor.

# 12. Autoevaluación

1. ¿Qué define breakpoint?
2. ¿Qué significa mobile-first?
3. ¿Media vs container query?
4. ¿Qué consulta prefers-reduced-motion?
5. ¿Para qué @supports?

# 13. Checklist

- [ ] Breakpoints justificados.
- [ ] Componentes independientes.
- [ ] Respeto preferencias.
- [ ] Diseño mejora progresivamente.

Continúa con imágenes responsive.



## Laboratorio completo: Media query por necesidad

### Comprender antes de modificar

La versión base utiliza una columna y no necesita detectar un dispositivo. La media query agrega dos columnas cuando hay espacio suficiente para estos textos. 42rem es una decisión de este contenido, no una norma para todas las tabletas. El punto de cambio debe elegirse viendo cuándo cada columna conserva lectura y espacio.

Una query no reemplaza las reglas anteriores: sus declaraciones entran en la cascada cuando la condición se cumple. Si otra regla posterior tiene prioridad, puede ocultar el cambio esperado. La anchura del viewport se expresa en píxeles CSS, no simplemente píxeles físicos de la pantalla. El zoom cambia la relación entre espacio físico y CSS y puede activar una distribución más estrecha. Los ajustes de movimiento y preferencias son otras condiciones posibles; no mezcles todas las decisiones en un único breakpoint.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Debajo del umbral hay una columna; por encima, dos. La separación y bordes existen en ambas distribuciones porque pertenecen a las reglas base.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Agenda adaptable</h1><div class="agenda"><article><h2>Mañana</h2><p>Lectura y conversación.</p></article><article><h2>Tarde</h2><p>Proyectos y experimentos.</p></article></div></main>
```

Las reglas específicas del tema son:

```css
.agenda { display: grid; gap: 1rem; }
.agenda article { padding: 1rem; border: 2px solid #075985; }
@media (min-width: 42rem) { .agenda { grid-template-columns: repeat(2, minmax(0, 1fr)); } }

```

### Experimento y explicación

Prueba justo debajo, en el umbral y justo encima de 42rem. Cambia el umbral a 50rem y compara. Aumenta los títulos hasta que dos columnas dejen de ser cómodas y decide si el cambio está justificado.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Añades una query que nunca se cumple porque copiaste max-width en vez de min-width.

**Cómo resolver:** Comprueba la condición en DevTools y la anchura actual. min-width activa a partir del mínimo; max-width hasta el máximo. Revisa también el orden de las reglas.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 19: Diseño responsive y mobile-first](../unidad19-responsive/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 21: Imágenes responsive](../unidad21-imagenes-responsive/README.md)
