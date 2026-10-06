# Unidad 05: HTML semántico

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Elegir elementos por significado y construir regiones/secciones comprensibles para personas, navegadores y tecnologías de asistencia.

# 1. div no está mal

`div` es un contenedor genérico válido cuando no existe una semántica más específica.

El problema es usarlo para todo.

# 2. Regiones

```html
<header>...</header>
<nav>...</nav>
<main>...</main>
<footer>...</footer>
```

`main` representa el contenido principal del documento y normalmente debe existir una sola región main visible relevante por página.

# 3. section

Representa una sección temática.

Suele tener un encabezado que identifica su tema:

```html
<section>
  <h2>Proyectos</h2>
  ...
</section>
```

No uses section como reemplazo automático de div.

# 4. article

Contenido autocontenido que podría tener sentido por sí mismo/reutilizarse:

```html
<article>
  <h2>Cómo construir...</h2>
  ...
</article>
```

Una tarjeta visual no es automáticamente article.

# 5. aside

Contenido relacionado pero tangencial respecto al flujo principal.

No significa simplemente “columna derecha”.

# 6. header/footer

Pueden pertenecer a la página o a una sección/article según contexto.

No son exclusivos del body.

# 7. Semántica y CSS

Dos elementos pueden verse idénticos y significar cosas distintas.

HTML decide significado; CSS decide presentación.

# 8. Landmarks

Elementos como nav/main pueden crear regiones navegables para tecnologías de asistencia.

Si tienes dos nav, usa nombres accesibles distintos cuando sea necesario.

# 9. Práctica guiada

Toma:

```html
<div class="header">...</div>
<div class="menu">...</div>
<div class="contenido">...</div>
<div class="footer">...</div>
```

Reestructura solo donde la semántica sea clara.

# 10. Errores frecuentes

- section para cada contenedor;
- article para toda tarjeta;
- aside = sidebar visual;
- div considerado “prohibido”;
- elegir etiqueta por estilo.

# 11. Reto
Reestructura una landing completa y explica por qué cada región usa su elemento.

# 12. Autoevaluación

1. ¿div está mal?
2. ¿Qué es section?
3. ¿Qué es article?
4. ¿aside significa derecha?
5. ¿HTML/CSS tienen la misma responsabilidad?

# 13. Checklist

- [ ] Elijo por significado.
- [ ] Mantengo jerarquía.
- [ ] Uso regiones útiles.
- [ ] No fuerzo semántica.

Continúa con tablas.



## Laboratorio completo: Página semántica

### Comprender antes de modificar

Los elementos semánticos explican responsabilidades. header presenta una página o sección, nav reúne navegación relevante y main contiene el contenido principal. Un article tiene sentido como contenido relativamente independiente; una section agrupa un tema y normalmente se identifica mediante encabezado. Un div sigue siendo útil para agrupar elementos por presentación cuando no hay una relación semántica más precisa.

aside representa contenido complementario, no cualquier columna derecha. footer no implica que el navegador lo sitúe al pie de la pantalla. HTML comunica estructura y CSS distribuye la presentación. La semántica nativa aporta información a herramientas, pero no garantiza que todo el sitio sea accesible: también importan nombres, controles, foco y contenido. Mantén un solo main visible en estos documentos sencillos. Evita añadir role="main" a main sin necesidad.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

El inspector debe reconocer encabezado de página, navegación, contenido principal y pie. Sin CSS conserva un orden de lectura lógico. Los títulos describen el tema de cada región.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<header><p>Biblioteca del barrio</p><nav aria-label="Principal"><a href="#actividades">Actividades</a> · <a href="#contacto">Contacto</a></nav></header>
<main><h1>Leer en comunidad</h1><section id="actividades"><h2>Actividades</h2><article><h3>Encuentro de cuentos</h3><p>Lectura compartida y conversación.</p></article></section>
<aside><h2>Antes de asistir</h2><p>Trae agua y un cuaderno.</p></aside>
<section id="contacto"><h2>Contacto</h2><p>Consulta en la biblioteca durante el horario de atención.</p></section></main>
<footer><p>Biblioteca del barrio. Sitio de práctica.</p></footer>
```

### Experimento y explicación

Sustituye la actividad por un anuncio independiente de un taller. Añade fecha en un time con datetime válido. Explica por qué una envoltura usada solo para centrar contenido puede seguir siendo div.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Cambias todos los div por section y dejas secciones sin encabezados ni tema.

**Cómo resolver:** Revisa qué representa cada grupo. Conserva div para envolturas de presentación y usa section cuando exista un tema identificable.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 04: Imágenes y contenido multimedia](../unidad04-multimedia/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 06: Tablas de datos](../unidad06-tablas/README.md)
