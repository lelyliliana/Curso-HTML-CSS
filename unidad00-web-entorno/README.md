# Unidad 00 — Cómo funciona la Web y preparar el entorno

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


---

## Continuar el curso

- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 01 — Documento HTML](../unidad01-documento-html/README.md)
