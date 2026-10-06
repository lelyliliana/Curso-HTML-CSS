# Unidad 17: CSS Grid

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Construir layouts bidimensionales con tracks, gaps y tamaños flexibles, y decidir cuándo Grid o Flex expresa mejor la relación espacial.

# 1. Contenedor

```css
.grid {
  display: grid;
}
```

Los hijos directos son grid items.

# 2. Columnas

```css
.grid {
  grid-template-columns: 1fr 1fr 1fr;
}
```

`fr` distribuye espacio flexible disponible dentro del grid.

No equivale simplemente a porcentaje.

# 3. repeat

```css
grid-template-columns: repeat(3, 1fr);
```

Evita repetir tracks idénticos.

# 4. minmax + auto-fit

```css
grid-template-columns:
  repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
```

Las columnas se adaptan al espacio disponible sin necesitar un breakpoint para cada cantidad.

# 5. auto-fit vs auto-fill

Ambos generan tracks repetidos, pero difieren en cómo manejan tracks vacíos/espacio.

Experimenta en DevTools en lugar de memorizar una frase.

# 6. gap

```css
gap: 1rem;
```

Funciona entre filas/columnas sin márgenes de compensación.

# 7. Colocar items

```css
.destacada {
  grid-column: span 2;
}
```

Un item puede ocupar varios tracks.

No fuerces spans que produzcan overflow en pantallas estrechas.

# 8. Áreas

```css
grid-template-areas:
  "header header"
  "nav main";
```

Pueden hacer layouts de página legibles cuando las áreas son estables.

No cambian el orden del DOM semántico.

# 9. Grid vs Flex

Pregunta:

- ¿la relación principal es una fila/columna? Flex.
- ¿necesito coordinar filas y columnas? Grid.
- ¿un componente Grid contiene Flex? Perfectamente válido.

No son rivales.

# 10. Intrinsic sizing

Contenido largo puede influir en tamaños mínimos.

Patrones como `minmax(0,1fr)` pueden permitir encogimiento cuando un track flexible desborda por min-content.

Diagnostica antes de aplicar.

# 11. Práctica guiada

Construye galería auto-fit y dashboard con áreas.

Redimensiona continuamente, no solo en tres anchos.

# 12. Errores frecuentes

- Grid para cualquier fila simple;
- columnas fijas que desbordan;
- cambiar orden visual ignorando DOM;
- media query para cada columna cuando auto-fit resuelve;
- no entender tamaño intrínseco.

# 13. Reto
Dashboard responsive con Grid y componentes internos Flex, justificando cada elección.

# 14. Autoevaluación

1. ¿Qué es track?
2. ¿Qué significa fr?
3. ¿Para qué minmax?
4. ¿Grid vs Flex?
5. ¿Áreas cambian DOM?
6. ¿Qué problema puede causar min-content?

# 15. Checklist

- [ ] Diseño tracks.
- [ ] Uso tamaños flexibles.
- [ ] Combino Grid/Flex.
- [ ] Mantengo DOM lógico.

Continúa con posicionamiento.



## Laboratorio completo: Grid adaptable

### Comprender antes de modificar

Grid coordina filas y columnas. La regla repetida crea tantas columnas de un mínimo definido como permita el contenedor. min(100%,16rem) evita exigir 16rem cuando todo el contenedor es más estrecho. 1fr reparte espacio flexible restante, no un porcentaje fijo del ancho total.

auto-fit colapsa pistas vacías generadas por la repetición y permite a las ocupadas aprovechar espacio. auto-fill conserva esas pistas aunque no haya elementos en todas. La diferencia se aprecia con pocos elementos y un contenedor ancho. gap se descuenta antes de repartir espacio. Para dos columnas iguales con contenido largo, minmax(0,1fr) permite un mínimo de pista cero, pero el contenido interior todavía necesita poder partirse o ajustarse. No fuerces spans de dos columnas en pantallas donde solo existe una.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Hay una, dos o tres columnas según el ancho disponible. Todas mantienen espacio entre tarjetas. Con una sola tarjeta en pantalla grande, auto-fit permite que ocupe el espacio disponible.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Galería de talleres</h1><div class="galeria"><article><h2>Lectura</h2><p>Historias compartidas.</p></article><article><h2>Robótica</h2><p>Diseño y construcción.</p></article><article><h2>Arte</h2><p>Crear con materiales cotidianos.</p></article></div></main>
```

Las reglas específicas del tema son:

```css
.galeria { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr)); gap: 1rem; }
.galeria article { border: 2px solid #075985; padding: 1rem; min-width: 0; overflow-wrap: anywhere; }

```

### Experimento y explicación

Deja una tarjeta y compara auto-fit con auto-fill en una ventana ancha. Restablece tres tarjetas. Introduce un título muy largo y verifica que no produzca scroll horizontal.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Usas minmax(300px,1fr) en un contenedor de 280 px y aparece desbordamiento.

**Cómo resolver:** El mínimo de 300 px es una restricción real. Reduce el mínimo para ese contexto o usa min(100%,300px) para permitir una sola columna estrecha.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 16: Flexbox](../unidad16-flexbox/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 18: Posicionamiento y capas](../unidad18-posicionamiento/README.md)
