# Unidad 03: Enlaces y navegación

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Construir navegación entre páginas, entender rutas/fragmentos y escribir enlaces comprensibles.

# 1. Relativo

```html
<a href="contacto.html">Contacto</a>
```

Se resuelve respecto a la URL/documento actual.

# 2. Subir carpeta

Desde una página dentro de `paginas/` hacia `index.html`:

```html
<a href="../index.html">Inicio</a>
```

Dibuja el árbol de carpetas si te confundes.

# 3. Absoluto

```html
<a href="https://example.org/">Referencia externa</a>
```

# 4. Fragmento

```html
<a href="#proyectos">Proyectos</a>
<section id="proyectos">...</section>
```

El id debe ser único en el documento.

# 5. Texto significativo

Evita “clic aquí” cuando el destino puede describirse.

```html
<a href="programa.html">Consulta el programa del curso</a>
```

# 6. Nueva pestaña

target="_blank" cambia comportamiento y puede sorprender.

Úsalo con una razón; no fuerces todas las externas a abrir otra pestaña.

# 7. nav

```html
<nav aria-label="Principal">
  ...
</nav>
```

Si hay varias navegaciones, un nombre accesible ayuda a distinguirlas.

# 8. Página actual

```html
<a href="cursos.html" aria-current="page">Cursos</a>
```

Comunica el estado además del estilo visual.

# 9. Práctica guiada

Crea index.html, cursos.html y contacto.html. Añade navegación coherente y un fragmento interno. Prueba cada enlace desde cada página.

# 10. Errores frecuentes

- ruta calculada desde carpeta equivocada;
- “clic aquí”;
- id duplicado;
- target blank para todo;
- navegación inconsistente.

# 11. Reto
Sitio de tres páginas con navegación, estado actual y enlaces internos.

# 12. Autoevaluación

1. ¿Ruta relativa respecto a qué?
2. ¿Qué hace ../?
3. ¿Qué es fragmento?
4. ¿Por qué texto descriptivo?
5. ¿Para qué aria-current?

# 13. Checklist

- [ ] Rutas correctas.
- [ ] Fragmentos.
- [ ] Texto significativo.
- [ ] Navegación coherente.

Continúa con multimedia.



## Laboratorio completo: Enlaces y fragmentos

### Comprender antes de modificar

Un enlace lleva a un destino. Su texto debe explicar adónde lleva sin exigir leer el párrafo entero. Leer los materiales del encuentro comunica más que clic aquí. El navegador aporta interacción con teclado, menú contextual y posibilidad de abrir otra pestaña; no es necesario imitarla con un elemento genérico.

Un fragmento como #horario busca un id dentro del documento. Cada id debe ser único. Un archivo relativo como detalle.html se busca en la carpeta del documento actual. Una URL que comienza con / se resuelve desde la raíz del sitio, que puede ser distinta de la raíz de un repositorio publicado en GitHub Pages. Para enlaces externos que decidas abrir aparte, indica el comportamiento y usa rel apropiado. Abrir todas las rutas en nuevas pestañas hace más difícil seguir el recorrido.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Horario cambia el fragmento de la URL y lleva a esa sección. Materiales abre detalle.html. Su enlace de regreso permite volver. Tab recorre los enlaces y Enter activa el enfocado.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<header><h1>Agenda del club</h1><nav aria-label="Secciones"><a href="#horario">Horario</a> · <a href="#recursos">Recursos</a></nav></header>
<main>
  <section id="horario"><h2>Horario</h2><p>Viernes a las 3:00 p. m.</p></section>
  <section id="recursos"><h2>Recursos</h2><p><a href="detalle.html">Leer los materiales del encuentro</a></p>
  <p><a href="https://developer.mozilla.org/es/docs/Web/HTML" target="_blank" rel="noopener noreferrer">Documentación de HTML (abre otra pestaña)</a></p></section>
</main>
```

Las reglas específicas del tema son:

```css
section { margin-block: 2rem; }
```

### Experimento y explicación

Añade una sección Preguntas con id="preguntas" y su enlace en el nav. En detalle.html añade un enlace a index.html#recursos. Verifica los dos recorridos con teclado.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** El enlace usa href="#Horario", pero la sección tiene id="horario".

**Cómo resolver:** Haz coincidir ambos valores, respetando mayúsculas. Comprueba también que no haya dos secciones con el mismo identificador.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 02: Texto, jerarquía y contenido](../unidad02-texto/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 04: Imágenes y contenido multimedia](../unidad04-multimedia/README.md)
