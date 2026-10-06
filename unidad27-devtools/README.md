# Unidad 27: DevTools, validación y depuración

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

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



## Laboratorio completo: Diagnóstico en DevTools

### Comprender antes de modificar

Diagnosticar consiste en reducir incertidumbre con evidencia. Si una regla no aparece, comprueba primero que el CSS se haya cargado. Si aparece pero no coincide, revisa selector y elemento. Si coincide y queda tachada, investiga cascada. Si gana pero el aspecto sigue inesperado, consulta valor computado y geometría.

Elements muestra el DOM interpretado, no necesariamente cada carácter del archivo original. Styles muestra declaraciones y permite cambios temporales; recargar suele perderlos. Para conservar una corrección debes editar el archivo del proyecto. Network muestra recursos bajo HTTP y ayuda a distinguir 404 de un problema de selector. El modelo de caja permite medir ancho/padding/borde sin adivinar. Console puede mostrar errores, pero la ausencia de errores no demuestra accesibilidad ni layout correcto.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

La nota tiene fondo claro. Puedes encontrar .tarjeta .nota en Styles, desactivar background y ver el cambio. Al recargar vuelve el estilo del archivo guardado.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Encontrar una regla</h1><article class="tarjeta"><h2>Laboratorio</h2><p class="nota">Este párrafo debe tener fondo claro.</p></article></main>
```

Las reglas específicas del tema son:

```css
.tarjeta { border: 2px solid #075985; padding: 1rem; }
.tarjeta .nota { background: #e0f2fe; padding: .5rem; }

```

### Experimento y explicación

Introduce de uno en uno tres fallos: ruta CSS incorrecta, clase nota escrita como notas y regla posterior que cambia background. Anota panel, evidencia y corrección para cada caso. Restaura antes de pasar al siguiente.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Corriges solo en Styles y cierras el navegador sin guardar el archivo.

**Cómo resolver:** Tras confirmar la hipótesis, aplica la modificación en styles.css, guarda y recarga. Comprueba que el resultado persiste con una carga nueva.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 26: Accesibilidad visual y estados](../unidad26-accesibilidad-css/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 28: Rendimiento web básico](../unidad28-rendimiento/README.md)
