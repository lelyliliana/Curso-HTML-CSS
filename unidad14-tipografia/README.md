# Unidad 14: Tipografía y legibilidad

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

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



## Laboratorio completo: Tipografía legible

### Comprender antes de modificar

La tipografía combina tamaño, altura de línea, longitud de línea, peso y espacio. Una fuente diferente no corrige párrafos demasiado largos o una altura insuficiente. Un line-height sin unidad multiplica el tamaño de fuente de cada elemento que lo hereda. Si heredaras una longitud fija en píxeles, un hijo con fuente grande podría conservar un interlineado demasiado pequeño.

La pila system-ui, sans-serif usa recursos disponibles en el sistema: el aspecto exacto varía entre Windows, Ubuntu y macOS, mientras que el contenido y la estructura se mantienen. No diseñes para que una línea termine siempre en una palabra concreta. Cuando uses una fuente web, verifica licencia, formatos, pesos y comportamiento de carga. Texto real con tildes, palabras largas y cantidades permite detectar problemas que no aparecen con dos palabras de muestra.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

La columna mantiene una longitud razonable en una pantalla amplia. La entrada es mayor que los párrafos. Al aumentar zoom, el contenido se reacomoda sin una altura fija que lo recorte.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main class="articulo"><h1>Leer antes de diseñar</h1><p class="entrada">Un sitio necesita contenido que pueda recorrerse con comodidad.</p><h2>Un ritmo consistente</h2><p>Los párrafos tienen una altura de línea suficiente y una longitud limitada. La fuente del sistema evita descargar archivos adicionales para este ejemplo.</p><p>Amplía el texto desde el navegador y observa si el contenido mantiene el orden y permite seguir leyendo.</p></main>
```

Las reglas específicas del tema son:

```css
.articulo { max-width: 65ch; margin-inline: auto; }
body { font-family: system-ui, sans-serif; font-size: 1rem; line-height: 1.6; }
h1, h2 { line-height: 1.2; }
.entrada { font-size: 1.25rem; }

```

### Experimento y explicación

Duplica la longitud de un párrafo, agrega una palabra larga y aumenta zoom a 200%. Compara line-height:1.6 con una longitud fija en un bloque que tiene dos tamaños de fuente.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Fijas una tarjeta a 100 px de alto y el texto ampliado queda cortado.

**Cómo resolver:** Usa altura automática y, si hace falta un mínimo visual, min-height. Prueba contenido variable antes de decidir límites.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 13: Color, fondos y contraste](../unidad13-color/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 15: Flujo normal y display](../unidad15-flujo-display/README.md)
