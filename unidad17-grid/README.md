# Unidad 17 — CSS Grid

Grid trabaja muy bien con filas y columnas.

```css
.grid {
 display:grid;
 grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
 gap:1rem;
}
```

## Grid vs Flex
No son rivales. Elige según la relación espacial.

## Reto
Crea dashboard responsive sin media query para el número básico de columnas.
