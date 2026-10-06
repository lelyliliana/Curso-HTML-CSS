# Unidad 09: CSS, cascada e herencia

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Conectar CSS, comprender cómo el navegador decide qué declaración gana y diagnosticar estilos sin recurrir a !important.

# 1. Regla CSS

```css
h1 {
  font-size: 2rem;
  color: #222;
}
```

- selector: `h1`;
- propiedades: `font-size`, `color`;
- valores: `2rem`, `#222`.

# 2. CSS externo

```html
<link rel="stylesheet" href="css/styles.css">
```

Comprueba en Network que realmente cargó. Si no aparece, ningún cambio dentro del archivo podrá verse.

# 3. La cascada

Cuando varias declaraciones compiten por la misma propiedad del mismo elemento, el navegador considera factores como:

- origen;
- importancia;
- capas de cascada cuando se usan;
- especificidad;
- proximidad/orden dentro de las reglas aplicables.

“Gana la última regla” solo es cierto cuando los demás factores relevantes empatan.

# 4. Ejemplo

```css
p { color: blue; }
.aviso { color: red; }
```

```html
<p class="aviso">Atención</p>
```

La clase tiene mayor especificidad que el selector de tipo, por lo que rojo gana aunque el orden pueda variar en este caso.

# 5. Herencia

Propiedades como `color` y varias tipográficas suelen heredarse.

```css
body {
  color: #222;
}
```

Los descendientes pueden recibir ese valor si no existe otra declaración aplicable.

Propiedades como `margin` normalmente no se heredan.

# 6. Valor declarado, cascaded y computed

DevTools puede mostrar:

- reglas tachadas;
- origen;
- valor computado.

No mires solo tu archivo: mira qué valor terminó usando el navegador.

# 7. !important

```css
color: red !important;
```

cambia la prioridad dentro de la cascada.

No es “más CSS”. Puede ser útil en casos concretos, pero usarlo para resolver cada conflicto crea una escalada difícil de mantener.

# 8. Cascade layers

CSS moderno permite ordenar grupos mediante `@layer`.

Son útiles en sistemas grandes, frameworks o estilos por capas, pero primero domina la cascada normal.

# 9. Práctica guiada

Crea tres reglas que afecten el mismo párrafo:

- tipo;
- clase;
- clase posterior.

Antes de abrir navegador, predice el resultado. Después comprueba en DevTools.

# 10. Errores frecuentes

- añadir !important sin investigar;
- creer que siempre gana lo último;
- pensar que toda propiedad se hereda;
- editar CSS que no está cargado;
- aumentar especificidad como solución permanente.

# 11. Reto
Recibe un elemento con cinco reglas competidoras y explica exactamente por qué cada propiedad termina con su valor final.

# 12. Autoevaluación

1. ¿Qué es selector?
2. ¿Siempre gana última regla?
3. ¿Color puede heredarse?
4. ¿Margin suele heredarse?
5. ¿Para qué sirve DevTools?
6. ¿Por qué evitar guerras de !important?

# 13. Checklist

- [ ] Enlazo CSS.
- [ ] Predigo cascada.
- [ ] Distingo herencia.
- [ ] Diagnostico en DevTools.

Continúa con selectores.



## Laboratorio completo: Cascada observable

### Comprender antes de modificar

La cascada selecciona declaraciones considerando origen, importancia y capas antes de comparar especificidad y orden dentro del contexto correspondiente. En este ejemplo todas las declaraciones son reglas normales del autor, sin capas: podemos estudiar especificidad y orden sin introducir otras prioridades.

.aviso y .destacado tienen la misma especificidad. Las dos reglas .aviso compiten por color y gana la posterior. El primer párrafo también coincide con .destacado, cuya declaración aparece después. CSS no elige un bloque entero: cada propiedad compite por separado. El background de .aviso se conserva porque .destacado no define fondo. El valor computado es el resultado utilizado tras resolver declaraciones; el panel Styles permite ver cuáles fueron descartadas. Cambiar la clase en HTML o aumentar la especificidad altera qué candidatos compiten.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

El primer aviso es rojizo y el segundo verde, ambos con fondo claro. En Styles, la primera declaración color de .aviso está tachada. En Computed puedes consultar el color final.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Cascada</h1><p class="aviso destacado">El aviso tiene dos clases.</p><p class="aviso">Este aviso tiene una clase.</p></main>
```

Las reglas específicas del tema son:

```css
.aviso { color: #075985; background: #f0f9ff; padding: 1rem; }
.aviso { color: #166534; }
.destacado { color: #9f1239; }

```

### Experimento y explicación

Mueve .destacado antes de las dos reglas .aviso y predice el color del primer párrafo. Añade luego .aviso.destacado con otro color. Explica ambos resultados sin usar !important.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Agregas !important porque no sabes qué selector está ganando.

**Cómo resolver:** Inspecciona el elemento, comprueba coincidencias y orden, y elimina conflictos innecesarios. Una regla con !important añade otra prioridad y puede hacer más difícil diagnosticar la siguiente modificación.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 08: Accesibilidad HTML](../unidad08-accesibilidad/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 10: Selectores y especificidad](../unidad10-selectores/README.md)
