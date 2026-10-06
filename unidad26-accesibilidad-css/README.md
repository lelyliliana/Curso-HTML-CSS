# Unidad 26: Accesibilidad visual y estados

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Comprobar foco, contraste, reflow, preferencias y estados interactivos desde la capa CSS.

# 1. Foco visible

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
}
```

No elimines outline sin un reemplazo visible y suficiente.

# 2. Contraste de estados

No compruebes solo texto normal.

Revisa:

- enlaces;
- placeholder cuando sea relevante;
- bordes necesarios para identificar controles;
- focus;
- hover;
- disabled;
- error.

# 3. Color

Error, éxito, selección y estado no deben depender únicamente del color.

CSS puede reforzar iconos, bordes y texto, pero HTML debe contener la información esencial.

# 4. Zoom y reflow

Prueba:

- zoom 200%;
- viewport estrecho;
- aumento de texto cuando el entorno lo permita.

Busca:

- texto cortado;
- controles superpuestos;
- scroll horizontal general;
- contenido oculto.

# 5. Unidades y texto

Evita alturas fijas para cajas con texto:

```css
.card {
  height: 120px;
}
```

puede romperse al aumentar texto.

Prefiere contenido que determine altura o usa min-height cuando exista un mínimo real.

# 6. Reduced motion

Respeta `prefers-reduced-motion` en movimientos que puedan afectar a usuarios.

# 7. Forced colors / alto contraste

Sistemas pueden usar modos de colores forzados.

Evita depender de fondos/imágenes para comunicar estados sin alternativa.

Puedes probar `forced-colors` si tu alcance lo requiere.

# 8. Ocultar contenido

`display:none` no es una técnica de “solo visual”.

Usa patrón visually-hidden cuando contenido debe seguir disponible a lectores de pantalla.

# 9. Orden visual

Flex/Grid pueden cambiar presentación, pero evita una secuencia visual que contradiga el DOM/foco.

# 10. Práctica guiada

Audita componentes de Unidad 25:

1. teclado;
2. foco;
3. contraste;
4. zoom;
5. viewport estrecho;
6. reduced motion;
7. estado disabled/error.

Documenta barrera→corrección→verificación.

# 11. Errores frecuentes

- outline:none;
- altura fija con texto;
- contraste solo del body;
- color como único estado;
- orden visual distinto del teclado;
- reduced motion ignorado.

# 12. Reto
Corrige una biblioteca de componentes hasta que funcione con teclado, zoom y preferencias de movimiento.

# 13. Autoevaluación

1. ¿Por qué focus visible?
2. ¿Qué probar además de texto normal?
3. ¿Altura fija y zoom?
4. ¿Display none sirve para screen-reader-only?
5. ¿Orden visual puede diferir del foco?
6. ¿Qué hace reduced motion?

# 14. Checklist

- [ ] Foco.
- [ ] Contraste.
- [ ] Reflow.
- [ ] Estados redundantes.
- [ ] Preferencias respetadas.

Continúa con calidad y publicación.



## Laboratorio completo: CSS que conserva acceso

### Comprender antes de modificar

CSS puede facilitar o impedir acceso aunque el HTML sea correcto. Quitar contornos, fijar alturas o reordenar visualmente controles puede causar barreras. La comprobación debe incluir teclado, ampliación y reflujo. Zoom 200% comprueba que el texto ampliado sigue disponible; el reflujo a un ancho cercano a 320 píxeles CSS aborda otra condición y no se sustituye por una captura grande.

Un foco debe verse sin quedar oculto por un encabezado fijo. Si lo añades, considera espacio o scroll-margin en destinos. Las áreas de acción necesitan tamaño y separación suficientes; los criterios específicos de tamaño de objetivo tienen excepciones y no equivalen a exigir 44 px para cualquier enlace dentro de texto. Una técnica visualmente oculta conserva contenido para herramientas cuando está bien aplicada, pero no debe esconder instrucciones que todas las personas necesitan. El ejemplo usa texto y enlace reales, sin duplicar controles.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

El contenido permanece legible en 320 px de ancho y con texto ampliado. Tab muestra el salto y luego la acción. No hay un panel que aparezca solo al pasar el mouse.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<a class="saltar" href="#contenido">Saltar al contenido</a><main id="contenido" tabindex="-1"><h1>Contenido legible</h1><p class="lectura">Amplía el texto y conserva acceso a todas las acciones. La columna limita longitud, pero no fija altura.</p><p><a class="accion" href="#ayuda">Consultar ayuda</a></p><section id="ayuda"><h2>Ayuda</h2><p>Este texto permanece visible sin depender de hover.</p></section></main>
```

Las reglas específicas del tema son:

```css
.lectura { max-width: 65ch; }
.accion { display: inline-block; padding: .75rem 1rem; border: 2px solid currentColor; }
.saltar { position: absolute; top: -5rem; left: 1rem; background: white; }
.saltar:focus { top: .5rem; }
:focus-visible { outline: 3px solid #9f1239; outline-offset: 3px; }

```

### Experimento y explicación

Prueba el recorrido a 200% y en un ancho de 320 px CSS. Escribe tres observaciones: foco visible, ausencia de recorte y acceso a ayuda. Alarga la frase de la acción y comprueba que sigue cabiendo.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Un encabezado fijo tapa el enlace enfocado o la sección de destino.

**Cómo resolver:** Revisa el posicionamiento y el espacio reservado. Un diseño puede requerir scroll-margin-top en destinos, pero antes evalúa si el encabezado necesita ser fijo.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 25: Componentes y arquitectura CSS](../unidad25-componentes/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 27: DevTools, validación y depuración](../unidad27-devtools/README.md)
