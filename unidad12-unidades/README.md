# Unidad 12: Unidades, tamaños y límites

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Elegir unidades relativas/absolutas y crear tamaños fluidos sin impedir zoom ni adaptación.

# 1. px

CSS px es una unidad de referencia, no necesariamente un píxel físico de pantalla.

Útil para bordes/detalles y también puede usarse en otros contextos, pero no conviertas todo el diseño en dimensiones rígidas.

# 2. rem

```css
padding: 1rem;
```

Se basa en el tamaño de fuente del elemento raíz.

Es útil para escalas coherentes que respondan a preferencias/configuración del usuario.

# 3. em

Depende del tamaño de fuente del elemento (o del contexto de la propiedad).

Puede ser útil cuando un componente debe escalar consigo mismo, pero el anidamiento puede sorprender.

# 4. Porcentajes

Su referencia depende de la propiedad/contexto.

`width:50%` suele depender del bloque contenedor; otros porcentajes tienen reglas distintas.

No memorices “% = padre” para todo.

# 5. Viewport

`vw`, `vh` y unidades modernas como `dvh`, `svh`, `lvh` ayudan con viewport móvil y barras dinámicas.

No uses 100vh por reflejo cuando la UI móvil requiera otra semántica.

# 6. ch

Aproxima el ancho del carácter "0" de la fuente.

Útil para limitar líneas de texto:

```css
.prose {
  max-width: 65ch;
}
```

# 7. min/max/clamp

```css
.container {
  width: min(100% - 2rem, 70rem);
}
```

```css
h1 {
  font-size: clamp(2rem, 5vw, 4rem);
}
```

`clamp(min, preferido, max)`.

# 8. Texto y zoom

No desactives zoom mediante viewport.

Usa tamaños/containers que puedan adaptarse cuando el usuario aumenta texto o zoom.

# 9. Práctica guiada

Construye:

- container fluido;
- ancho de lectura 65ch;
- heading con clamp;
- espacio con rem.

Prueba 320px y zoom 200%.

# 10. Errores frecuentes

- todo px rígido;
- 100vw generando overflow con scrollbar;
- 100vh sin considerar móvil;
- em anidado sin comprender;
- viewport que bloquea zoom.

# 11. Reto
Layout fluido sin media query que mantenga límites legibles.

# 12. Autoevaluación

1. ¿px = píxel físico?
2. ¿rem depende de qué?
3. ¿em?
4. ¿% siempre padre?
5. ¿Qué hace clamp?
6. ¿Por qué dvh?

# 13. Checklist

- [ ] Elijo unidad con criterio.
- [ ] Uso límites fluidos.
- [ ] Pruebo zoom.
- [ ] Evito rigidez innecesaria.

Continúa con color.



## Laboratorio completo: Unidades relativas

### Comprender antes de modificar

rem se refiere al tamaño de fuente raíz y em depende del contexto de la propiedad. Para padding, 1em corresponde al tamaño de fuente del propio elemento; para font-size se relaciona con la fuente heredada. En esta tarjeta, aumentar font-size también aumenta su padding de 1em. ch aproxima el ancho del carácter cero de la fuente, no un conteo exacto de letras de cualquier texto.

clamp define límite inferior, preferencia y límite superior. Aquí h1 puede crecer con el viewport, pero no indefinidamente. Los porcentajes dependen de la propiedad y del bloque de referencia: no son una regla universal de porcentaje del padre. No bloquees el zoom ni fijes html a un tamaño que desconozca las preferencias del usuario. Un diseño necesita probar texto y zoom, incluso cuando usa unidades relativas.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

El título crece hasta su límite y el bloque de lectura no ocupa toda una pantalla grande. En pantalla pequeña cabe en el ancho disponible. El padding de la tarjeta corresponde a su propia fuente.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main class="lectura"><h1>Una medida para leer</h1><p>Una línea demasiado larga hace difícil volver al comienzo de la siguiente. Este bloque usa una anchura máxima relacionada con caracteres y conserva espacio en pantallas pequeñas.</p><div class="tarjeta"><h2>Espaciado local</h2><p>El tamaño del texto de esta tarjeta cambia sin modificar todo el documento.</p></div></main>
```

Las reglas específicas del tema son:

```css
.lectura { max-width: 60ch; margin-inline: auto; }
h1 { font-size: clamp(1.75rem, 5vw, 3rem); line-height: 1.2; }
.tarjeta { font-size: 1.25rem; padding: 1em; border: 2px solid #075985; }

```

### Experimento y explicación

Cambia la fuente de tarjeta a 2rem. Compara padding:1em y padding:1rem. Calcula qué pasa si la fuente raíz es 16 px y luego cambia la preferencia del navegador.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Usas 100vw para el contenido junto a márgenes y aparece scroll horizontal.

**Cómo resolver:** 100vw mide el viewport, no el espacio restante después de márgenes. Usa un ancho automático o 100% con modelo de caja apropiado y comprueba el elemento responsable.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 11: Modelo de caja](../unidad11-box-model/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 13: Color, fondos y contraste](../unidad13-color/README.md)
