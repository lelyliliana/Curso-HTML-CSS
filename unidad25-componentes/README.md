# Unidad 25: Componentes y arquitectura CSS

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Crear componentes reutilizables con estados claros y organizar CSS para reducir acoplamiento.

# 1. Componente

Ejemplo:

```text
.card
.card__title
.card__body
.card--featured
```

La convención puede recordar BEM, pero no es obligatorio seguir BEM literalmente.

Lo importante es que el componente tenga una responsabilidad visual clara.

# 2. API del componente

HTML esperado:

```html
<article class="card">
  <h2 class="card__title">...</h2>
  <div class="card__body">...</div>
</article>
```

CSS no debería depender de que card esté exactamente dentro de `main > section:nth-child(2)`.

# 3. Variantes

```css
.button {}
.button--primary {}
.button--danger {}
```

Una variante expresa una diferencia intencional.

Evita combinaciones explosivas de clases que contradicen estados.

# 4. Estado

Puede representarse mediante:

- atributos nativos;
- ARIA cuando corresponde;
- data attributes;
- clases.

Ejemplo:
```css
.alert[data-state="error"] {}
```

La fuente del estado debe corresponder a la semántica/interacción real.

# 5. Layout vs componente

El componente no debería imponer márgenes externos específicos para todos los lugares.

El layout padre suele controlar separación entre componentes mediante gap.

Esto mejora reutilización.

# 6. Utilidades

Una utilidad pequeña como `.visually-hidden` puede ser apropiada.

No conviertas toda la hoja en combinaciones de clases atómicas si no has elegido deliberadamente ese enfoque.

# 7. Capas de organización

Una estructura posible:
```text
base
layout
components
utilities
```

En proyectos grandes, `@layer` puede ayudar a ordenar la cascada.

No necesitas una arquitectura enorme para cinco reglas.

# 8. Tokens

Componentes consumen tokens:

```css
.card {
  padding: var(--space-3);
  background: var(--surface-card);
}
```

Evita valores repetidos sin significado.

# 9. Práctica guiada

Construye:

- button;
- card;
- alert;
- field.

Úsalos en dos contextos distintos sin cambiar selectores internos.

# 10. Errores frecuentes

- selector dependiente de página;
- margin externo fijo dentro de componente;
- variante por cada diferencia minúscula;
- nombres puramente visuales;
- arquitectura sobredimensionada.

# 11. Reto
Biblioteca mínima de cuatro componentes con tokens, estados y documentación de uso.

# 12. Autoevaluación

1. ¿Qué hace reutilizable un componente?
2. ¿Quién controla separación externa?
3. ¿BEM es obligatorio?
4. ¿Qué es variante?
5. ¿Cuándo @layer aporta?

# 13. Checklist

- [ ] Componentes desacoplados.
- [ ] Estados claros.
- [ ] Tokens.
- [ ] Layout separado.

Continúa con accesibilidad CSS.



## Laboratorio completo: Componentes reutilizables

### Comprender antes de modificar

Un componente tiene estructura, variantes y estados que pueden repetirse sin copiar reglas divergentes. Aquí tarjeta define la base y tarjeta--destacada una variante. La variante no redefine todos los valores: cambia solo lo que expresa su propósito. Una convención de nombres como esta ayuda a reconocer responsabilidades, pero no es un requisito del navegador.

El componente debe soportar títulos y párrafos de distinta longitud. No uses un id exclusivo por tarjeta para duplicar estilos. La distribución pertenece a coleccion; la apariencia individual a tarjeta. Esta separación permite reutilizar una tarjeta fuera de una cuadrícula. También debes conservar un enlace con nombre descriptivo: dos enlaces que dicen Ver más pueden ser ambiguos fuera de su contexto. Una tarjeta no debería convertirse entera en un enlace con controles interactivos anidados.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Las tarjetas comparten padding, radio y encabezado. La destacada tiene fondo y borde diferentes. Ambas pueden crecer si el párrafo se alarga.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Tarjetas reutilizables</h1><div class="coleccion"><article class="tarjeta"><h2>Lectura</h2><p>Conversar sobre un cuento.</p><a href="#informacion">Ver lectura</a></article><article class="tarjeta tarjeta--destacada"><h2>Robótica</h2><p>Explorar sensores con un montaje sencillo.</p><a href="#informacion">Ver robótica</a></article></div><section id="informacion"><h2>Información</h2><p>Las actividades son ejemplos educativos.</p></section></main>
```

Las reglas específicas del tema son:

```css
.coleccion { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr)); gap: 1rem; }
.tarjeta { padding: 1rem; border: 2px solid #64748b; border-radius: .5rem; }
.tarjeta h2 { margin-block-start: 0; }
.tarjeta--destacada { border-color: #075985; background: #f0f9ff; }

```

### Experimento y explicación

Crea una tercera tarjeta de arte usando la clase base. Añade una variante compacta que cambie únicamente el padding. Prueba un título largo y comprueba los nombres de los enlaces.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Cada tarjeta tiene un CSS distinto aunque representa el mismo componente.

**Cómo resolver:** Extrae las reglas comunes a tarjeta y conserva diferencias como variantes explícitas. Verifica luego todas las instancias para que la extracción no borre un estado necesario.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 24: Transiciones y animaciones](../unidad24-animaciones/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 26: Accesibilidad visual y estados](../unidad26-accesibilidad-css/README.md)
