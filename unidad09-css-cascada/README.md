# Unidad 09 — CSS, cascada e herencia

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
