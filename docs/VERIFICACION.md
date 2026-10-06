# Comprobar los ejemplos

[Índice](../README.md) · [Entorno](ENTORNO.md) · [Proyecto final](../unidad32-proyecto-final/README.md)

La lectura y ejecución de los ejemplos HTML/CSS no necesitan Python ni paquetes. Las comprobaciones siguientes son opcionales para quien quiera revisar el repositorio completo.

## Integridad de archivos

Desde la raíz del curso ejecuta `python scripts/verificar.py` (en Ubuntu/macOS puedes usar python3; en Windows con Launcher, py -3). Solo utiliza la biblioteca estándar.

Comprueba destinos locales de documentación y HTML, fragmentos HTML, imágenes con alt, id únicos, asociaciones label/for, bloques Markdown cerrados y navegación de las 33 unidades. No solicita páginas externas ni juzga toda la accesibilidad.

## Comportamiento en navegador

1. En un entorno Python de pruebas instala `python -m pip install -r tests/requirements.txt`.
2. Instala el navegador de pruebas con `python -m playwright install --with-deps firefox`. En Linux puede requerir permisos para dependencias del sistema.
3. Ejecuta `python tests/navegador.py` desde la raíz.

Las dependencias de pruebas no forman parte del sitio. Playwright ejecuta Firefox; html5lib comprueba reparaciones del parser HTML5 y tinycss2 comprueba sintaxis léxica. Esta revisión no equivale a la validación normativa completa de Nu HTML Checker ni a comprobar que todas las propiedades CSS tengan valores admitidos.

Los casos comprueban carga de los 31 laboratorios, anchos 320/768/1440, cascada, selectores, modelo de caja, Grid, media query, picture, variables, movimiento reducido, formularios inválidos/válidos, destinos de tarjetas, salto con teclado, details y portabilidad de la carpeta del sitio final. El proyecto se prueba también con fuente raíz ampliada al 200%; esa comprobación no sustituye el zoom real del navegador.

## Comprobación manual necesaria

Usa el [checklist final](../unidad32-proyecto-final/CHECKLIST.md). Revisa además zoom real, contraste de todos los estados, lector de pantalla cuando esté disponible, contenido variable y URL pública. Una prueba automática que pasa no demuestra conformidad completa con WCAG ni ausencia de todos los errores.

[Volver al índice](../README.md)
