# Unidad 23: Pseudoclases y pseudoelementos

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Diseñar estados interactivos y contenido decorativo sin confundir estado, estructura y accesibilidad.

# 1. Pseudoclase

Selecciona un estado/condición:

```css
a:hover {}
button:focus-visible {}
input:checked {}
button:disabled {}
```

No crea un elemento nuevo.

# 2. Hover no basta

Touch puede no tener hover equivalente.

Si información o acción solo aparece al hover, parte de las personas no podrá acceder.

Diseña también foco, estado persistente o interacción explícita.

# 3. focus-visible

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

Permite indicador de foco cuando el navegador determina que es apropiado, especialmente navegación por teclado.

No elimines outline sin alternativa.

# 4. Estados de formulario

```css
input:invalid {}
input:disabled {}
input:checked {}
```

El estado visual debe acompañar, no reemplazar, mensajes/semántica.

# 5. Estructurales

```css
li:nth-child(odd) {}
```

Selecciona según posición estructural.

Si el diseño depende de que “el tercer elemento siempre sea especial”, revisa si una clase semántica sería más estable.

# 6. :has

```css
.field:has(input:invalid) {}
```

Permite seleccionar un elemento según descendientes/relaciones.

Comprueba soporte requerido y no escondas lógica esencial difícil de entender.

# 7. Pseudoelementos

```css
.badge::before {
  content: "";
}
```

Útiles para decoración.

No pongas información esencial únicamente en `content` generado por CSS.

# 8. ::selection

Puede personalizar selección, manteniendo contraste.

# 9. Práctica guiada

Botón/enlace/campo con:

- default;
- hover;
- focus-visible;
- disabled;
- invalid/selected cuando corresponda.

Prueba mouse, teclado y touch conceptual.

# 10. Errores frecuentes

- solo hover;
- quitar focus;
- contenido esencial en ::before;
- nth-child frágil;
- disabled que parece habilitado.

# 11. Reto
Componente interactivo cuyos estados sean distinguibles sin depender solo de color.

# 12. Autoevaluación

1. ¿Pseudo-clase crea elemento?
2. ¿Hover existe siempre?
3. ¿Para qué focus-visible?
4. ¿Qué hace :has?
5. ¿Información esencial en ::before?

# 13. Checklist

- [ ] Estados completos.
- [ ] Foco visible.
- [ ] Touch considerado.
- [ ] Pseudoelementos decorativos.

Continúa con animaciones.



## Laboratorio completo: Estados y pseudoclases

### Comprender antes de modificar

Una pseudoclase selecciona estados o relaciones, como :hover, :focus-visible o :nth-child. Un pseudoelemento selecciona una parte generada o representada, como ::marker. El estado hover depende del dispositivo y no debe ser el único modo de acceder a contenido importante. El foco aparece al navegar y debe poder reconocerse sin necesitar el mouse.

:nth-child cuenta posiciones entre hermanos, no solo entre elementos de una clase concreta. Añadir otro hijo puede cambiar las coincidencias. ::before y ::after pueden aportar decoración, pero no son una buena ubicación para instrucciones esenciales, ya que su exposición y comportamiento no sustituyen contenido HTML real. Una clase .seleccionado no equivale automáticamente a estado accesible: si existe un control seleccionable, su semántica y comportamiento deben comunicarlo.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Hover cambia el fondo del enlace y Tab muestra un contorno distinto. Las filas primera y tercera tienen fondo claro. Los marcadores conservan su función de lista.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Estados visibles</h1><p><a class="enlace" href="#contenido">Abrir el contenido</a></p><section id="contenido"><h2>Contenido</h2><p>Usa mouse y teclado para comparar los estados.</p></section><ul class="lista"><li>Leer</li><li>Practicar</li><li>Revisar</li></ul></main>
```

Las reglas específicas del tema son:

```css
.enlace { display: inline-block; padding: .5rem; border: 2px solid #075985; }
.enlace:hover { background: #e0f2fe; }
.enlace:focus-visible { outline: 3px solid #9f1239; outline-offset: 4px; }
.lista li:nth-child(odd) { background: #f0f9ff; }
.lista li::marker { color: #075985; }

```

### Experimento y explicación

Añade una cuarta fila y predice cuáles recibirán fondo. Recorre el enlace con teclado y confirma que su foco no depende de hover. Explica cuándo usarías contenido HTML en lugar de ::before.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Eliminas outline para que el borde de foco no cambie el diseño.

**Cómo resolver:** Conserva una señal de foco visible y contrastada. outline no ocupa espacio en la caja como border y puede separarse mediante outline-offset.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 22: Variables CSS y funciones](../unidad22-variables/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 24: Transiciones y animaciones](../unidad24-animaciones/README.md)
