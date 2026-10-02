# Unidad 05 — HTML semántico

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
