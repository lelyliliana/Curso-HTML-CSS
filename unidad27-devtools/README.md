# Unidad 27 — DevTools, validación y depuración

## Qué aprenderás
Diagnosticar HTML/CSS con evidencia, distinguir errores de estructura/estilo/recurso y validar sin editar a ciegas.

# 1. Método

```text
síntoma → hipótesis → evidencia → cambio mínimo → comprobar
```

No cambies cinco propiedades simultáneamente.

# 2. Elements

Inspecciona el DOM que realmente construyó el navegador.

Comprueba:
- clases;
- atributos;
- jerarquía;
- elementos generados/normalizados.

# 3. Styles

Una propiedad tachada indica que otra regla/condición ganó o que no aplica.

Mira:
- selector;
- archivo/línea;
- especificidad;
- media query;
- herencia.

# 4. Computed

Muestra el valor final computado.

Si esperabas 16px y ves 24px, rastrea de dónde procede.

# 5. Box model

DevTools muestra content/padding/border/margin.

Úsalo para explicar tamaño antes de cambiar width al azar.

# 6. Layout tools

Navegadores modernos pueden superponer:
- Grid;
- Flex;
- gaps;
- tracks.

Actívalos para ver ejes/espacio.

# 7. Network

Comprueba:
- 404;
- tamaño;
- caché;
- tipo;
- tiempo;
- recurso realmente descargado.

Es fundamental para imágenes responsive y fuentes.

# 8. Console

Aunque el curso no usa JavaScript como núcleo, la consola puede mostrar problemas de recursos, políticas o navegador.

# 9. Accessibility tree

El inspector de accesibilidad permite revisar roles/nombres/estados calculados.

No sustituye prueba con teclado/lector.

# 10. Validación

Un validador HTML/CSS puede detectar errores sintácticos/estructurales.

Una página válida puede seguir siendo inaccesible o tener mal diseño.

Validación ≠ calidad total.

# 11. Responsive mode

Simula tamaños/DPR/touch en cierta medida.

No reemplaza completamente navegador/dispositivo real cuando el proyecto lo requiere.

# 12. Práctica guiada

Provoca:
1. CSS 404;
2. especificidad;
3. overflow;
4. alt/nombre incorrecto;
5. imagen enorme.

Diagnostica cada uno sin editar primero.

# 13. Reto
Bitácora de cinco fallos con síntoma, hipótesis, evidencia, corrección y verificación.

# 14. Autoevaluación
1. ¿Styles vs Computed?
2. ¿Para qué Box Model?
3. ¿Qué muestra Network?
4. ¿Validador garantiza accesibilidad?
5. ¿Responsive mode reemplaza dispositivo real?

# 15. Checklist
- [ ] Diagnostico antes de editar.
- [ ] Uso panel correcto.
- [ ] Valido.
- [ ] Registro evidencia.

Continúa con rendimiento.
