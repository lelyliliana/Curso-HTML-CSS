# Unidad 11 — Modelo de caja

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


---

## Continuar el curso

- **Unidad anterior:** [Unidad 10 — Selectores y especificidad](../unidad10-selectores/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 12 — Unidades, tamaños y límites](../unidad12-unidades/README.md)
