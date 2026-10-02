# Unidad 12 — Unidades, tamaños y límites

## Qué aprenderás
Elegir unidades relativas/absolutas y crear tamaños fluidos sin impedir zoom ni adaptación.

# 1. px

CSS px es una unidad de referencia, no necesariamente un píxel físico de pantalla.

Útil para bordes/detalles y también puede usarse en otros contextos, pero no conviertas todo el diseño en dimensiones rígidas.

# 2. rem

```css
padding: 1rem;
```

Se basa en el tamaño de fuente del elemento raíz.

Es útil para escalas coherentes que respondan a preferencias/configuración del usuario.

# 3. em

Depende del tamaño de fuente del elemento (o del contexto de la propiedad).

Puede ser útil cuando un componente debe escalar consigo mismo, pero el anidamiento puede sorprender.

# 4. Porcentajes

Su referencia depende de la propiedad/contexto.

`width:50%` suele depender del bloque contenedor; otros porcentajes tienen reglas distintas.

No memorices “% = padre” para todo.

# 5. Viewport

`vw`, `vh` y unidades modernas como `dvh`, `svh`, `lvh` ayudan con viewport móvil y barras dinámicas.

No uses 100vh por reflejo cuando la UI móvil requiera otra semántica.

# 6. ch

Aproxima el ancho del carácter "0" de la fuente.

Útil para limitar líneas de texto:

```css
.prose {
  max-width: 65ch;
}
```

# 7. min/max/clamp

```css
.container {
  width: min(100% - 2rem, 70rem);
}
```

```css
h1 {
  font-size: clamp(2rem, 5vw, 4rem);
}
```

`clamp(min, preferido, max)`.

# 8. Texto y zoom

No desactives zoom mediante viewport.

Usa tamaños/containers que puedan adaptarse cuando el usuario aumenta texto o zoom.

# 9. Práctica guiada

Construye:
- container fluido;
- ancho de lectura 65ch;
- heading con clamp;
- espacio con rem.

Prueba 320px y zoom 200%.

# 10. Errores frecuentes
- todo px rígido;
- 100vw generando overflow con scrollbar;
- 100vh sin considerar móvil;
- em anidado sin comprender;
- viewport que bloquea zoom.

# 11. Reto
Layout fluido sin media query que mantenga límites legibles.

# 12. Autoevaluación
1. ¿px = píxel físico?
2. ¿rem depende de qué?
3. ¿em?
4. ¿% siempre padre?
5. ¿Qué hace clamp?
6. ¿Por qué dvh?

# 13. Checklist
- [ ] Elijo unidad con criterio.
- [ ] Uso límites fluidos.
- [ ] Pruebo zoom.
- [ ] Evito rigidez innecesaria.

Continúa con color.
