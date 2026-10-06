# Unidad 16: Flexbox

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Distribuir ítems en un eje principal, controlar alineación y comprender grow, shrink, basis y wrap.

# 1. Contenedor e ítems

```css
.toolbar {
  display: flex;
}
```

`.toolbar` es **flex container**.

Sus hijos directos se convierten en **flex items**.

Una propiedad como `justify-content` va normalmente en el contenedor, no en cada hijo.

# 2. Ejes

Con:

```css
flex-direction: row;
```

main axis suele ser horizontal en escritura izquierda→derecha.

cross axis es perpendicular.

Si cambias a column, los ejes cambian.

No memorices “justify = horizontal”.

# 3. justify-content

Distribuye ítems a lo largo del **main axis**.

# 4. align-items

Alinea ítems en el **cross axis** dentro de la línea.

# 5. gap

```css
display: flex;
gap: 1rem;
```

Crea espacio entre ítems sin márgenes laterales manuales.

# 6. flex-wrap

```css
flex-wrap: wrap;
```

Permite crear múltiples líneas cuando no cabe.

Si existe wrap, `align-content` puede distribuir líneas cuando hay espacio adicional en cross axis.

# 7. flex shorthand

```css
.item {
  flex: 1 1 15rem;
}
```

Conceptualmente:

- grow: crecer;
- shrink: encoger;
- basis: tamaño base.

No memorices `flex:1` sin comprender qué comportamiento necesitas.

# 8. min-width:auto

Los flex items pueden negarse a encogerse por su tamaño mínimo intrínseco.

En algunos layouts:

```css
.item {
  min-width: 0;
}
```

permite que contenido se encoja/trunque según diseño.

Úsalo después de diagnosticar, no como reset universal.

# 9. Auto margins

```css
.login {
  margin-inline-start: auto;
}
```

Puede empujar un ítem consumiendo espacio libre en el eje principal.

# 10. Orden visual

`order` puede cambiar visualmente el orden sin cambiar DOM.

Eso puede crear diferencias con navegación por teclado/lectores.

No lo uses para corregir una estructura HTML incorrecta.

# 11. Práctica guiada

Construye:

- barra con logo/nav/acción;
- grupo de botones;
- tarjetas que envuelvan.

Cambia row→column y predice justify/align.

# 12. Errores frecuentes

- justify = horizontal siempre;
- propiedades del contenedor en hijos;
- flex:1 sin entender;
- order para arreglar DOM;
- overflow por min-width intrínseco.

# 13. Reto
Componente de tarjetas flexible desde móvil a escritorio usando wrap y tamaños intrínsecos.

# 14. Autoevaluación

1. ¿Quién es flex container?
2. ¿Quiénes son items?
3. ¿Qué eje usa justify?
4. ¿Qué cambia con column?
5. ¿Qué hace wrap?
6. ¿Por qué order puede afectar accesibilidad?

# 15. Checklist

- [ ] Distingo container/item.
- [ ] Comprendo ejes.
- [ ] Uso gap/wrap.
- [ ] Comprendo flex shorthand.
- [ ] Mantengo orden lógico.

Continúa con Grid.



## Laboratorio completo: Flexbox para componentes

### Comprender antes de modificar

Flexbox distribuye hijos directos en un eje principal y uno transversal. Con flex-direction:row, justify-content actúa sobre el eje principal y align-items sobre el transversal. Cambiar a column cambia cómo se interpretan esos ejes: no memorices justify como horizontal en cualquier caso.

flex-wrap permite varias líneas cuando el espacio no alcanza. Cada línea flex distribuye su propio espacio, a diferencia de una cuadrícula que coordina filas y columnas. gap separa elementos sin márgenes de compensación. flex:1 no significa exactamente un tercio visible sin considerar base, mínimos, contenido y separación. Los elementos pueden conservar un mínimo intrínseco que impida encoger; min-width:0 puede ser necesario para un hijo con contenido largo. No uses order para crear un recorrido visual diferente al orden de lectura y teclado.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Los enlaces forman una fila mientras caben y pasan a otra línea al reducir espacio. El orden sigue siendo Guía, Taller, Proyecto tanto visualmente como con Tab.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Barra de recursos</h1><nav class="barra" aria-label="Recursos"><a href="#guia">Guía</a><a href="#taller">Taller</a><a href="#proyecto">Proyecto</a></nav><section id="guia"><h2>Guía</h2><p>Lee los conceptos.</p></section><section id="taller"><h2>Taller</h2><p>Practica.</p></section><section id="proyecto"><h2>Proyecto</h2><p>Integra.</p></section></main>
```

Las reglas específicas del tema son:

```css
.barra { display: flex; flex-wrap: wrap; gap: .75rem; align-items: center; }
.barra a { padding: .5rem 1rem; border: 2px solid #075985; }

```

### Experimento y explicación

Agrega un enlace de texto largo con destino válido. Compara flex-wrap:wrap y nowrap. Cambia flex-direction a column y prueba align-items:flex-start frente a stretch.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Añades order:-1 al último enlace para que parezca primero.

**Cómo resolver:** Si la prioridad realmente cambia, cambia el orden del HTML. order solo cambia presentación y puede desconectar la secuencia visual del teclado.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 15: Flujo normal y display](../unidad15-flujo-display/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 17: CSS Grid](../unidad17-grid/README.md)
