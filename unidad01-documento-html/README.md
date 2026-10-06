# Unidad 01: Documento HTML

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Construir un documento válido, comprender elementos/atributos/anidación y separar metadatos de contenido visible.

# 1. Estructura

```html
<!doctype html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport"
        content="width=device-width, initial-scale=1.0">
  <title>Mi sitio</title>
</head>
<body>
  <h1>Hola</h1>
</body>
</html>
```

# 2. Doctype

`<!doctype html>` indica al navegador que use el modo estándar HTML moderno.

No es una etiqueta de contenido.

# 3. html y lang

```html
<html lang="es">
```

Declara el idioma principal.

Ayuda a tecnologías de asistencia, pronunciación y procesamiento.

# 4. head vs body

**head:** metadatos/recursos del documento.  
**body:** contenido de la página.

`title` aparece normalmente en pestaña/marcadores/resultados, no como título visual del body.

# 5. charset

```html
<meta charset="UTF-8">
```

Decláralo temprano para interpretar caracteres correctamente.

# 6. viewport

```html
<meta name="viewport"
      content="width=device-width, initial-scale=1.0">
```

Permite que el viewport móvil corresponda al ancho del dispositivo, esencial para responsive moderno.

# 7. Elemento, etiqueta, atributo

```html
<a href="curso.html">Ver curso</a>
```

- elemento: conjunto completo;
- etiquetas: apertura/cierre;
- atributo: `href`;
- contenido: “Ver curso”.

# 8. Anidación

```html
<p>Aprende <strong>HTML</strong> desde cero.</p>
```

Cierra respetando estructura.

# 9. Elementos vacíos

```html
<img src="foto.jpg" alt="Descripción">
```

No todos tienen etiqueta de cierre.

# 10. Validación

El navegador intenta recuperarse de HTML incorrecto, lo que puede ocultar errores.

Usa inspector/validador cuando una estructura se comporte extraño.

# 11. Práctica guiada

Crea página con:

- title;
- h1;
- párrafo;
- idioma;
- UTF-8;
- viewport.

Inspecciona DOM.

# 12. Errores frecuentes

- title dentro de body;
- h1 como sustituto de title;
- lang ausente/incorrecto;
- anidación inválida;
- pensar que si navegador “lo muestra” el HTML está bien.

# 13. Reto
Documento completo válido y explica la función de cada línea del esqueleto.

# 14. Autoevaluación

1. ¿head/body?
2. ¿title/h1?
3. ¿para qué lang?
4. ¿viewport?
5. ¿Qué es atributo?
6. ¿Navegador corrige errores automáticamente de forma confiable?

# 15. Checklist

- [ ] Creo documento.
- [ ] Declaro idioma/charset/viewport.
- [ ] Anido correctamente.
- [ ] Distingo metadatos/contenido.

Continúa con texto.



## Laboratorio completo: Documento HTML completo

### Comprender antes de modificar

El documento tiene dos zonas principales. head describe el documento y relaciona recursos; body contiene el contenido que el navegador presenta. title identifica la pestaña y el historial. h1 encabeza el contenido de la página: no reemplaza title. El atributo lang="es" informa el idioma principal y ayuda a herramientas de lectura a pronunciarlo.

El doctype activa el modo estándar. meta charset indica UTF-8 y aparece al comienzo de head. La etiqueta viewport permite que un navegador móvil use el ancho del dispositivo como referencia del diseño. No vuelve responsive una página por sí sola: el contenido y CSS también deben adaptarse. La sangría facilita leer relaciones entre elementos, pero no sustituye las etiquetas de cierre. El navegador puede reparar HTML incorrecto; que algo se vea no demuestra que su estructura esté bien.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

La pestaña muestra Documento HTML completo y la página muestra Club de lectura. En Elements encontrarás html, head y body. El contenido se mantiene legible si desactivas styles.css.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main>
  <h1>Club de lectura</h1>
  <p>Nos reunimos para leer y conversar sobre tecnología.</p>
  <p>Próximo encuentro: miércoles, 4:00 p. m.</p>
</main>
```

### Experimento y explicación

Crea una página de un club distinto. Cambia title, h1 y los dos párrafos. Escribe una palabra con tilde. Explica por qué cambiar solo title no cambia el encabezado visible.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Escribes un segundo body para agregar otro párrafo.

**Cómo resolver:** Añade el párrafo dentro del body existente. Un documento tiene una estructura principal; no se crea un body por cada sección. Revisa el archivo fuente y no solo el DOM reparado.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 00: Cómo funciona la Web y preparar el entorno](../unidad00-web-entorno/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 02: Texto, jerarquía y contenido](../unidad02-texto/README.md)
