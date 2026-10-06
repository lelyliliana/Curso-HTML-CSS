# Unidad 02: Texto, jerarquía y contenido

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Estructurar contenido por significado y crear una jerarquía que funcione incluso sin CSS.

# 1. Encabezados

h1–h6 expresan niveles de sección, no tamaños visuales.

No elijas h4 porque “se ve pequeño”. El tamaño se controla con CSS.

# 2. Jerarquía

```html
<h1>Curso de robótica</h1>
<h2>Materiales</h2>
<h3>Sensores</h3>
<h2>Proyectos</h2>
```

La estructura debería poder convertirse en un esquema lógico.

# 3. Párrafos

```html
<p>HTML describe la estructura del contenido.</p>
```

No uses varios br para simular párrafos o márgenes.

# 4. Énfasis

```html
<strong>Importante</strong>
<em>énfasis</em>
```

Tienen significado semántico. Si solo quieres apariencia, CSS puede ser más apropiado.

# 5. Listas

```html
<ul>
  <li>HTML</li>
  <li>CSS</li>
</ul>
```

Usa ol cuando el orden de los elementos sea significativo.

# 6. Citas

blockquote representa una cita extensa; no debe usarse simplemente para indentar visualmente.

# 7. Whitespace

HTML normalmente colapsa secuencias de espacios en texto.

No maquetes alineando con espacios.

# 8. Práctica guiada

Toma texto plano con título, secciones, pasos, advertencia y cita. Márcalo semánticamente sin CSS.

# 9. Errores frecuentes

- heading por tamaño;
- br para márgenes;
- lista hecha con guiones en párrafos;
- strong solo por negrita;
- blockquote para diseño.

# 10. Reto
Convierte una guía plana en HTML comprensible con CSS desactivado.

# 11. Autoevaluación

1. ¿h2 significa tamaño?
2. ¿Cuándo ol?
3. ¿strong/em son solo apariencia?
4. ¿Para qué blockquote?
5. ¿Cómo crear separación visual?

# 12. Checklist

- [ ] Jerarquía lógica.
- [ ] Listas correctas.
- [ ] Semántica antes de estilo.
- [ ] Contenido comprensible sin CSS.

Continúa con enlaces.



## Laboratorio completo: Texto y jerarquía

### Comprender antes de modificar

La jerarquía de encabezados representa relaciones entre contenidos. h2 introduce una sección dentro de la página y h3 una subsección de esa sección. Elegir h4 porque parece pequeño mezcla estructura con presentación. Más adelante CSS controlará el tamaño sin alterar el nivel.

Una lista ordenada comunica una secuencia; una lista no ordenada reúne elementos cuyo orden no es esencial. strong expresa importancia y em énfasis, aunque sus estilos predeterminados sean negrita y cursiva. No son herramientas para escoger cualquier apariencia. El HTML colapsa gran parte del espacio en blanco del código: diez espacios no constituyen un sistema de alineación. Tampoco uses muchos br para separar secciones. Cada párrafo debe ser un p y el espacio visual se controla con CSS cuando corresponda.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Preparación aparece como lista con viñetas; Procedimiento como lista numerada. Cómo comprobar pertenece a Procedimiento. Un inspector de accesibilidad debe reconocer una jerarquía h1, h2, h2, h3.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main>
  <h1>Guía de estudio</h1>
  <p>Practica <strong>cada día</strong> y pregunta cuando algo no tenga sentido.</p>
  <section><h2>Preparación</h2><ul><li>Abre tu carpeta.</li><li>Identifica el objetivo.</li></ul></section>
  <section><h2>Procedimiento</h2><ol><li>Lee el ejemplo.</li><li>Modifica una parte.</li><li>Comprueba el resultado.</li></ol>
  <h3>Cómo comprobar</h3><p>Explica el cambio con tus propias palabras. <em>No basta con copiar.</em></p></section>
</main>
```

### Experimento y explicación

Añade una sección Evaluación con dos criterios en lista no ordenada y una subsección Evidencia con un párrafo. Mantén la jerarquía. Cambia luego una lista a ol y explica si cambió el significado.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** El título de una sección se representa con un p en negrita.

**Cómo resolver:** Usa un encabezado del nivel correspondiente. strong dentro de p no incorpora esa sección a la estructura de encabezados que usan lectores y otras herramientas.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 01: Documento HTML](../unidad01-documento-html/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 03: Enlaces y navegación](../unidad03-enlaces/README.md)
