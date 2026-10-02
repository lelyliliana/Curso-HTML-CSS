# Unidad 10 — Selectores y especificidad

## Qué aprenderás
Seleccionar elementos sin acoplar el CSS innecesariamente al HTML y razonar sobre especificidad.

# 1. Selectores básicos

```css
p {}
.card {}
#principal {}
[data-state="active"] {}
```

Tipo, clase, id y atributo expresan criterios distintos.

Para estilos reutilizables, las clases suelen ser una base predecible.

# 2. Combinadores

Descendiente:
```css
.card p {}
```

Hijo directo:
```css
.card > p {}
```

Hermano adyacente:
```css
h2 + p {}
```

Usa el selector que represente la relación necesaria, no uno más profundo “para asegurar”.

# 3. Especificidad

Modelo práctico:
- IDs pesan más que clases/atributos/pseudoclases;
- clases pesan más que tipos/pseudoelementos;
- el orden decide cuando la prioridad/especificidad relevante empata.

No conviertas esto en una carrera de números.

# 4. Ejemplo

```css
a { color: blue; }
.nav__link { color: green; }
#principal a { color: red; }
```

El id hace muy difícil sobrescribir el estilo de forma reutilizable.

Por eso no se recomienda usar IDs como herramienta habitual de styling.

# 5. Clases de componente

```css
.card {}
.card__title {}
.card--featured {}
```

Es una convención posible para nombres predecibles. No necesitas adoptar BEM completo para beneficiarte de clases explícitas.

# 6. Selectores profundos

```css
main .page .content article .card h3 span {}
```

Se rompe cuando cambia la estructura y acumula especificidad.

Mejor, cuando el elemento tiene un rol reutilizable:

```css
.card__label {}
```

# 7. :where e :is

CSS moderno ofrece `:where()` con especificidad cero para el selector funcional y `:is()` con reglas propias de especificidad.

Son útiles para APIs de estilos, pero no sustituyen comprender lo básico.

# 8. Práctica guiada

Refactoriza un selector de cinco niveles a clases de componente. Cambia el HTML interno y comprueba cuál versión resiste mejor.

# 9. Errores frecuentes
- IDs para ganar;
- selectores demasiado profundos;
- !important como parche;
- clase ligada a apariencia como `.texto-rojo-18px` cuando debería expresar rol;
- selector universal indiscriminado para estilos costosos/inesperados.

# 10. Reto
Diseña estilos de tarjeta que puedan reutilizarse en dos secciones sin aumentar especificidad.

# 11. Autoevaluación
1. ¿Clase vs id?
2. ¿Qué hace >?
3. ¿Por qué selector profundo acopla?
4. ¿Qué ocurre si empata especificidad?
5. ¿Para qué puede servir :where?

# 12. Checklist
- [ ] Selectores claros.
- [ ] Especificidad baja/predecible.
- [ ] Evito profundidad.
- [ ] Reutilizo componentes.

Continúa con box model.
