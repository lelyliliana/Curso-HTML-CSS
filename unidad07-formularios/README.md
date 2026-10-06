# Unidad 07: Formularios

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Construir controles etiquetados, comprender name/value y usar validación HTML sin confundirla con validación de servidor.

# 1. Form

```html
<form action="/registro" method="post">
  ...
</form>
```

`action` indica destino y `method` método HTTP del envío tradicional.

En un sitio estático de práctica el backend puede no existir; aun así aprende el contrato.

# 2. Label

```html
<label for="correo">Correo</label>
<input id="correo" name="correo" type="email">
```

`for` coincide con `id`.

El label amplía la zona activable y da nombre accesible.

Placeholder no lo sustituye.

# 3. name

```html
<input name="correo">
```

`name` identifica el dato al enviar formulario.

Un input con id pero sin name puede no enviarse como esperas.

# 4. Tipos

Usa tipos adecuados:

- email;
- number;
- date;
- tel;
- checkbox;
- radio.

Aportan semántica, teclados móviles y validaciones básicas, pero no garantizan datos válidos de negocio.

# 5. required y restricciones

```html
<input
  type="number"
  name="edad"
  min="18"
  max="100"
  required>
```

El navegador puede ayudar.

El servidor debe volver a validar porque el cliente puede omitirse/manipularse.

# 6. Radio

Radios del mismo grupo comparten `name`.

```html
<input type="radio" name="plan" value="basico">
```

# 7. Checkbox

Puede representar booleanos o múltiples opciones según nombres/valores.

No asumas que un checkbox no marcado enviará siempre un valor.

# 8. fieldset/legend

Agrupan controles relacionados, especialmente útil para radio/checkbox.

# 9. Botones

```html
<button type="submit">Enviar</button>
<button type="button">Vista previa</button>
```

Dentro de form, especifica tipo cuando la intención importa; el default de button puede ser submit.

# 10. Autocomplete

Atributos `autocomplete` apropiados pueden mejorar experiencia.

No desactives autocomplete indiscriminadamente.

# 11. Práctica guiada

Formulario de registro:

- nombre;
- email;
- plan;
- términos;
- botón.

Prueba solo teclado y envío con campos inválidos.

# 12. Errores frecuentes

- placeholder como label;
- input sin name;
- botón accidentalmente submit;
- validación cliente como única defensa;
- fieldset omitido en grupos complejos.

# 13. Reto
Formulario accesible con instrucciones, errores nativos básicos y grupos correctamente etiquetados.

# 14. Autoevaluación

1. ¿for/id?
2. ¿Para qué name?
3. ¿Placeholder reemplaza label?
4. ¿Cliente basta para validar?
5. ¿Qué agrupa fieldset?
6. ¿button default puede sorprender?

# 15. Checklist

- [ ] Labels.
- [ ] Names.
- [ ] Tipos correctos.
- [ ] Grupos.
- [ ] Validación básica.

Continúa con accesibilidad.



## Laboratorio completo: Formulario de práctica

### Comprender antes de modificar

Un control necesita nombre accesible y, para participar en el envío tradicional, un name. id sirve para asociar el label mediante for y debe ser único. name determina la clave enviada. El atributo type="email" activa una comprobación sintáctica del navegador, pero no verifica que una cuenta exista. required evita el envío vacío normal; no sustituye validación de servidor.

Los radio comparten name para formar una elección exclusiva y tienen value distintos. fieldset y legend dan contexto al grupo. La ayuda visible explica qué sucede. Este formulario usa GET hacia una página estática de demostración: los valores se incorporan a la URL, no se almacenan ni se envía correo. No lo uses con datos sensibles. En producción, un endpoint real y su contrato decidirían método, tratamiento y persistencia. El mensaje de validación varía por idioma y navegador: evalúa comportamiento, no una frase exacta.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Enviar vacío activa validación. Un correo como persona no cumple el tipo email. Con nombre Ana, correo ana@example.com y un taller, se abre resultado.html con parámetros de consulta. Esa página advierte que no hubo inscripción real.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Elegir un taller</h1><p id="aviso">Demostración local: no se envían datos a una organización. Usa información ficticia.</p>
<form action="resultado.html" method="get" aria-describedby="aviso">
  <p><label for="nombre">Nombre ficticio (obligatorio)</label><br><input id="nombre" name="nombre" autocomplete="off" required minlength="2"></p>
  <p><label for="correo">Correo ficticio (obligatorio)</label><br><input id="correo" name="correo" type="email" autocomplete="off" required></p>
  <fieldset><legend>Taller preferido</legend><label><input type="radio" name="taller" value="lectura" required> Lectura</label><label><input type="radio" name="taller" value="robotica"> Robótica</label></fieldset>
  <p><button type="submit">Comprobar formulario local</button></p>
</form></main>
```

Las reglas específicas del tema son:

```css
fieldset { max-width: 35rem; } fieldset label { display: block; } input:not([type="radio"]) { max-width: 100%; box-sizing: border-box; }
```

### Experimento y explicación

Prueba vacío, nombre de una letra, correo sin formato válido y datos ficticios completos. Anota cuál control impide continuar. Retira temporalmente name del correo y compara los parámetros del envío válido.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Se muestra un placeholder como única etiqueta y un botón que promete Inscribirme de verdad.

**Cómo resolver:** Añade label visible y describe el alcance real. El placeholder desaparece al escribir y no debe ser la única instrucción. Una página estática de resultado no prueba entrega de mensajes.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 06: Tablas de datos](../unidad06-tablas/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 08: Accesibilidad HTML](../unidad08-accesibilidad/README.md)
