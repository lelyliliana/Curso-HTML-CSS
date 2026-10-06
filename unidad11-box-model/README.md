# Unidad 11: Modelo de caja

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Calcular el espacio real de un elemento y comprender margin, border, padding, content, box-sizing y overflow.

# 1. Caja

```text
margin
└─ border
   └─ padding
      └─ content
```

Cada elemento genera cajas según su display/contexto.

# 2. content-box

Por defecto, `width` normalmente define el ancho del content box.

```css
.card {
  width: 300px;
  padding: 20px;
  border: 2px solid;
}
```

Ancho exterior sin margin:
```text
300 + 40 + 4 = 344px
```

# 3. border-box

```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

Ahora width incluye content + padding + border.

Una caja width:300px ocupa 300px de borde a borde.

# 4. Margin

Margin separa cajas.

Los márgenes verticales de bloques en flujo normal pueden colapsar bajo ciertas condiciones; no siempre se suman como esperarías.

Flex/Grid cambian este comportamiento.

# 5. Padding

Espacio interno entre contenido y borde.

No uses espacios HTML para crear padding.

# 6. Overflow

Si el contenido no cabe:

- visible;
- hidden;
- auto;
- scroll;
- clip, según necesidad.

`overflow:hidden` puede ocultar contenido, foco o sombras. No lo uses solo para “arreglar” una caja sin entender el desbordamiento.

# 7. min/max

```css
.card {
  width: 100%;
  max-width: 40rem;
}
```

Permite flexibilidad con límites.

# 8. Práctica guiada

Construye dos cajas iguales:

- content-box;
- border-box.

Mide en DevTools y explica la diferencia.

# 9. Errores frecuentes

- olvidar padding/border en tamaño;
- usar width fija y padding que rompe layout;
- ocultar overflow;
- margin para crear espacio interno;
- no revisar min-content/desbordamiento de texto largo.

# 10. Reto
Tarjeta de ancho estable con contenido largo y sin scroll horizontal accidental.

# 11. Autoevaluación

1. ¿Qué incluye content-box?
2. ¿Qué incluye border-box?
3. ¿Margin es interno?
4. ¿Overflow hidden siempre?
5. ¿Qué hacen max-width/min-width?

# 12. Checklist

- [ ] Calculo caja.
- [ ] Uso border-box.
- [ ] Distingo margin/padding.
- [ ] Diagnostico overflow.

Continúa con unidades.



## Laboratorio completo: Medir el modelo de caja

### Comprender antes de modificar

width no siempre expresa el ancho exterior. Con content-box, la declaración mide el contenido; padding y border se suman. Con border-box incluye contenido, padding y border. Los márgenes siguen estando fuera en ambos casos. En este ejemplo no hay min/max-width ni reglas adicionales que alteren la comparación.

La caja content-box mide 200 + 40 + 10 = 250 px entre bordes exteriores. La border-box mide 200 px y deja 150 px para contenido. DevTools muestra un esquema de las capas. El espacio entre dos bloques puede incluir colapso de márgenes verticales en ciertos contextos; no supongas que siempre se suman. Para distribuir componentes con una separación estable, gap en Flex/Grid suele expresar mejor esa relación. box-sizing se usa como política general, pero entender la suma permite reconocer cuándo un tamaño no cabe.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

La primera caja ocupa 250 px y la segunda 200 px. Inspecciona ambas: tienen el mismo padding y borde, pero distinta anchura de contenido.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Modelo de caja</h1><div class="caja contenido">content-box: ancho declarado 200 px</div><div class="caja borde">border-box: ancho declarado 200 px</div></main>
```

Las reglas específicas del tema son:

```css
.caja { width: 200px; padding: 20px; border: 5px solid #075985; margin-block: 1rem; overflow-wrap: anywhere; }
.contenido { box-sizing: content-box; }
.borde { box-sizing: border-box; }

```

### Experimento y explicación

Cambia padding a 10 px y border a 2 px. Calcula los anchos exteriores y de contenido antes de medir. Después fija width:100% en una caja dentro de un contenedor estrecho y explica qué política evita sumar ancho extra.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Pones width:100% con padding y ocultas el desbordamiento del body para que desaparezca el scroll.

**Cómo resolver:** Revisa la caja que supera su contenedor y corrige box-sizing o el tamaño. Ocultar desbordamiento global puede recortar contenido y controles sin resolver la causa.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 10: Selectores y especificidad](../unidad10-selectores/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 12: Unidades, tamaños y límites](../unidad12-unidades/README.md)
