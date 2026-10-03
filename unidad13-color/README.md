# Unidad 13 — Color, fondos y contraste

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Usar color dentro de un sistema visual sin convertirlo en el único canal de información.

# 1. Sintaxis

```css
color: #1f2937;
background-color: rgb(255 255 255);
border-color: hsl(220 10% 80%);
```

CSS moderno ofrece varias sintaxis. Elige una convención consistente.

# 2. Texto y fondo

`color` afecta texto/foreground.  
`background-color` pinta fondo.

El contraste depende de la combinación.

# 3. Contraste

No evalúes “se ve bien en mi monitor” como prueba.

Usa herramientas y revisa también estados interactivos.

# 4. Color no debe ser el único indicador

Un error no debería comunicarse únicamente volviendo un campo rojo.

Añade texto, icono u otra señal comprensible.

# 5. Texto sobre imagen

Si existe texto sobre fotografía/gradiente, comprueba contraste en distintas zonas y tamaños.

Un overlay puede ayudar, pero debe verificarse.

# 6. Bordes y sombras

Son herramientas visuales, no semánticas.

Una sombra no convierte un div en botón.

# 7. Tokens

```css
:root {
  --color-text: #1f2937;
  --color-surface: #fff;
  --color-danger: #b42318;
}
```

Permiten consistencia. Los profundizaremos en Unidad 22.

# 8. Tema oscuro

`prefers-color-scheme` puede ayudar a responder a preferencias.

No inviertas colores automáticamente sin revisar imágenes, bordes, sombras y contraste.

# 9. Práctica guiada

Diseña estados normal, información, éxito y error. Cada uno debe poder reconocerse sin depender solo del color.

# 10. Errores frecuentes
- contraste a ojo;
- rojo/verde como única señal;
- texto sobre imagen sin prueba;
- demasiados colores;
- dark mode como inversión automática.

# 11. Reto
Paleta pequeña con estados y comprobación de contraste.

# 12. Autoevaluación
1. ¿color vs background?
2. ¿Por qué no solo rojo/verde?
3. ¿Qué son tokens?
4. ¿Sombras añaden semántica?
5. ¿Dark mode es invertir colores?

# 13. Checklist
- [ ] Contraste.
- [ ] Señales redundantes.
- [ ] Paleta coherente.
- [ ] Estados accesibles.

Continúa con tipografía.


---

## Continuar el curso

- **Unidad anterior:** [Unidad 12 — Unidades, tamaños y límites](../unidad12-unidades/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 14 — Tipografía y legibilidad](../unidad14-tipografia/README.md)
