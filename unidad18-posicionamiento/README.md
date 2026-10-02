# Unidad 18 — Posicionamiento y capas

## Qué aprenderás
Usar relative, absolute, fixed y sticky comprendiendo containing blocks y stacking contexts.

# 1. static

Es el posicionamiento normal por defecto para muchos elementos.

`top/right/bottom/left` no funcionan como con elementos posicionados.

# 2. relative

```css
.card {
  position: relative;
}
```

Permanece en el flujo y puede convertirse en referencia para descendientes absolute según reglas de containing block.

# 3. absolute

```css
.badge {
  position: absolute;
  inset-block-start: .5rem;
  inset-inline-end: .5rem;
}
```

Sale del flujo normal para posicionamiento y se ubica respecto a su containing block, no automáticamente respecto a “la pantalla”.

# 4. Patrón badge

```css
.card { position: relative; }
.badge { position: absolute; ... }
```

Aquí la relación visual pertenece al componente.

# 5. fixed

Se posiciona normalmente respecto al viewport, con excepciones/contextos creados por ciertas propiedades ancestras.

Útil para elementos persistentes, pero puede tapar contenido/controles.

# 6. sticky

```css
.header {
  position: sticky;
  top: 0;
}
```

Combina comportamiento de flujo y fijación dentro de su contenedor/scrolling context.

Puede “no funcionar” por overflow, tamaño o contexto del ancestro.

# 7. z-index

No es un ranking global.

Funciona dentro de **stacking contexts**.

Un hijo con z-index 999999 no puede necesariamente escapar del stacking context de su padre para superar otro contexto.

# 8. Stacking contexts

Pueden crearse por propiedades como:
- posicionamiento + z-index en ciertos casos;
- opacity <1;
- transform;
- isolation;
y otras.

DevTools ayuda a diagnosticar.

# 9. Modal

Un modal real requiere más que `position:fixed`:
- semántica;
- foco;
- cierre;
- bloqueo/gestión del fondo;
- teclado.

Aquí solo estudiamos layout/capas; no declares un modal accesible completo solo por dibujar una caja.

# 10. Práctica guiada

Construye:
- badge absolute;
- header sticky;
- botón fixed.

Después crea dos stacking contexts y comprueba por qué un z-index enorme no gana.

# 11. Errores frecuentes
- absolute para maquetar toda página;
- z-index cada vez mayor;
- sticky sin revisar overflow;
- fixed tapando contenido;
- modal visual sin interacción accesible.

# 12. Reto
Componente con badge y cabecera sticky, documentando containing block y stacking context.

# 13. Autoevaluación
1. ¿relative sale del flujo?
2. ¿Absolute respecto a qué?
3. ¿Sticky siempre respecto al viewport?
4. ¿z-index es global?
5. ¿Qué es stacking context?
6. ¿Una caja fixed ya es modal accesible?

# 14. Checklist
- [ ] Elijo position con propósito.
- [ ] Identifico containing block.
- [ ] Comprendo capas.
- [ ] Evito z-index arbitrario.

Continúa con responsive.
