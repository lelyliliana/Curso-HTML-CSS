# Unidad 24 — Transiciones y animaciones

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Añadir movimiento con propósito, distinguir transition/animation y respetar preferencias de reducción de movimiento.

# 1. Transition

Interpola cambios de propiedades entre estados.

```css
.button {
  transition:
    transform 180ms ease,
    background-color 180ms ease;
}

.button:hover {
  transform: translateY(-2px);
}
```

# 2. No uses transition: all

```css
transition: all .2s;
```

puede animar propiedades inesperadas.

Declara las que realmente deben transicionar.

# 3. Animation

```css
@keyframes pulse {
  from { opacity: .6; }
  to { opacity: 1; }
}
```

Permite secuencias autónomas/múltiples pasos.

No necesitas keyframes para un simple cambio hover.

# 4. Rendimiento

Transform y opacity suelen poder animarse eficientemente.

Animar layout (width, top, etc.) puede requerir más trabajo de layout/paint.

“Solo transform” tampoco es una regla absoluta; mide si el caso importa.

# 5. Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  .decorative-motion {
    animation: none;
    transition: none;
  }
}
```

La adaptación depende del efecto. Puedes reducir distancia/duración o reemplazar movimiento por cambio no espacial.

# 6. Movimiento con propósito

Útil para:
- feedback;
- relación entre estados;
- orientación espacial.

Evita movimiento constante que distrae sin aportar.

# 7. No bloquees interacción

Una animación no debería impedir que una persona use la interfaz durante segundos innecesarios.

# 8. Práctica guiada

Crea botón, disclosure visual y tarjeta con feedback. Después activa reduced motion en DevTools/SO y comprueba alternativa.

# 9. Errores frecuentes
- transition all;
- animación decorativa infinita;
- ignorar reduced motion;
- movimiento como única señal;
- animar propiedades costosas sin necesidad.

# 10. Reto
Microinteracción con versión completa y reducida, explicando qué información conserva.

# 11. Autoevaluación
1. ¿Transition vs animation?
2. ¿Por qué evitar all?
3. ¿Qué propiedades suelen ser eficientes?
4. ¿Reduced motion = borrar todo siempre?
5. ¿Movimiento debe aportar qué?

# 12. Checklist
- [ ] Movimiento con propósito.
- [ ] Propiedades explícitas.
- [ ] Reduced motion.
- [ ] Interacción no bloqueada.

Continúa con componentes.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 23 — Pseudoclases y pseudoelementos](../unidad23-pseudo/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 25 — Componentes y arquitectura CSS](../unidad25-componentes/README.md)
