# Unidad 30: Publicación de un sitio estático

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Preparar un sitio portable, publicarlo y diagnosticar diferencias entre localhost y hosting.

# 1. Antes de publicar

Comprueba:

- enlaces;
- rutas;
- mayúsculas/minúsculas;
- imágenes;
- metadatos;
- favicon si aplica;
- accesibilidad;
- responsive;
- archivos innecesarios.

# 2. Portabilidad

No debe existir:

```text
/home/usuario/...
C:\Users\...
localhost:...
```

en recursos que deban funcionar públicamente, salvo documentación/ejemplos claramente identificados.

# 3. Página inicial

Muchos hostings buscan `index.html`.

Respeta convenciones del proveedor.

# 4. GitHub Pages: concepto

Un repositorio puede publicar contenido estático desde una rama/origen configurado.

La URL base puede incluir nombre del repositorio:

```text
https://usuario.github.io/repositorio/
```

Por eso rutas absolutas desde raíz como `/css/styles.css` pueden comportarse distinto que rutas relativas en un project site.

Comprueba la URL real.

# 5. Dominio propio

Si usas dominio:

- DNS;
- configuración del hosting;
- HTTPS;
- canonical;
deben corresponder a la URL pública.

No copies configuración DNS de otro proyecto sin entender registros.

# 6. HTTPS

Usa HTTPS en publicación real.

Evita mixed content: página HTTPS que intenta cargar recursos HTTP puede ser bloqueada/degradada.

# 7. 404

Después de publicar, abre DevTools Network y revisa todos los recursos.

Un sitio puede “verse casi bien” con una fuente/imagen/CSS faltante.

# 8. Caché

Tras actualizar, el navegador/CDN puede conservar recursos.

Antes de “arreglar” archivos al azar:

- revisa Network;
- versión/respuesta;
- hard reload cuando corresponda;
- política del hosting.

# 9. README

Documenta:

- propósito;
- estructura;
- cómo abrir local;
- URL pública;
- tecnologías;
- decisiones relevantes.

No necesitas instrucciones internas de construcción del curso.

# 10. Práctica guiada

Publica una página de práctica en un hosting estático.

Comprueba:

1. home;
2. navegación;
3. imágenes;
4. CSS;
5. móvil;
6. HTTPS;
7. metadatos;
8. 404 inexistente.

# 11. Errores frecuentes

- rutas que solo funcionan local;
- case mismatch;
- URL base ignorada;
- HTTP dentro de HTTPS;
- publicar archivos temporales;
- asumir que push = sitio actualizado instantáneamente.

# 12. Reto
Publica el sitio y realiza una auditoría desde la URL pública, no desde localhost.

# 13. Autoevaluación

1. ¿Por qué index.html?
2. ¿Qué problema tiene ruta /css en project site?
3. ¿Qué es mixed content?
4. ¿Cómo diagnosticar 404?
5. ¿Local y producción pueden diferir?

# 14. Checklist

- [ ] Sitio portable.
- [ ] URL pública verificada.
- [ ] HTTPS.
- [ ] Sin recursos rotos.
- [ ] README útil.

Continúa con taller.



## Guía de publicación

Sigue [PUBLICAR.md](../docs/PUBLICAR.md) para preparar una carpeta independiente, configurar la fuente de Pages y comprobar la URL real.

## Laboratorio completo: Preparar publicación

### Comprender antes de modificar

En un sitio de proyecto, la URL suele incluir el nombre del repositorio. Una ruta /styles.css busca en la raíz del dominio y puede ignorar esa carpeta. styles.css busca junto al HTML. Los enlaces relativos funcionan al mover la carpeta completa, siempre que conserves su estructura.

El ejemplo de esta unidad utiliza una imagen compartida situada fuera de ejemplo. Para publicar un sitio independiente debes copiar todos los recursos necesarios y ajustar rutas; el proyecto final ya incluye sus propios recursos. Publicar el repositorio entero no es lo mismo que publicar únicamente la carpeta del sitio. GitHub Pages permite escoger una fuente por rama o mediante Actions según configuración. La guía adicional explica una ruta de publicación sencilla sin alterar dominio ni DNS. Un push puede iniciar despliegue, pero debes esperar su resultado y comprobar la URL pública.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Inicio y Detalles permiten ida y regreso. Con un servidor local, CSS y SVG responden correctamente. La URL de Detalles conserva la carpeta del ejemplo.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<header><nav aria-label="Principal"><a href="index.html" aria-current="page">Inicio</a> · <a href="detalle.html">Detalles</a></nav></header><main><h1>Mi sitio portable</h1><p>Los recursos y enlaces utilizan rutas relativas.</p><img src="../../recursos/img/aula.svg" alt="Aula organizada para actividades" width="800" height="450"></main>
```

Las reglas específicas del tema son:

```css
main { max-width: 50rem; }
```

### Experimento y explicación

Copia el proyecto final de referencia a una carpeta nueva y comprueba que funcione con sus propios recursos. Revisa las rutas desde la raíz del nuevo sitio. Sigue la guía de publicación con un repositorio de práctica y registra la URL real.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** El sitio funciona localmente porque una ruta apunta a tu escritorio.

**Cómo resolver:** Copia el recurso dentro del proyecto y utiliza una ruta relativa desde el documento. Comprueba mayúsculas exactas, porque el hosting puede distinguirlas aunque tu equipo no lo haga.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 29: SEO técnico básico y metadatos](../unidad29-seo/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 31: Taller integrador de interfaces](../unidad31-taller/README.md)
