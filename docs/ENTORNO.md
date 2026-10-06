# Preparar el entorno en Ubuntu, Windows o macOS

[Índice](../README.md) · [Unidad 00](../unidad00-web-entorno/README.md) · [Siguiente: documento HTML](../unidad01-documento-html/README.md)

## Herramientas

Necesitas un navegador actual y un editor de texto. El curso utiliza Visual Studio Code como referencia, pero los archivos son HTML y CSS estándar. No necesitas Node.js, npm, Java, Docker ni una cuenta de hosting para comenzar.

1. Descarga el instalador correspondiente desde [Visual Studio Code](https://code.visualstudio.com/download).
2. En Ubuntu, usa el paquete .deb de la arquitectura de tu equipo y ábrelo con el instalador de paquetes; consulta la [guía de Linux](https://code.visualstudio.com/docs/setup/linux) si utilizas otro método.
3. En Windows, ejecuta el instalador para tu usuario. No es necesario instalar WSL para este curso.
4. En macOS, abre el archivo descargado y mueve la aplicación a Aplicaciones. Selecciona la arquitectura correspondiente.
5. Abre VS Code y utiliza Archivo (File) > Abrir carpeta (Open Folder). Abre la carpeta raíz del curso o de tu proyecto, no un archivo suelto.

## Obtener una copia

En el repositorio de GitHub, usa Code > Download ZIP y extrae el archivo. Trabaja en la carpeta extraída; no intentes editar dentro del comprimido. Si ya utilizas Git, puedes clonar el repositorio y abrir la copia local. El curso no requiere aprender Git antes de la primera página.

## Abrir HTML sin servidor

1. En el explorador de archivos, entra en unidad00-web-entorno/ejemplo.
2. Abre index.html con tu navegador.
3. Abre el mismo archivo en el editor y cambia una frase.
4. Guarda (Ctrl+S en Windows/Ubuntu, Command+S en macOS).
5. Recarga el navegador. Comprueba que estás viendo el archivo que editaste.

La dirección comienza por file:. Es suficiente para los primeros ejemplos estáticos. Para revisar HTTP, estados de recursos y publicación, utiliza un servidor local.

## Servidor local desde VS Code

1. Abre Extensiones y busca **Live Preview**, publicado por **Microsoft** (identificador ms-vscode.live-server).
2. Instálalo y abre el HTML de la lección.
3. Usa la acción de previsualización de la extensión. Los nombres de menús pueden cambiar por versión e idioma; consulta su [documentación](https://marketplace.visualstudio.com/items?itemName=ms-vscode.live-server).
4. Abre también la vista en el navegador externo para utilizar DevTools y teclado de forma completa.
5. Confirma que la dirección comienza por http y conserva la carpeta del archivo.

No instales una extensión solo porque tenga un nombre parecido: comprueba editor e identificador. No necesitas instalar varias extensiones de servidor simultáneamente.

## Alternativa con Python (si ya lo tienes)

Abre una terminal en la raíz del curso. No ejecutes este servidor dentro de una carpeta que contenga datos privados.

| Sistema | Comando |
|---|---|
| Ubuntu | `python3 -m http.server 8000 --bind 127.0.0.1` |
| Windows con Python Launcher | `py -3 -m http.server 8000 --bind 127.0.0.1` |
| macOS con Python instalado | `python3 -m http.server 8000 --bind 127.0.0.1` |

Abre http://127.0.0.1:8000/unidad00-web-entorno/ejemplo/. Mantén la terminal abierta y detén el servidor con Ctrl+C. Si el puerto está ocupado, elige otro y utiliza ese mismo número en la URL. No es necesario exponer el servidor a Internet. Si no tienes Python, usa la alternativa de VS Code; este curso no exige instalar otro lenguaje.

## DevTools

En el menú del navegador busca Herramientas de desarrollo o Inspeccionar. En muchos navegadores F12 o Ctrl+Shift+I funciona en Windows/Ubuntu y Command+Option+I en macOS. Los nombres varían entre Chrome, Edge, Firefox y Safari. Safari puede requerir habilitar herramientas para desarrolladores en sus ajustes avanzados.

- Elements/Inspector: estructura del documento.
- Styles/Rules y Computed: reglas aplicadas y valores resultantes.
- Network/Red: URL, estado y carga de recursos; abre el panel y recarga para registrar solicitudes.
- Accessibility/Accesibilidad: nombres y estructura expuesta a herramientas.

## Comprobación final

Puedes editar, guardar y recargar. El HTML enlaza su CSS y la imagen; las rutas no contienen nombres personales ni directorios de tu computador. Bajo HTTP los recursos responden correctamente. Si no aparece un cambio, comprueba archivo editado, archivo abierto, guardado y caché antes de modificar más código.

[Volver a la unidad 00](../unidad00-web-entorno/README.md)
