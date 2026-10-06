# Unidad 00: Cómo funciona la Web y preparar el entorno

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Comprender qué ocurre al abrir una página, distinguir archivo/URL/servidor y preparar un proyecto que puedas diagnosticar.

# 1. Qué ocurre al visitar un sitio

Modelo simplificado:

```text
navegador → solicitud HTTP → servidor
navegador ← respuesta HTML/CSS/recursos ← servidor
```

El navegador interpreta los recursos y construye la página.

No confundas Internet, Web, navegador y servidor: son conceptos relacionados, no sinónimos.

# 2. URL

Ejemplo:

```text
https://ejemplo.com/cursos/index.html
```

Podemos reconocer:

- esquema/protocolo: https;
- host: ejemplo.com;
- ruta: /cursos/index.html.

Una URL puede incluir puerto, query y fragmento.

# 3. Archivo local vs HTTP

Abrir:

```text
file:///home/usuario/mi-sitio/index.html
```

no es igual que servir:

```text
http://localhost:...
```

Algunas APIs/rutas/comportamientos dependen del contexto HTTP.

Para HTML/CSS básico puedes comenzar con archivo local y después usar un servidor local sencillo.

# 4. Proyecto

```text
mi-sitio/
├── index.html
├── css/
│   └── styles.css
└── img/
```

Usa nombres:

- claros;
- sin rutas personales;
- consistentes en mayúsculas/minúsculas.

Un hosting Linux puede distinguir `Logo.png` de `logo.png`.

# 5. Rutas relativas

Desde index.html:

```html
<link rel="stylesheet" href="css/styles.css">
<img src="img/logo.png" alt="...">
```

No uses:

```text
/home/miusuario/Escritorio/logo.png
```

Eso solo existe en tu equipo.

# 6. DevTools desde el inicio

Aprende:

- Elements/Inspector;
- Styles;
- Network;
- Console.

Si una imagen no aparece, no adivines: Network puede mostrar 404 y la URL solicitada.

# 7. Código fuente vs DOM

El HTML fuente es el documento recibido/escrito.

El navegador construye un DOM y puede normalizar ciertas estructuras.

Más adelante JavaScript podrá modificar ese DOM.

# 8. Práctica guiada

1. crea estructura;
2. index.html mínimo;
3. styles.css;
4. enlázalo;
5. abre DevTools;
6. rompe deliberadamente la ruta CSS;
7. identifica el fallo;
8. corrige.

# 9. Errores frecuentes

- rutas absolutas personales;
- nombres con mayúsculas inconsistentes;
- editar archivo distinto al abierto;
- confundir archivo local con servidor;
- “no funciona” sin revisar Network/Console.

# 10. Reto
Crea sitio mínimo con HTML, CSS e imagen usando solo rutas relativas y comprueba recursos en Network.

# 11. Autoevaluación

1. ¿Navegador y servidor son lo mismo?
2. ¿Qué partes tiene una URL?
3. ¿file:// y http:// son iguales?
4. ¿Por qué evitar rutas personales?
5. ¿Qué panel ayuda con un 404?

# 12. Checklist

- [ ] Comprendo flujo web.
- [ ] Creo estructura.
- [ ] Uso rutas relativas.
- [ ] Diagnostico recursos.

Continúa con HTML.



## Laboratorio completo: Primer sitio local

### Comprender antes de modificar

Un sitio puede ser una colección de archivos antes de publicarse. El navegador interpreta index.html y solicita cada recurso indicado por sus rutas. La ruta del CSS se resuelve desde el HTML; una ruta usada dentro de CSS se resuelve desde el archivo CSS. Por eso mover un archivo puede romper recursos sin cambiar su nombre.

En este ejemplo styles.css está junto a index.html. La imagen se encuentra en recursos/img, dos niveles por encima. Cada ../ sube una carpeta. Escribir una ruta de tu escritorio impediría que otra persona abriera el ejemplo en su equipo. Usa el explorador de archivos de VS Code para reconocer la estructura antes de escribir rutas. Un archivo guardado no implica que la pestaña del navegador se haya actualizado: guarda y recarga.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Verás un título azul, un párrafo y una ilustración de aula. En Network, bajo HTTP, el HTML, el CSS y el SVG deben responder correctamente. El nombre de la pestaña será Primer sitio local.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main>
  <h1>Mi primer sitio</h1>
  <p>Esta página se abre desde una carpeta de mi computador.</p>
  <img src="../../recursos/img/aula.svg" alt="Tres mesas organizadas alrededor de una pizarra" width="800" height="450">
  <p><a href="https://developer.mozilla.org/es/">Consultar MDN</a></p>
</main>
```

Las reglas específicas del tema son:

```css
h1 { color: #075985; }
```

### Experimento y explicación

Cambia el texto del párrafo por tu nombre y una meta de aprendizaje. Cambia temporalmente href="styles.css" por href="estilo.css", guarda y recarga. Anota qué aspecto cambia y qué recurso falla. Restablece styles.css.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** La imagen no aparece después de mover index.html a otra carpeta.

**Cómo resolver:** Recalcula la ruta desde la ubicación nueva. Comprueba nombre, extensión y mayúsculas. El hecho de que el SVG exista en el repositorio no garantiza que la URL solicitada apunte a él.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 01: Documento HTML](../unidad01-documento-html/README.md)
