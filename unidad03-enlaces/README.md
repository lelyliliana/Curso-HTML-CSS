# Unidad 03 — Enlaces y navegación

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
