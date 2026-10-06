# Unidad 29: SEO técnico básico y metadatos

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Crear metadatos útiles para buscadores y compartir contenido sin convertir HTML en una lista de “trucos SEO”.

# 1. Contenido primero

SEO técnico no compensa una página sin contenido útil, clara estructura o accesibilidad.

Muchos fundamentos coinciden:

- title;
- headings;
- enlaces descriptivos;
- HTML semántico;
- rendimiento.

# 2. title

```html
<title>Curso de HTML y CSS | Aprende con Leli</title>
```

Debe describir la página y distinguirla de otras.

No llenes con palabras clave repetidas.

# 3. Meta description

```html
<meta
  name="description"
  content="Aprende HTML y CSS desde los fundamentos...">
```

Puede usarse como fragmento en resultados, pero el buscador puede elegir otro texto.

No es garantía de ranking ni de snippet exacto.

# 4. Headings

Son estructura de contenido, no “lugares donde meter keywords”.

# 5. Canonical

```html
<link rel="canonical"
      href="https://ejemplo.com/curso/">
```

Indica URL preferida entre variantes/duplicados.

No añadas canonical ficticio o incorrecto por checklist.

# 6. Robots

`robots.txt` y meta robots orientan rastreo/indexación bajo reglas de los crawlers.

No son mecanismos de seguridad. Una URL sensible no debe protegerse con robots.txt.

# 7. Open Graph

```html
<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="https://...">
```

Mejora la representación al compartir en plataformas compatibles.

No todas usan exactamente las mismas reglas.

# 8. URLs

URLs legibles/estables ayudan a personas y sistemas.

No cambies rutas publicadas sin redirecciones apropiadas cuando controlas servidor.

# 9. Datos estructurados

Schema.org/JSON-LD puede describir ciertos tipos de contenido.

No añadas marcado que no corresponda a contenido visible/real.

Este curso solo introduce el concepto.

# 10. Sitemap

Puede ayudar a descubrir URLs en sitios grandes.

No es necesario fabricar uno manual para una landing de una página solo por “SEO”.

# 11. Práctica guiada

Crea head para:

- inicio;
- curso;
- artículo.

Cada uno con title/description/OG distintos y canonical solo si conoces URL pública correcta.

# 12. Errores frecuentes

- keyword stuffing;
- misma title en todas;
- description como ranking garantizado;
- robots como seguridad;
- canonical copiado sin revisar;
- structured data ficticio.

# 13. Reto
Metadatos completos para un sitio real/ficticio explicando el propósito de cada elemento.

# 14. Autoevaluación

1. ¿Description garantiza snippet?
2. ¿Headings son truco SEO?
3. ¿Canonical para qué?
4. ¿robots.txt protege secretos?
5. ¿OG para qué?
6. ¿Structured data puede inventar contenido?

# 15. Checklist

- [ ] Titles únicos.
- [ ] Descriptions útiles.
- [ ] Canonical correcto cuando aplica.
- [ ] Social metadata coherente.

Continúa con publicación.



## Laboratorio completo: Metadatos por página

### Comprender antes de modificar

title debe identificar la página y distinguirla de otras del mismo sitio. La meta description resume el contenido, aunque un buscador puede elegir otro fragmento y no está obligado a mostrarla. Los encabezados y enlaces descriptivos ayudan a comprender la página; repetir palabras clave artificialmente no garantiza posicionamiento.

Open Graph aporta metadatos para ciertas vistas de enlaces compartidos. Una imagen social debe existir y su URL pública debe ser correcta. canonical expresa una URL preferida para contenido equivalente; no se copia de otro sitio y no garantiza por sí solo cómo un buscador indexa. En el ejemplo no se inventa canonical porque todavía no existe una dirección pública definitiva. Cada página del proyecto final tendrá title y description propios. SEO técnico no sustituye contenido útil, accesibilidad ni una buena navegación.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

La pestaña identifica el taller. Ver código fuente muestra una description específica. No existe una canonical ficticia ni una og:image con ruta inexistente.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Taller de lectura del barrio</h1><p>Un encuentro para conversar sobre relatos cortos.</p><h2>Qué encontrarás</h2><p>Lectura compartida, preguntas y recomendaciones.</p></main>
```

### Experimento y explicación

Escribe title y description para una página distinta de robótica. Haz que describan su contenido real. Explica cuándo podrías añadir canonical después de publicar y por qué no usarías localhost.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Todas las páginas se titulan Inicio y tienen una descripción copiada.

**Cómo resolver:** Asigna metadatos específicos. El título debe permitir distinguir la página en pestañas e historial y la descripción debe corresponder al contenido.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 28: Rendimiento web básico](../unidad28-rendimiento/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 30: Publicación de un sitio estático](../unidad30-publicacion/README.md)
