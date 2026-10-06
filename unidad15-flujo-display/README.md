# Unidad 15: Flujo normal y display

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Comprender dónde coloca el navegador los elementos antes de utilizar Flexbox, Grid o position.

# 1. Flujo normal

Sin layout especial, los elementos participan en el flujo del documento.

Los bloques se organizan en la dirección de bloque y el contenido inline fluye en líneas.

Comprenderlo evita usar position para todo.

# 2. block

Un bloque normalmente comienza una nueva línea y utiliza el espacio disponible según su contexto.

# 3. inline

Participa dentro de una línea de texto.

```html
<p>Aprende <strong>HTML</strong> hoy.</p>
```

Width/height no se comportan igual que en un bloque.

# 4. inline-block

Fluye en línea pero genera una caja que admite dimensiones de forma similar a un bloque.

Flex/Grid resuelven hoy muchos layouts que antes usaban inline-block.

# 5. display:none

Retira el elemento del layout y normalmente también de la accesibilidad expuesta.

No lo uses para contenido que debe seguir disponible a tecnologías de asistencia.

# 6. visibility:hidden

Oculta visualmente conservando espacio.

No es equivalente a display:none.

# 7. Visualmente oculto

Para contenido destinado a lectores de pantalla existen patrones específicos de “visually hidden”; no uses display:none.

# 8. Flujo y márgenes

En flujo normal pueden ocurrir colapsos de márgenes verticales.

Flex/Grid crean contextos con reglas distintas.

# 9. Práctica guiada

Crea bloques y spans. Cambia solo display y observa salto de línea, dimensiones y espacio.

# 10. Errores frecuentes

- absolute para layout normal;
- display:none para label accesible;
- width en inline esperando bloque;
- aprender Flex sin entender flujo.

# 11. Reto
Página simple solo con flujo normal y explicación de la posición de cada elemento.

# 12. Autoevaluación

1. ¿Qué es flujo normal?
2. ¿Block/inline?
3. ¿display:none conserva espacio?
4. ¿Cómo ocultar solo visualmente?
5. ¿Por qué flujo antes de Flex?

# 13. Checklist

- [ ] Comprendo flujo.
- [ ] Distingo display.
- [ ] Oculto correctamente.
- [ ] Evito position innecesario.

Continúa con Flexbox.



## Laboratorio completo: Flujo y display

### Comprender antes de modificar

El flujo normal organiza contenido según su tipo de caja y el espacio disponible. Un elemento inline participa en líneas de texto; un bloque ocupa el ancho disponible en su contexto habitual y comienza una nueva línea. display puede alterar esas cajas sin cambiar el significado HTML: un span estilizado como bloque sigue siendo un elemento semánticamente genérico.

inline-block permite que una caja participe en una línea y tenga dimensiones de bloque. Los espacios del HTML entre cajas inline pueden producir separación visible. display:none retira la caja y normalmente su exposición al árbol de accesibilidad. visibility:hidden conserva espacio, aunque oculta el contenido y generalmente lo excluye de accesibilidad. opacity:0 conserva la caja y puede dejar interacción/foco activos: no es intercambiable con ocultación funcional. Elige según qué experiencia debe tener la persona.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

La etiqueta acompaña al texto. El div tiene su propia línea. No hay un hueco reservado para el párrafo con display:none. La pieza muestra borde y padding.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Bloques y líneas</h1><p>Este párrafo contiene <span class="etiqueta">una etiqueta inline</span> y continúa en la misma línea cuando hay espacio.</p><div class="bloque">Un div ocupa una nueva línea en el flujo normal.</div><p>Este <span class="pieza">inline-block</span> admite dimensiones y sigue participando en una línea.</p><p class="oculto">Este párrafo está oculto con display:none.</p><p>Último párrafo visible.</p></main>
```

Las reglas específicas del tema son:

```css
.etiqueta { background: #e0f2fe; }
.bloque { background: #f0fdf4; padding: .5rem; }
.pieza { display: inline-block; padding: .5rem; border: 1px solid #075985; }
.oculto { display: none; }

```

### Experimento y explicación

Alterna la regla oculto entre display:none, visibility:hidden y opacity:0. Anota si conserva espacio. Si el elemento fuera un enlace, comprueba además si puede recibir foco.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Asignas width a un span inline y esperas que mida como una tarjeta.

**Cómo resolver:** Revisa su display. Si necesitas una caja dimensionada en la línea, usa inline-block; si necesitas una sección de contenido, revisa también si el HTML elegido expresa su función.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 14: Tipografía y legibilidad](../unidad14-tipografia/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 16: Flexbox](../unidad16-flexbox/README.md)
