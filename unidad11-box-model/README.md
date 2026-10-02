# Unidad 11 — Modelo de caja

```text
margin
  border
    padding
      content
```

## box-sizing
```css
*, *::before, *::after {
  box-sizing: border-box;
}
```

Con border-box, width incluye padding/border.

## Overflow
El contenido puede desbordar. No ocultes overflow automáticamente sin comprender qué información desaparece.

## Reto
Construye tarjetas con ancho estable y explica cada parte de la caja.
