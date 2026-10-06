# Unidad 22: Variables CSS y funciones

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Crear tokens con custom properties, comprender alcance/herencia y combinar calc, min, max y clamp.

# 1. Custom property

```css
:root {
  --space-1: .5rem;
  --space-2: 1rem;
  --radius: .75rem;
}
```

Uso:

```css
.card {
  padding: var(--space-2);
  border-radius: var(--radius);
}
```

# 2. Son parte de la cascada

Las custom properties heredan y pueden sobrescribirse por contexto.

```css
.theme-dark {
  --surface: #111;
  --text: #fff;
}
```

Los descendientes usan los nuevos valores.

# 3. Fallback

```css
color: var(--text-color, #222);
```

El fallback se usa si la custom property no está definida/usable según reglas de var.

No sustituye un sistema de tokens bien definido.

# 4. Token semántico

Mejor:
```css
--color-danger
--surface-card
```

que:
```css
--red
--white-box
```

cuando el valor puede cambiar de tema.

# 5. calc

```css
width: calc(100% - 2rem);
```

Combina unidades compatibles bajo reglas CSS.

# 6. min/max

```css
width: min(100% - 2rem, 70rem);
```

Escoge el menor resultado.

# 7. clamp

```css
font-size: clamp(2rem, 4vw + 1rem, 4rem);
```

Define mínimo, valor preferido y máximo.

# 8. Tokens no son variables Sass

Las custom properties existen en tiempo de ejecución del navegador y participan en cascada/herencia.

Esto permite temas/contextos dinámicos sin recompilar CSS.

# 9. Práctica guiada

Extrae de una página:

- espacios;
- radios;
- superficies;
- texto;
- acento.

Crea tokens semánticos y un segundo tema.

# 10. Errores frecuentes

- variable para cada literal sin sistema;
- nombres ligados a color actual;
- no comprender alcance;
- calc innecesario;
- clamp con valores que no producen transición útil.

# 11. Reto
Sistema pequeño de tokens con tema alternativo sin duplicar componentes.

# 12. Autoevaluación

1. ¿Custom property hereda?
2. ¿Qué hace var fallback?
3. ¿Token semántico?
4. ¿calc para qué?
5. ¿Qué hace clamp?
6. ¿Custom property existe solo al compilar?

# 13. Checklist

- [ ] Tokens con significado.
- [ ] Comprendo alcance.
- [ ] Uso funciones fluidas.
- [ ] Evito duplicación de tema.

Continúa con pseudoclases.



## Laboratorio completo: Variables para un sistema visual

### Comprender antes de modificar

Las propiedades personalizadas participan en la cascada y normalmente se heredan. Una declaración en :root ofrece valores generales; una redefinición en .tema afecta esa tarjeta y sus descendientes. No reemplaza automáticamente cualquier color escrito como literal. Para recibir el cambio, la declaración debe utilizar var(--acento).

Los nombres pueden describir propósito, como acento o espacio, en vez de un color concreto que luego cambie. Un fallback var(--token,valor) se usa ante ciertas situaciones de ausencia o valor inválido de la propiedad personalizada, pero no convierte cualquier resultado inválido en CSS válido. Los tokens ayudan a mantener consistencia; no prueban contraste ni garantizan que todos los componentes se adapten a cualquier tema. Después de cambiar un token verifica sus usos reales y los estados de interacción.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

La primera tarjeta y su enlace son azules; la segunda utiliza púrpura. Espacio y radio se mantienen iguales. En Computed puedes reconocer el valor heredado de --acento.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Tokens de diseño</h1><article class="tarjeta"><h2>Lectura</h2><p>Una tarjeta reutiliza color y espacio.</p><a href="#nota">Ver detalles</a></article><article class="tarjeta tema"><h2>Robótica</h2><p>La segunda tarjeta cambia el token de acento.</p><a href="#nota">Ver detalles</a></article><p id="nota">Los contenidos comparten una estructura.</p></main>
```

Las reglas específicas del tema son:

```css
:root { --acento: #075985; --espacio: 1rem; --radio: .5rem; }
.tarjeta { border: 2px solid var(--acento); padding: var(--espacio); border-radius: var(--radio); margin-block: var(--espacio); }
.tarjeta a { color: var(--acento); }
.tema { --acento: #6b21a8; }

```

### Experimento y explicación

Añade una tercera tarjeta con otro acento oscuro. Cambia --espacio solo en esa tarjeta. Comprueba qué descendientes heredan la variable y mide contraste del nuevo enlace.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Escribes var(acento) y el borde no toma el color.

**Cómo resolver:** El nombre de una propiedad personalizada comienza por --. Comprueba sintaxis y nombre exacto: var(--acento).

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 21: Imágenes responsive](../unidad21-imagenes-responsive/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 23: Pseudoclases y pseudoelementos](../unidad23-pseudo/README.md)
