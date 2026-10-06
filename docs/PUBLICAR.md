# Publicar tu sitio de práctica en GitHub Pages

[Índice del curso](../README.md) · [Unidad 30](../unidad30-publicacion/README.md) · [Siguiente: taller](../unidad31-taller/README.md)

## Preparar una carpeta independiente

1. Copia la carpeta ejemplos/sitio-final completa a una carpeta de proyecto. Si publicas tu propia solución, incluye todos sus recursos.
2. Comprueba que index.html esté en la raíz de esa carpeta y pueda abrir las páginas secundarias.
3. Revisa rutas y nombres exactos. styles.css e img deben estar dentro del proyecto. No publiques datos privados ni archivos ajenos al sitio.
4. Actualiza el README para describir tu proyecto y su carácter ficticio.

## Crear y subir el repositorio

1. En GitHub crea un repositorio de práctica. Un repositorio público está disponible para el uso habitual de Pages; las opciones para privados dependen del plan.
2. Sube el contenido de la carpeta del sitio a la raíz del repositorio mediante Add file > Upload files, o usa Git si conoces su flujo.
3. Comprueba en GitHub que index.html y styles.css estén directamente en la raíz, no dentro de otra carpeta innecesaria. Confirma que img también esté presente.

## Activar publicación por rama

1. En el repositorio abre Settings > Pages.
2. En Build and deployment selecciona Deploy from a branch.
3. Selecciona la rama que contiene el sitio (normalmente main) y la carpeta / (root). Guarda.
4. Revisa el resultado del despliegue y la URL que muestra Pages. No asumas que publicar un commit actualiza el sitio instantáneamente.
5. Abre la URL generada. Un sitio de proyecto suele tener la forma https://usuario.github.io/nombre-repositorio/.

La interfaz puede variar por idioma o permisos. Si no aparece Pages, comprueba acceso al repositorio y disponibilidad del plan. Consulta la [documentación oficial de la fuente de publicación](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site). Esta actividad no necesita configurar un dominio ni cambiar DNS.

## Auditar la dirección pública

1. Abre Inicio y luego Talleres/Contacto. Copia la URL de Talleres y ábrela directamente en otra pestaña.
2. Revisa Network después de recargar. HTML, CSS e imágenes deben tener respuestas correctas.
3. Prueba los enlaces a fragmentos y el formulario con datos ficticios. GET no añade un servicio de correo por estar publicado.
4. Confirma HTTPS y ausencia de recursos HTTP incrustados.
5. Abre una dirección que no exista para comprobar la página 404. Verifica que el enlace de regreso tenga sentido desde esa dirección; las rutas relativas de una página 404 pueden necesitar adaptación según su ubicación.
6. Actualiza README con la URL real y fecha de revisión.

## Si algo falla

| Síntoma | Comprobación | Corrección |
|---|---|---|
| Inicio no aparece | index.html y fuente de publicación | Selecciona rama/carpeta que realmente lo contiene |
| Falta CSS | URL solicitada en Network | Usa ruta relativa y mayúsculas correctas |
| Faltan imágenes | Archivo subido y URL | Copia recursos y corrige ruta |
| No aparece el último cambio | Estado del despliegue y caché | Espera resultado, revisa recurso recibido y recarga |
| Formulario no envía correo | Alcance estático | Mantén el aviso; necesitarías un servicio real para enviar |

[Volver a la Unidad 30](../unidad30-publicacion/README.md)
