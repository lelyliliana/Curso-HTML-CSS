# Unidad 04 — Imágenes y contenido multimedia

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


---

## Continuar el curso

- **Unidad anterior:** [Unidad 03 — Enlaces y navegación](../unidad03-enlaces/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 05 — HTML semántico](../unidad05-semantica/README.md)
