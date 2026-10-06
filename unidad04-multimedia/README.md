# Unidad 04: Imágenes y contenido multimedia

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Incluir imágenes con propósito, escribir alt según contexto y reducir problemas de layout/carga.

# 1. Imagen

```html
<img
  src="img/proyecto.jpg"
  alt="Prototipo de robot sobre una mesa"
  width="1200"
  height="800">
```

# 2. alt depende del contexto

Pregunta:
> ¿qué información perdería alguien si no percibe esta imagen?

Una imagen informativa puede necesitar descripción.

Una puramente decorativa puede usar:

```html
alt=""
```

# 3. Función, no nombre de archivo

Evita alt como:
```text
imagen.jpg
foto
imagen de...
```

Describe información o función relevante.

# 4. Imagen como enlace

Si es el único contenido del enlace, el alt debe comunicar función/destino.

# 5. figure

```html
<figure>
  <img src="img/prototipo.jpg" alt="...">
  <figcaption>Prototipo final.</figcaption>
</figure>
```

Úsalo cuando contenido visual y caption formen una unidad.

# 6. Dimensiones

width/height ayudan al navegador a reservar proporción/espacio y reducir layout shift.

CSS fluido:

```css
img {
  max-width: 100%;
  height: auto;
}
```

# 7. Formatos

JPEG, PNG, WebP, AVIF y SVG tienen propiedades distintas.

Elige según contenido, compatibilidad, transparencia y tamaño; no por moda.

# 8. Lazy loading

```html
<img loading="lazy" ...>
```

Puede servir fuera del viewport.

No lo apliques automáticamente a la imagen principal crítica sin medir.

# 9. Audio/video

Incluye controles y alternativas apropiadas. El contenido hablado/informativo puede requerir subtítulos o transcripción.

# 10. Práctica guiada

Crea galería con:

- informativa;
- decorativa;
- imagen-enlace;
- figure/caption.

Justifica cada alt.

# 11. Errores frecuentes

- alt = archivo;
- mismo alt para todo;
- decorativa descrita innecesariamente;
- imagen enorme reducida solo con CSS;
- lazy en recurso crítico por reflejo.

# 12. Reto
Galería accesible y optimizada con justificación de alt/formato.

# 13. Autoevaluación

1. ¿Alt describe siempre apariencia?
2. ¿Decorativa?
3. ¿Imagen enlace?
4. ¿Por qué width/height?
5. ¿Lazy siempre?

# 14. Checklist

- [ ] Alt contextual.
- [ ] Dimensiones.
- [ ] Formato apropiado.
- [ ] Multimedia accesible.

Continúa con semántica.



## Laboratorio completo: Imágenes con propósito

### Comprender antes de modificar

El texto alternativo comunica la información de una imagen cuando no puede verse o cuando se usa una herramienta de lectura. Depende del contexto. Aquí importa la distribución de mesas y pasillo, no que se trate de un archivo SVG. Si la misma imagen solo decorara un fondo sin aportar información adicional, un alt vacío podría ser correcto. Omitir alt no equivale a marcarla decorativa.

width y height proporcionan una proporción intrínseca que ayuda a reservar espacio antes de cargar. CSS puede reducir la imagen con max-width y conservar la proporción con height:auto. figcaption es una descripción visible para todas las personas; no sustituye automáticamente alt. Para audio y vídeo se requieren además alternativas adecuadas al contenido (transcripción, subtítulos y, cuando corresponda, audiodescripción). Tener controls hace disponible un reproductor, pero no aporta por sí solo esas alternativas.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

El aula conserva proporción al estrechar la ventana. Al bloquear la imagen, su alternativa sigue expresando la distribución relevante. El pie visible explica el uso del esquema.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main>
  <h1>Distribución del aula</h1>
  <figure><img src="../../recursos/img/aula.svg" alt="Tres mesas alrededor de una pizarra, con un pasillo central libre" width="800" height="450"><figcaption>Esquema de distribución para un taller de lectura.</figcaption></figure>
  <p>El pasillo permite llegar a las mesas sin mover las sillas.</p>
</main>
```

Las reglas específicas del tema son:

```css
figure { margin: 0; max-width: 50rem; }
```

### Experimento y explicación

Escribe dos alternativas para la imagen: una en una página sobre distribución y otra si se usa como decoración junto a un texto que ya describe exactamente las mesas. Justifica la diferencia. No agregues una ruta a un vídeo inexistente.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** La imagen se estira al fijar simultáneamente ancho y alto CSS sin respetar la proporción.

**Cómo resolver:** Mantén height:auto al cambiar el ancho. Si el diseño requiere un recorte, define un contenedor y object-fit con una decisión consciente sobre qué parte de la imagen puede perderse.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 03: Enlaces y navegación](../unidad03-enlaces/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 05: HTML semántico](../unidad05-semantica/README.md)
