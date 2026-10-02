# Unidad 21 — Imágenes responsive

## Qué aprenderás
Servir imágenes adecuadas al espacio/densidad y distinguir resolución adaptable de dirección artística.

# 1. CSS básico

```css
img {
  max-width: 100%;
  height: auto;
}
```

Evita que la imagen exceda su contenedor manteniendo proporción.

Esto no evita descargar un archivo enorme.

# 2. srcset por resolución/ancho

```html
<img
  src="img/foto-800.jpg"
  srcset="
    img/foto-480.jpg 480w,
    img/foto-800.jpg 800w,
    img/foto-1600.jpg 1600w"
  sizes="(min-width: 60rem) 50vw, 100vw"
  alt="...">
```

El navegador elige un candidato considerando información disponible.

# 3. sizes

Con descriptores `w`, sizes comunica el tamaño de presentación esperado bajo condiciones.

Un srcset sin sizes apropiado puede producir elecciones menos eficientes.

# 4. picture

Para **dirección artística**:

```html
<picture>
  <source media="(min-width: 60rem)"
          srcset="hero-wide.jpg">
  <img src="hero-mobile.jpg" alt="...">
</picture>
```

Aquí no solo cambia resolución: puede cambiar recorte/composición.

# 5. Formato

picture también puede ofrecer formatos alternativos con fallback.

No dupliques recursos sin medir beneficio/costo de mantenimiento.

# 6. Dimensiones

Mantén width/height o `aspect-ratio` apropiado para reservar espacio y reducir layout shift.

# 7. LCP

La imagen principal visible inicialmente puede ser el Largest Contentful Paint.

No le pongas lazy loading por costumbre. Prioridad/carga debe analizarse.

# 8. Práctica guiada

Hero:
- versión móvil;
- versión amplia;
- dos resoluciones;
- dimensiones;
- alt contextual.

Observa en Network qué recurso descarga el navegador a distintos tamaños/DPR.

# 9. Errores frecuentes
- imagen 4000px para miniatura;
- srcset sin comprender sizes;
- picture para todo;
- lazy en hero crítico;
- dimensiones ausentes.

# 10. Reto
Hero responsive con evidencia en Network de que no siempre descarga el recurso mayor.

# 11. Autoevaluación
1. ¿max-width reduce bytes descargados?
2. ¿Qué comunica srcset?
3. ¿Para qué sizes?
4. ¿Cuándo picture?
5. ¿Qué es dirección artística?
6. ¿Lazy siempre?

# 12. Checklist
- [ ] Imagen fluida.
- [ ] Recurso adecuado.
- [ ] Dimensiones.
- [ ] Dirección artística cuando aplica.

Continúa con variables.
