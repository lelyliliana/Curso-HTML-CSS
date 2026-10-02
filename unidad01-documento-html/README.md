# Unidad 01 — Documento HTML

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
