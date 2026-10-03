# Unidad 23 — Pseudoclases y pseudoelementos

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Diseñar estados interactivos y contenido decorativo sin confundir estado, estructura y accesibilidad.

# 1. Pseudoclase

Selecciona un estado/condición:

```css
a:hover {}
button:focus-visible {}
input:checked {}
button:disabled {}
```

No crea un elemento nuevo.

# 2. Hover no basta

Touch puede no tener hover equivalente.

Si información o acción solo aparece al hover, parte de las personas no podrá acceder.

Diseña también foco, estado persistente o interacción explícita.

# 3. focus-visible

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

Permite indicador de foco cuando el navegador determina que es apropiado, especialmente navegación por teclado.

No elimines outline sin alternativa.

# 4. Estados de formulario

```css
input:invalid {}
input:disabled {}
input:checked {}
```

El estado visual debe acompañar, no reemplazar, mensajes/semántica.

# 5. Estructurales

```css
li:nth-child(odd) {}
```

Selecciona según posición estructural.

Si el diseño depende de que “el tercer elemento siempre sea especial”, revisa si una clase semántica sería más estable.

# 6. :has

```css
.field:has(input:invalid) {}
```

Permite seleccionar un elemento según descendientes/relaciones.

Comprueba soporte requerido y no escondas lógica esencial difícil de entender.

# 7. Pseudoelementos

```css
.badge::before {
  content: "";
}
```

Útiles para decoración.

No pongas información esencial únicamente en `content` generado por CSS.

# 8. ::selection

Puede personalizar selección, manteniendo contraste.

# 9. Práctica guiada

Botón/enlace/campo con:
- default;
- hover;
- focus-visible;
- disabled;
- invalid/selected cuando corresponda.

Prueba mouse, teclado y touch conceptual.

# 10. Errores frecuentes
- solo hover;
- quitar focus;
- contenido esencial en ::before;
- nth-child frágil;
- disabled que parece habilitado.

# 11. Reto
Componente interactivo cuyos estados sean distinguibles sin depender solo de color.

# 12. Autoevaluación
1. ¿Pseudo-clase crea elemento?
2. ¿Hover existe siempre?
3. ¿Para qué focus-visible?
4. ¿Qué hace :has?
5. ¿Información esencial en ::before?

# 13. Checklist
- [ ] Estados completos.
- [ ] Foco visible.
- [ ] Touch considerado.
- [ ] Pseudoelementos decorativos.

Continúa con animaciones.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 22 — Variables CSS y funciones](../unidad22-variables/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 24 — Transiciones y animaciones](../unidad24-animaciones/README.md)
