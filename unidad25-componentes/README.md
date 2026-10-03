# Unidad 25 — Componentes y arquitectura CSS

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


---

## Continuar el curso

- **Unidad anterior:** [Unidad 24 — Transiciones y animaciones](../unidad24-animaciones/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 26 — Accesibilidad visual y estados](../unidad26-accesibilidad-css/README.md)
