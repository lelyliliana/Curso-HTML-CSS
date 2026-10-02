# Unidad 14 — Tipografía y legibilidad

## Qué aprenderás
Construir jerarquía tipográfica, controlar longitud de línea y cargar fuentes sin sacrificar lectura o rendimiento.

# 1. Familia

```css
body {
  font-family: system-ui, sans-serif;
}
```

Incluye fallbacks.

# 2. Jerarquía

No necesitas diez tamaños. Define una escala pequeña para título, subtítulo, cuerpo y texto auxiliar.

La jerarquía también utiliza peso, espacio y posición.

# 3. line-height

```css
body {
  line-height: 1.6;
}
```

Un valor sin unidad escala con el tamaño de fuente y suele heredarse de forma útil.

# 4. Longitud de línea

```css
.prose {
  max-width: 65ch;
}
```

Las líneas extremadamente largas dificultan lectura.

No existe un número perfecto; valida según fuente y contenido.

# 5. Peso

No todas las fuentes incluyen todos los pesos.

Solicitar un peso ausente puede producir síntesis/interpolación según fuente/navegador.

# 6. letter-spacing

Úsalo con moderación. Aumentarlo en párrafos completos puede perjudicar lectura.

# 7. Fuentes web

Implican:
- descarga;
- peso;
- privacidad/proveedor;
- posibles cambios de layout.

Las fuentes del sistema pueden ser una excelente opción.

# 8. Autoalojadas

Con `@font-face`, declara archivos y pesos correctamente y considera `font-display`.

No uses el mismo archivo como si representara todos los pesos.

# 9. Práctica guiada

Diseña un artículo con escala, line-height, ancho de lectura y fallbacks. Prueba móvil y zoom 200%.

# 10. Errores frecuentes
- texto diminuto;
- líneas de pantalla completa;
- demasiadas familias;
- cargar pesos innecesarios;
- jerarquía solo por color.

# 11. Reto
Sistema tipográfico de cuatro roles con justificación y prueba a zoom.

# 12. Autoevaluación
1. ¿Por qué fallback?
2. ¿Qué aporta line-height sin unidad?
3. ¿Para qué ch?
4. ¿Más fuentes es mejor?
5. ¿Qué cuesta una webfont?

# 13. Checklist
- [ ] Jerarquía.
- [ ] Lectura cómoda.
- [ ] Fallbacks.
- [ ] Carga razonable.

Continúa con flujo.
