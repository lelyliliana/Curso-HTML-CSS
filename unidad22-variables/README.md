# Unidad 22 — Variables CSS y funciones

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Crear tokens con custom properties, comprender alcance/herencia y combinar calc, min, max y clamp.

# 1. Custom property

```css
:root {
  --space-1: .5rem;
  --space-2: 1rem;
  --radius: .75rem;
}
```

Uso:

```css
.card {
  padding: var(--space-2);
  border-radius: var(--radius);
}
```

# 2. Son parte de la cascada

Las custom properties heredan y pueden sobrescribirse por contexto.

```css
.theme-dark {
  --surface: #111;
  --text: #fff;
}
```

Los descendientes usan los nuevos valores.

# 3. Fallback

```css
color: var(--text-color, #222);
```

El fallback se usa si la custom property no está definida/usable según reglas de var.

No sustituye un sistema de tokens bien definido.

# 4. Token semántico

Mejor:
```css
--color-danger
--surface-card
```

que:
```css
--red
--white-box
```

cuando el valor puede cambiar de tema.

# 5. calc

```css
width: calc(100% - 2rem);
```

Combina unidades compatibles bajo reglas CSS.

# 6. min/max

```css
width: min(100% - 2rem, 70rem);
```

Escoge el menor resultado.

# 7. clamp

```css
font-size: clamp(2rem, 4vw + 1rem, 4rem);
```

Define mínimo, valor preferido y máximo.

# 8. Tokens no son variables Sass

Las custom properties existen en tiempo de ejecución del navegador y participan en cascada/herencia.

Esto permite temas/contextos dinámicos sin recompilar CSS.

# 9. Práctica guiada

Extrae de una página:
- espacios;
- radios;
- superficies;
- texto;
- acento.

Crea tokens semánticos y un segundo tema.

# 10. Errores frecuentes
- variable para cada literal sin sistema;
- nombres ligados a color actual;
- no comprender alcance;
- calc innecesario;
- clamp con valores que no producen transición útil.

# 11. Reto
Sistema pequeño de tokens con tema alternativo sin duplicar componentes.

# 12. Autoevaluación
1. ¿Custom property hereda?
2. ¿Qué hace var fallback?
3. ¿Token semántico?
4. ¿calc para qué?
5. ¿Qué hace clamp?
6. ¿Custom property existe solo al compilar?

# 13. Checklist
- [ ] Tokens con significado.
- [ ] Comprendo alcance.
- [ ] Uso funciones fluidas.
- [ ] Evito duplicación de tema.

Continúa con pseudoclases.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 21 — Imágenes responsive](../unidad21-imagenes-responsive/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 23 — Pseudoclases y pseudoelementos](../unidad23-pseudo/README.md)
