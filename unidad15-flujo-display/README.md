# Unidad 15 — Flujo normal y display

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Comprender dónde coloca el navegador los elementos antes de utilizar Flexbox, Grid o position.

# 1. Flujo normal

Sin layout especial, los elementos participan en el flujo del documento.

Los bloques se organizan en la dirección de bloque y el contenido inline fluye en líneas.

Comprenderlo evita usar position para todo.

# 2. block

Un bloque normalmente comienza una nueva línea y utiliza el espacio disponible según su contexto.

# 3. inline

Participa dentro de una línea de texto.

```html
<p>Aprende <strong>HTML</strong> hoy.</p>
```

Width/height no se comportan igual que en un bloque.

# 4. inline-block

Fluye en línea pero genera una caja que admite dimensiones de forma similar a un bloque.

Flex/Grid resuelven hoy muchos layouts que antes usaban inline-block.

# 5. display:none

Retira el elemento del layout y normalmente también de la accesibilidad expuesta.

No lo uses para contenido que debe seguir disponible a tecnologías de asistencia.

# 6. visibility:hidden

Oculta visualmente conservando espacio.

No es equivalente a display:none.

# 7. Visualmente oculto

Para contenido destinado a lectores de pantalla existen patrones específicos de “visually hidden”; no uses display:none.

# 8. Flujo y márgenes

En flujo normal pueden ocurrir colapsos de márgenes verticales.

Flex/Grid crean contextos con reglas distintas.

# 9. Práctica guiada

Crea bloques y spans. Cambia solo display y observa salto de línea, dimensiones y espacio.

# 10. Errores frecuentes
- absolute para layout normal;
- display:none para label accesible;
- width en inline esperando bloque;
- aprender Flex sin entender flujo.

# 11. Reto
Página simple solo con flujo normal y explicación de la posición de cada elemento.

# 12. Autoevaluación
1. ¿Qué es flujo normal?
2. ¿Block/inline?
3. ¿display:none conserva espacio?
4. ¿Cómo ocultar solo visualmente?
5. ¿Por qué flujo antes de Flex?

# 13. Checklist
- [ ] Comprendo flujo.
- [ ] Distingo display.
- [ ] Oculto correctamente.
- [ ] Evito position innecesario.

Continúa con Flexbox.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 14 — Tipografía y legibilidad](../unidad14-tipografia/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 16 — Flexbox](../unidad16-flexbox/README.md)
