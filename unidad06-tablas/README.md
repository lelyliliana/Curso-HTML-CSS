# Unidad 06 — Tablas de datos

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


---

## Continuar el curso

- **Unidad anterior:** [Unidad 05 — HTML semántico](../unidad05-semantica/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 07 — Formularios](../unidad07-formularios/README.md)
