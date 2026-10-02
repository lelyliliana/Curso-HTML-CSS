# Unidad 26 — Accesibilidad visual y estados

## Qué aprenderás
Comprobar foco, contraste, reflow, preferencias y estados interactivos desde la capa CSS.

# 1. Foco visible

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

No elimines outline sin un reemplazo visible y suficiente.

# 2. Contraste de estados

No compruebes solo texto normal.

Revisa:
- enlaces;
- placeholder cuando sea relevante;
- bordes necesarios para identificar controles;
- focus;
- hover;
- disabled;
- error.

# 3. Color

Error, éxito, selección y estado no deben depender únicamente del color.

CSS puede reforzar iconos, bordes y texto, pero HTML debe contener la información esencial.

# 4. Zoom y reflow

Prueba:
- zoom 200%;
- viewport estrecho;
- aumento de texto cuando el entorno lo permita.

Busca:
- texto cortado;
- controles superpuestos;
- scroll horizontal general;
- contenido oculto.

# 5. Unidades y texto

Evita alturas fijas para cajas con texto:

```css
.card {
  height: 120px;
}
```

puede romperse al aumentar texto.

Prefiere contenido que determine altura o usa min-height cuando exista un mínimo real.

# 6. Reduced motion

Respeta `prefers-reduced-motion` en movimientos que puedan afectar a usuarios.

# 7. Forced colors / alto contraste

Sistemas pueden usar modos de colores forzados.

Evita depender de fondos/imágenes para comunicar estados sin alternativa.

Puedes probar `forced-colors` si tu alcance lo requiere.

# 8. Ocultar contenido

`display:none` no es una técnica de “solo visual”.

Usa patrón visually-hidden cuando contenido debe seguir disponible a lectores de pantalla.

# 9. Orden visual

Flex/Grid pueden cambiar presentación, pero evita una secuencia visual que contradiga el DOM/foco.

# 10. Práctica guiada

Audita componentes de Unidad 25:
1. teclado;
2. foco;
3. contraste;
4. zoom;
5. viewport estrecho;
6. reduced motion;
7. estado disabled/error.

Documenta barrera→corrección→verificación.

# 11. Errores frecuentes
- outline:none;
- altura fija con texto;
- contraste solo del body;
- color como único estado;
- orden visual distinto del teclado;
- reduced motion ignorado.

# 12. Reto
Corrige una biblioteca de componentes hasta que funcione con teclado, zoom y preferencias de movimiento.

# 13. Autoevaluación
1. ¿Por qué focus visible?
2. ¿Qué probar además de texto normal?
3. ¿Altura fija y zoom?
4. ¿Display none sirve para screen-reader-only?
5. ¿Orden visual puede diferir del foco?
6. ¿Qué hace reduced motion?

# 14. Checklist
- [ ] Foco.
- [ ] Contraste.
- [ ] Reflow.
- [ ] Estados redundantes.
- [ ] Preferencias respetadas.

Continúa con calidad y publicación.
