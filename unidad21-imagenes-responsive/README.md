# Unidad 21: Imágenes responsive

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

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



## Laboratorio completo: Selección de imágenes

### Comprender antes de modificar

picture permite elegir una composición según condiciones (dirección artística) o formatos soportados. source aporta candidatos y el img final es obligatorio como alternativa y portador del texto alternativo. En este ejemplo la imagen cuadrada conserva la información principal, pero organiza las mesas de otra manera. El alt debe seguir describiendo de forma válida el contenido seleccionado.

srcset con descriptores w y sizes sirve para elegir recursos según anchura de presentación y densidad de pantalla. sizes describe el espacio que ocupará la imagen; no le asigna ancho CSS. Con candidatos 400w y 800w, el navegador puede elegir según DPR, caché y otras decisiones. No prometas que una URL siempre será seleccionada en un ancho dado. Los SVG de este ejemplo son vectoriales: no necesitamos exportar muchas resoluciones para nitidez. Para fotografías sí importa ofrecer tamaños y formatos apropiados.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

A 320 px se ve composición cuadrada; en pantalla amplia, horizontal. En DevTools puedes consultar currentSrc del img para reconocer el recurso elegido. No hay una imagen rota como fallback.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Ilustración adaptable</h1><picture><source media="(max-width: 35rem)" srcset="../../recursos/img/aula-cuadrada.svg"><img src="../../recursos/img/aula.svg" alt="Aula con mesas y una pizarra" width="800" height="450"></picture><p>En poco espacio se usa una composición cuadrada. En una pantalla ancha se conserva la composición horizontal.</p></main>
```

Las reglas específicas del tema son:

```css
picture { display: block; max-width: 50rem; }
```

### Experimento y explicación

Cambia el umbral de source y comprueba currentSrc. Explica por qué sizes no cambia el ancho CSS. Si trabajas con una fotografía propia, prepara versiones reales de distinta resolución antes de escribir candidatos w.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Añades loading="lazy" a la imagen principal situada al comenzar la página.

**Cómo resolver:** Evalúa si es candidata a LCP. La imagen principal visible suele necesitar carga temprana; reserva lazy para imágenes fuera de la vista inicial cuando corresponda.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 20: Media queries y container queries](../unidad20-media-queries/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 22: Variables CSS y funciones](../unidad22-variables/README.md)
