# Unidad 06: Tablas de datos

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Representar relaciones tabulares, identificar encabezados y hacer tablas comprensibles y adaptables.

# 1. Cuándo tabla

Una tabla sirve cuando los datos tienen relaciones por filas/columnas.

No la uses para colocar logo a la izquierda y menú a la derecha.

# 2. Estructura

```html
<table>
  <caption>Ventas mensuales</caption>
  <thead>
    <tr>
      <th scope="col">Mes</th>
      <th scope="col">Ventas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Enero</th>
      <td>120</td>
    </tr>
  </tbody>
</table>
```

# 3. caption

Identifica el propósito de la tabla.

No lo reemplaces únicamente por un párrafo visualmente cercano si el caption pertenece semánticamente a la tabla.

# 4. th y scope

`th` representa encabezado.

`scope="col"` o `scope="row"` ayuda a expresar asociación en tablas sencillas.

Tablas complejas pueden requerir técnicas adicionales.

# 5. thead/tbody/tfoot

Agrupan filas por función.

No cambian por sí solos la apariencia.

# 6. celdas combinadas

`colspan`/`rowspan` pueden representar estructuras reales, pero complican comprensión/accesibilidad.

No los uses para maquetar.

# 7. Responsive

Una tabla ancha puede necesitar:

- contenedor con overflow horizontal;
- priorización/replanteamiento del contenido.

No conviertas automáticamente cada fila en “tarjeta” si se pierde la relación tabular.

# 8. Práctica guiada

Construye tabla de calificaciones con encabezados de estudiante y actividad. Navega conceptualmente: ¿qué encabezados describen cada dato?

# 9. Errores frecuentes

- tabla para layout;
- td usado como encabezado;
- caption ausente cuando aporta;
- scope incorrecto;
- responsive que destruye relaciones.

# 10. Reto
Tabla con encabezados de fila/columna y estrategia móvil que preserve significado.

# 11. Autoevaluación

1. ¿Cuándo tabla?
2. ¿th vs td?
3. ¿Qué hace scope?
4. ¿thead da estilo?
5. ¿Tabla ancha debe convertirse siempre en cards?

# 12. Checklist

- [ ] Datos realmente tabulares.
- [ ] Encabezados correctos.
- [ ] Caption útil.
- [ ] Adaptación sin perder significado.

Continúa con formularios.



## Laboratorio completo: Tabla de horarios

### Comprender antes de modificar

Una tabla representa datos relacionados por filas y columnas. Si solo necesitas poner una foto junto a un párrafo, esa relación visual no convierte el contenido en datos tabulares. caption nombra el conjunto de datos. th marca encabezados y scope explicita si describen columna o fila en una tabla sencilla.

En el ejemplo, Taller es encabezado de columna y Lectura es encabezado de su fila. Una persona puede relacionar el día y la hora con el taller correspondiente. thead y tbody organizan grupos, pero no sustituyen th ni las asociaciones. Para tablas complejas con encabezados multinivel se requieren asociaciones más elaboradas; conviene simplificar cuando sea posible. Las líneas de borde son CSS, no el significado de la tabla. No agregues celdas vacías para simular márgenes.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Hay tres columnas y dos filas de datos. El caption aparece antes de la tabla. Lectura y Robótica son encabezados de fila; Martes y 15:00 son datos.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Horarios de talleres</h1>
<table><caption>Talleres disponibles (hora local)</caption><thead><tr><th scope="col">Taller</th><th scope="col">Día</th><th scope="col">Hora</th></tr></thead>
<tbody><tr><th scope="row">Lectura</th><td>Martes</td><td>15:00</td></tr><tr><th scope="row">Robótica</th><td>Jueves</td><td>16:00</td></tr></tbody></table>
</main>
```

Las reglas específicas del tema son:

```css
table { border-collapse: collapse; } th, td { border: 1px solid #64748b; padding: .5rem; } caption { font-weight: bold; text-align: left; }
```

### Experimento y explicación

Agrega un taller de arte el sábado a las 10:00 y verifica que todas las filas tengan tres celdas. Añade una frase que explique el horario para quien no necesita revisar cada celda.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Se usa td en todos los encabezados porque la negrita se obtiene con CSS.

**Cómo resolver:** Sustituye las celdas que nombran filas/columnas por th y añade scope. La apariencia en negrita no crea asociaciones semánticas.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 05: HTML semántico](../unidad05-semantica/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 07: Formularios](../unidad07-formularios/README.md)
