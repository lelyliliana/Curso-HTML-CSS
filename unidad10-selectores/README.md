# Unidad 10: Selectores y especificidad

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Seleccionar elementos sin acoplar el CSS innecesariamente al HTML y razonar sobre especificidad.

# 1. Selectores básicos

```css
p {}
.card {}
#principal {}
[data-state="active"] {}
```

Tipo, clase, id y atributo expresan criterios distintos.

Para estilos reutilizables, las clases suelen ser una base predecible.

# 2. Combinadores

Descendiente:
```css
.card p {}
```

Hijo directo:
```css
.card > p {}
```

Hermano adyacente:
```css
h2 + p {}
```

Usa el selector que represente la relación necesaria, no uno más profundo “para asegurar”.

# 3. Especificidad

Modelo práctico:

- IDs pesan más que clases/atributos/pseudoclases;
- clases pesan más que tipos/pseudoelementos;
- el orden decide cuando la prioridad/especificidad relevante empata.

No conviertas esto en una carrera de números.

# 4. Ejemplo

```css
a { color: blue; }
.nav__link { color: green; }
#principal a { color: red; }
```

El id hace muy difícil sobrescribir el estilo de forma reutilizable.

Por eso no se recomienda usar IDs como herramienta habitual de styling.

# 5. Clases de componente

```css
.card {}
.card__title {}
.card--featured {}
```

Es una convención posible para nombres predecibles. No necesitas adoptar BEM completo para beneficiarte de clases explícitas.

# 6. Selectores profundos

```css
main .page .content article .card h3 span {}
```

Se rompe cuando cambia la estructura y acumula especificidad.

Mejor, cuando el elemento tiene un rol reutilizable:

```css
.card__label {}
```

# 7. :where e :is

CSS moderno ofrece `:where()` con especificidad cero para el selector funcional y `:is()` con reglas propias de especificidad.

Son útiles para APIs de estilos, pero no sustituyen comprender lo básico.

# 8. Práctica guiada

Refactoriza un selector de cinco niveles a clases de componente. Cambia el HTML interno y comprueba cuál versión resiste mejor.

# 9. Errores frecuentes

- IDs para ganar;
- selectores demasiado profundos;
- !important como parche;
- clase ligada a apariencia como `.texto-rojo-18px` cuando debería expresar rol;
- selector universal indiscriminado para estilos costosos/inesperados.

# 10. Reto
Diseña estilos de tarjeta que puedan reutilizarse en dos secciones sin aumentar especificidad.

# 11. Autoevaluación

1. ¿Clase vs id?
2. ¿Qué hace >?
3. ¿Por qué selector profundo acopla?
4. ¿Qué ocurre si empata especificidad?
5. ¿Para qué puede servir :where?

# 12. Checklist

- [ ] Selectores claros.
- [ ] Especificidad baja/predecible.
- [ ] Evito profundidad.
- [ ] Reutilizo componentes.

Continúa con box model.



## Laboratorio completo: Selectores con alcance

### Comprender antes de modificar

Un selector describe un conjunto de elementos. .panel > p selecciona párrafos hijos directos de panel; .panel p también alcanzaría párrafos descendientes dentro de otro contenedor. .recursos a.especial requiere que el enlace tenga esa clase y esté dentro de recursos. El espacio entre selectores comunica relación de descendencia; escribir .recursos.especial exige ambas clases en el mismo elemento.

Las clases permiten agrupar por función y reutilizar estilos. Un id identifica un destino único y también puede seleccionarse con CSS, pero aumenta especificidad y no es necesario para cada componente visual. Mantener alcance explícito evita que una regla p global cambie avisos, pies y tarjetas simultáneamente. Primero identifica qué elementos deben cambiar y luego escribe el selector. No compenses una selección incorrecta agregando propiedades a todos los elementos.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Solo el párrafo directamente dentro del panel tiene fondo azul claro. Taller está en negrita. El párrafo externo no recibe el fondo del panel.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Selectores</h1><section class="panel"><h2>Recursos</h2><ul class="recursos"><li><a href="#nota">Guía</a></li><li><a href="#nota" class="especial">Taller</a></li></ul><p id="nota">Todos los recursos están disponibles.</p></section><p>Este párrafo está fuera del panel.</p></main>
```

Las reglas específicas del tema son:

```css
.panel { border: 2px solid #075985; padding: 1rem; }
.panel > p { background: #f0f9ff; }
.recursos a { text-decoration-thickness: .15em; }
.recursos a.especial { font-weight: bold; }

```

### Experimento y explicación

Envuelve el párrafo del panel en un div. Predice si sigue seleccionado por >. Cambia el selector a .panel p y observa. Crea luego una clase para seleccionar ese aviso sin depender de la profundidad.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Escribes .recursos .especial y crees que exige dos clases en el mismo elemento.

**Cómo resolver:** El espacio significa descendencia. Usa .recursos.especial para ambas clases en el mismo elemento o .recursos a.especial para enlaces especiales dentro de la lista.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 09: CSS, cascada e herencia](../unidad09-css-cascada/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 11: Modelo de caja](../unidad11-box-model/README.md)
