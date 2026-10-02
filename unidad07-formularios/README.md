# Unidad 07 — Formularios

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
