# Unidad 08: Accesibilidad HTML

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Evaluar una página con semántica, teclado, nombres accesibles y alternativas antes de depender de ARIA.

# 1. Accesibilidad no es una etapa final

Una página accesible comienza con HTML correcto:

- headings;
- landmarks;
- enlaces;
- botones;
- labels;
- alt;
- idioma.

Corregir todo al final suele ser más difícil.

# 2. Teclado

Prueba:

- Tab;
- Shift+Tab;
- Enter;
- Space donde corresponda.

Pregunta:

- ¿puedo alcanzar controles?
- ¿sé dónde está el foco?
- ¿el orden tiene sentido?
- ¿puedo activar?

# 3. Botón vs enlace

**Enlace:** navega.  
**Botón:** ejecuta una acción.

No uses `<div onclick>` para recrear un botón si existe `<button>`.

# 4. Nombre accesible

Un control necesita un nombre comprensible.

Puede venir de:

- texto;
- label;
- alt en ciertos contextos;
- aria-label/labelledby cuando realmente es necesario.

# 5. ARIA

Regla útil:
> HTML nativo primero.

ARIA puede añadir semántica/estado, pero no añade automáticamente comportamiento de teclado.

`role="button"` en un div no lo convierte mágicamente en un botón completo.

# 6. Encabezados

Usa jerarquía para estructura, no para tamaño.

No necesitas “rellenar” niveles solo por una regla mecánica, pero la jerarquía debe representar el contenido.

# 7. Landmarks

main/nav/header/footer/aside pueden facilitar navegación.

Evita demasiadas regiones sin nombres que no ayudan.

# 8. Imágenes

Revisa alt según función, como en Unidad 04.

# 9. Formularios

Labels, instrucciones y errores deben asociarse de forma comprensible.

Color por sí solo no debería ser la única forma de comunicar error.

# 10. Herramientas

Auditorías automáticas ayudan, pero no detectan todo.

Combina:

- teclado manual;
- inspector de accesibilidad;
- herramientas automáticas;
- pruebas con lector de pantalla cuando el alcance lo permita.

# 11. Práctica guiada

Audita una página:

1. CSS opcionalmente desactivado;
2. teclado;
3. headings;
4. landmarks;
5. nombres;
6. imágenes;
7. formulario.

Registra barrera→impacto→corrección.

# 12. Errores frecuentes

- ARIA para arreglar HTML incorrecto;
- div como botón;
- foco invisible;
- alt automático sin contexto;
- confiar solo en Lighthouse/validador.

# 13. Reto
Corrige cinco barreras y explica cómo verificaste cada una.

# 14. Autoevaluación

1. ¿Enlace/botón?
2. ¿ARIA añade teclado automáticamente?
3. ¿Qué es nombre accesible?
4. ¿Herramienta automática basta?
5. ¿Por qué probar teclado?

# 15. Checklist

- [ ] HTML nativo.
- [ ] Teclado.
- [ ] Foco/nombres.
- [ ] Alternativas.
- [ ] Verificación manual.

Continúa con CSS.



## Laboratorio completo: Recorrido accesible

### Comprender antes de modificar

La accesibilidad se verifica mediante tareas. Una persona debe poder llegar al contenido, reconocer dónde está el foco y activar los controles sin mouse. Tab avanza por elementos interactivos; Shift+Tab retrocede. Enter activa enlaces y summary puede activarse con teclado según el comportamiento nativo. No conviertas un div en botón si ya existe un elemento apropiado.

El enlace de salto permite evitar navegación repetida. Su destino tiene tabindex="-1" para poder recibir foco sin añadir un paso permanente al recorrido de Tab. Los valores positivos de tabindex crean un orden paralelo que suele romper la lectura natural; conserva el orden del documento. El foco visible no se elimina con outline:none. Una revisión automática puede señalar problemas, pero no juzga todas las alternativas de imágenes ni si una interacción tiene sentido.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

El primer Tab hace visible Saltar al contenido. Al activarlo llegas a main. Puedes abrir y cerrar Qué debes traer con teclado y reconocer el control enfocado.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header><nav aria-label="Principal"><a href="#actividad">Actividad</a> · <a href="#ayuda">Ayuda</a></nav></header>
<main id="contenido" tabindex="-1"><h1>Un recorrido con teclado</h1><section id="actividad"><h2>Actividad</h2><p>Lee la guía y abre los detalles.</p><details><summary>Qué debes traer</summary><p>Un cuaderno y agua.</p></details></section><section id="ayuda"><h2>Ayuda</h2><p><a href="mailto:consulta@example.com">Abrir tu aplicación de correo</a></p></section></main>
```

Las reglas específicas del tema son:

```css
.saltar { position: absolute; left: 1rem; top: -5rem; background: white; padding: .5rem; } .saltar:focus { top: 1rem; }
```

### Experimento y explicación

Recorre la página sin mouse. Escribe la secuencia de controles y comprueba Shift+Tab. Abre el inspector de accesibilidad para identificar el nombre de la navegación. Cambia temporalmente el texto de un enlace a Aquí y explica qué información se pierde.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Ocultas el enlace de salto con display:none y esperas que aparezca al enfocar.

**Cómo resolver:** Un elemento con display:none no participa en el foco normal. Usa la técnica de posicionamiento del ejemplo o una técnica de ocultación visual que lo vuelva visible al recibir foco.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 07: Formularios](../unidad07-formularios/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 09: CSS, cascada e herencia](../unidad09-css-cascada/README.md)
