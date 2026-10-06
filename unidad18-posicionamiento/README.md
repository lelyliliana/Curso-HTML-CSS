# Unidad 18: Posicionamiento y capas

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Usar relative, absolute, fixed y sticky comprendiendo containing blocks y stacking contexts.

# 1. static

Es el posicionamiento normal por defecto para muchos elementos.

`top/right/bottom/left` no funcionan como con elementos posicionados.

# 2. relative

```css
.card {
  position: relative;
}
```

Permanece en el flujo y puede convertirse en referencia para descendientes absolute según reglas de containing block.

# 3. absolute

```css
.badge {
  position: absolute;
  inset-block-start: .5rem;
  inset-inline-end: .5rem;
}
```

Sale del flujo normal para posicionamiento y se ubica respecto a su containing block, no automáticamente respecto a “la pantalla”.

# 4. Patrón badge

```css
.card { position: relative; }
.badge { position: absolute; ... }
```

Aquí la relación visual pertenece al componente.

# 5. fixed

Se posiciona normalmente respecto al viewport, con excepciones/contextos creados por ciertas propiedades ancestras.

Útil para elementos persistentes, pero puede tapar contenido/controles.

# 6. sticky

```css
.header {
  position: sticky;
  top: 0;
}
```

Combina comportamiento de flujo y fijación dentro de su contenedor/scrolling context.

Puede “no funcionar” por overflow, tamaño o contexto del ancestro.

# 7. z-index

No es un ranking global.

Funciona dentro de **stacking contexts**.

Un hijo con z-index 999999 no puede necesariamente escapar del stacking context de su padre para superar otro contexto.

# 8. Stacking contexts

Pueden crearse por propiedades como:

- posicionamiento + z-index en ciertos casos;
- opacity <1;
- transform;
- isolation;
y otras.

DevTools ayuda a diagnosticar.

# 9. Modal

Un modal real requiere más que `position:fixed`:

- semántica;
- foco;
- cierre;
- bloqueo/gestión del fondo;
- teclado.

Aquí solo estudiamos layout/capas; no declares un modal accesible completo solo por dibujar una caja.

# 10. Práctica guiada

Construye:

- badge absolute;
- header sticky;
- botón fixed.

Después crea dos stacking contexts y comprueba por qué un z-index enorme no gana.

# 11. Errores frecuentes

- absolute para maquetar toda página;
- z-index cada vez mayor;
- sticky sin revisar overflow;
- fixed tapando contenido;
- modal visual sin interacción accesible.

# 12. Reto
Componente con badge y cabecera sticky, documentando containing block y stacking context.

# 13. Autoevaluación

1. ¿relative sale del flujo?
2. ¿Absolute respecto a qué?
3. ¿Sticky siempre respecto al viewport?
4. ¿z-index es global?
5. ¿Qué es stacking context?
6. ¿Una caja fixed ya es modal accesible?

# 14. Checklist

- [ ] Elijo position con propósito.
- [ ] Identifico containing block.
- [ ] Comprendo capas.
- [ ] Evito z-index arbitrario.

Continúa con responsive.



## Laboratorio completo: Posición dentro de una tarjeta

### Comprender antes de modificar

position:relative conserva la tarjeta en el flujo y puede establecer el bloque de referencia de un descendiente absoluto. El sello absoluto sale del flujo: no reserva espacio para sí. Por eso la tarjeta incluye padding superior suficiente para la etiqueta. Si el texto del sello crece, ese espacio debe volver a evaluarse.

No todos los elementos posicionados usan el viewport como referencia. absolute depende del bloque contenedor correspondiente; fixed suele referirse al viewport, aunque ciertas propiedades de ancestros pueden cambiarlo. sticky depende del contexto de scroll y de un umbral como top; necesita espacio para desplazarse dentro de sus límites. z-index interactúa con contextos de apilamiento: un número enorme no permite escapar de cualquier contexto. Primero entiende relación de contenedores, flujo y apilamiento antes de subir números.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Nuevo permanece en la esquina superior de la tarjeta. El párrafo posterior aparece debajo y no queda cubierto. El título tiene espacio reservado por el padding.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Una etiqueta contextual</h1><article class="tarjeta"><span class="sello">Nuevo</span><h2>Taller de lectura</h2><p>La etiqueta se posiciona respecto de esta tarjeta; el texto sigue en el flujo.</p></article><p>Este párrafo continúa después de la tarjeta.</p></main>
```

Las reglas específicas del tema son:

```css
.tarjeta { position: relative; border: 2px solid #075985; padding: 3.5rem 1rem 1rem; max-width: 32rem; }
.sello { position: absolute; inset-block-start: .75rem; inset-inline-end: .75rem; background: #075985; color: white; padding: .25rem .5rem; }

```

### Experimento y explicación

Retira position:relative de la tarjeta y observa a qué referencia se desplaza el sello. Restablécelo. Cambia el sello a texto largo y aumenta zoom; corrige cualquier solapamiento.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Posicionas absolutamente todos los párrafos para copiar una captura.

**Cómo resolver:** Regresa al flujo y utiliza Flex/Grid para relaciones de distribución. Las coordenadas de una captura no se adaptan a cambios de texto o fuente.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 17: CSS Grid](../unidad17-grid/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 19: Diseño responsive y mobile-first](../unidad19-responsive/README.md)
