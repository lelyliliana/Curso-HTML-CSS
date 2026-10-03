# Unidad 19 — Diseño responsive y mobile-first

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Construir interfaces que se adapten al espacio y al contenido antes de añadir breakpoints.

# 1. Responsive no significa tres versiones

No diseñamos obligatoriamente:
```text
móvil / tablet / escritorio
```

Diseñamos un sistema que funciona a través de un continuo de tamaños.

# 2. Mobile-first

Empieza con reglas que funcionen en espacio estrecho y añade cambios cuando haya espacio suficiente.

No significa diseñar solo para teléfono.

# 3. Primero lo fluido

Antes de media queries prueba:
- max-width;
- min()/max()/clamp();
- Flex wrap;
- Grid auto-fit/minmax;
- imágenes fluidas;
- tamaños intrínsecos.

Muchos componentes pueden adaptarse sin breakpoint.

# 4. Contenedor

```css
.container {
  width: min(100% - 2rem, 70rem);
  margin-inline: auto;
}
```

Crea margen flexible y ancho máximo.

# 5. Contenido que decide

Una tarjeta necesita cambio cuando su contenido ya no cabe cómodamente, no porque el dispositivo se llame “tablet”.

Redimensiona lentamente y observa el punto de tensión.

# 6. Reflow

A zoom alto o viewport estrecho, el contenido debería reacomodarse sin exigir scroll horizontal general para lectura ordinaria.

Excepciones como tablas/código ancho pueden necesitar scroll localizado.

# 7. Orden

Responsive no debe depender de reordenar visualmente elementos de manera que DOM/teclado tengan otra secuencia lógica.

# 8. Touch

No dependas de hover para revelar información imprescindible.

Los controles deben tener áreas de interacción razonables y separación suficiente.

# 9. Práctica guiada

Construye landing sin media queries usando:
- container;
- Grid auto-fit;
- Flex wrap;
- clamp.

Solo después identifica qué parte realmente necesita cambiar de composición.

# 10. Errores frecuentes
- breakpoints por modelo de teléfono;
- ancho fijo;
- ocultar contenido para que “quepa”;
- hover como única interacción;
- reordenar visualmente contra DOM.

# 11. Reto
Página funcional desde 320px hasta pantalla amplia con el menor número de breakpoints justificables.

# 12. Autoevaluación
1. ¿Responsive = tres tamaños?
2. ¿Qué es mobile-first?
3. ¿Qué probar antes de media query?
4. ¿Quién debería determinar breakpoint?
5. ¿Hover basta en touch?

# 13. Checklist
- [ ] Diseño fluido.
- [ ] Contenido guía cambios.
- [ ] Pruebo continuo de tamaños.
- [ ] Mantengo orden lógico.

Continúa con media queries.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 18 — Posicionamiento y capas](../unidad18-posicionamiento/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 20 — Media queries y container queries](../unidad20-media-queries/README.md)
