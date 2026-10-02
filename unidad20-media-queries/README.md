# Unidad 20 — Media queries y container queries

## Qué aprenderás
Cambiar estilos según capacidades/espacio cuando el diseño realmente lo necesita.

# 1. Breakpoint por contenido

```css
@media (min-width: 48rem) {
  .layout {
    grid-template-columns: 2fr 1fr;
  }
}
```

48rem debe surgir del punto donde la composición puede sostener dos columnas, no de “tamaño tablet”.

# 2. min-width

Con mobile-first:
- estilos base para espacio estrecho;
- mejoras progresivas con min-width.

No es la única estrategia posible, pero mantiene una dirección mental sencilla.

# 3. Otras condiciones

Media queries pueden consultar:
- ancho/alto;
- orientación;
- preferencias;
- capacidades de interacción, entre otras.

No uses orientación como sustituto de medir espacio disponible.

# 4. Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  /* reduce movimiento no esencial */
}
```

No significa necesariamente eliminar toda transición instantáneamente; reduce/evita movimiento problemático según diseño.

# 5. Contraste/tema

Existen preferencias como `prefers-color-scheme` y otras capacidades con soporte variable.

Diseña fallback antes de depender de una feature.

# 6. Container queries

Un componente reutilizable puede necesitar responder a **su contenedor**, no al viewport.

```css
.card-list {
  container-type: inline-size;
}

@container (min-width: 30rem) {
  .card {
    grid-template-columns: 10rem 1fr;
  }
}
```

Esto desacopla el componente de dónde se ubica.

# 7. Media vs container

Media query:
> ¿cómo está el viewport/dispositivo/preferencia?

Container query:
> ¿cuánto espacio tiene este componente?

# 8. Feature queries

```css
@supports (display: grid) {
  ...
}
```

Permiten mejora progresiva cuando necesitas soportar entornos diversos.

# 9. Práctica guiada

Crea una card que aparece en sidebar estrecho y main ancho. Hazla adaptarse mediante container query sin saber el ancho del viewport.

# 10. Errores frecuentes
- breakpoints por dispositivo;
- docenas de media queries;
- viewport query para componente reutilizable;
- reduced-motion ignorado;
- depender de feature sin fallback cuando el soporte objetivo lo exige.

# 11. Reto
Layout con un breakpoint de página y un componente que responda a su contenedor.

# 12. Autoevaluación
1. ¿Qué define breakpoint?
2. ¿Qué significa mobile-first?
3. ¿Media vs container query?
4. ¿Qué consulta prefers-reduced-motion?
5. ¿Para qué @supports?

# 13. Checklist
- [ ] Breakpoints justificados.
- [ ] Componentes independientes.
- [ ] Respeto preferencias.
- [ ] Diseño mejora progresivamente.

Continúa con imágenes responsive.
