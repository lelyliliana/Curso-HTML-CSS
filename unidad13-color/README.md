# Unidad 13: Color, fondos y contraste

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Usar color dentro de un sistema visual sin convertirlo en el único canal de información.

# 1. Sintaxis

```css
color: #1f2937;
background-color: rgb(255 255 255);
border-color: hsl(220 10% 80%);
```

CSS moderno ofrece varias sintaxis. Elige una convención consistente.

# 2. Texto y fondo

`color` afecta texto/foreground.  
`background-color` pinta fondo.

El contraste depende de la combinación.

# 3. Contraste

No evalúes “se ve bien en mi monitor” como prueba.

Usa herramientas y revisa también estados interactivos.

# 4. Color no debe ser el único indicador

Un error no debería comunicarse únicamente volviendo un campo rojo.

Añade texto, icono u otra señal comprensible.

# 5. Texto sobre imagen

Si existe texto sobre fotografía/gradiente, comprueba contraste en distintas zonas y tamaños.

Un overlay puede ayudar, pero debe verificarse.

# 6. Bordes y sombras

Son herramientas visuales, no semánticas.

Una sombra no convierte un div en botón.

# 7. Tokens

```css
:root {
  --color-text: #1f2937;
  --color-surface: #fff;
  --color-danger: #b42318;
}
```

Permiten consistencia. Los profundizaremos en Unidad 22.

# 8. Tema oscuro

`prefers-color-scheme` puede ayudar a responder a preferencias.

No inviertas colores automáticamente sin revisar imágenes, bordes, sombras y contraste.

# 9. Práctica guiada

Diseña estados normal, información, éxito y error. Cada uno debe poder reconocerse sin depender solo del color.

# 10. Errores frecuentes

- contraste a ojo;
- rojo/verde como única señal;
- texto sobre imagen sin prueba;
- demasiados colores;
- dark mode como inversión automática.

# 11. Reto
Paleta pequeña con estados y comprobación de contraste.

# 12. Autoevaluación

1. ¿color vs background?
2. ¿Por qué no solo rojo/verde?
3. ¿Qué son tokens?
4. ¿Sombras añaden semántica?
5. ¿Dark mode es invertir colores?

# 13. Checklist

- [ ] Contraste.
- [ ] Señales redundantes.
- [ ] Paleta coherente.
- [ ] Estados accesibles.

Continúa con tipografía.



## Laboratorio completo: Color y estados

### Comprender antes de modificar

El color puede reforzar significado, pero no debe ser su única señal. Confirmada y Atención aparecen como texto para que la diferencia no dependa de reconocer verde o naranja. Un enlace subrayado se reconoce también sin distinguir su tono. Evalúa el contraste del texto con el fondo efectivo, especialmente cuando hay transparencias o imágenes.

Para WCAG AA, el texto normal requiere al menos 4.5:1 y el texto grande 3:1, con excepciones definidas por el criterio. Texto grande tiene una definición específica (aproximadamente 24 px normal o 18.66 px en negrita bajo la conversión habitual), no cualquier encabezado. Los requisitos de componentes y gráficos relevantes son diferentes del criterio de texto. Una paleta bonita no garantiza legibilidad: mide cada pareja utilizada. No confundas contraste con saturación o brillo percibido.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Los dos avisos pueden distinguirse por palabras incluso en escala de grises. Los enlaces mantienen subrayado. Usa un comprobador de contraste para las parejas texto/fondo, no para colores aislados.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Estado de una solicitud</h1><p class="estado"><strong>Confirmada:</strong> puedes asistir al taller.</p><p class="advertencia"><strong>Atención:</strong> la sesión comienza a las 15:00.</p><p><a href="#detalle">Leer indicaciones</a></p><section id="detalle"><h2>Indicaciones</h2><p>Trae un cuaderno.</p></section></main>
```

Las reglas específicas del tema son:

```css
.estado { background: #f0fdf4; color: #14532d; border-inline-start: .35rem solid #14532d; padding: 1rem; }
.advertencia { background: #fff7ed; color: #7c2d12; padding: 1rem; }
a { text-decoration: underline; }

```

### Experimento y explicación

Diseña un tercer estado Cancelada con texto y una señal visual adicional. Prueba la página en escala de grises. Registra la pareja de colores y el contraste, manteniendo legible texto pequeño.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Un enlace solo se diferencia del párrafo por un azul poco contrastado.

**Cómo resolver:** Mantén subrayado u otra señal persistente y revisa contraste. El foco debe aportar una señal adicional durante navegación con teclado.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 12: Unidades, tamaños y límites](../unidad12-unidades/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 14: Tipografía y legibilidad](../unidad14-tipografia/README.md)
