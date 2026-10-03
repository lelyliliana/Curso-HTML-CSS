# Unidad 17 — CSS Grid

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


---

## Continuar el curso

- **Unidad anterior:** [Unidad 16 — Flexbox](../unidad16-flexbox/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 18 — Posicionamiento y capas](../unidad18-posicionamiento/README.md)
