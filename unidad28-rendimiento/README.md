# Unidad 28: Rendimiento web básico

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Medir una página, identificar recursos costosos y mejorar carga sin sacrificar calidad o accesibilidad.

# 1. Mide primero

No optimices por intuición.

Usa Network/Lighthouse u otras herramientas para observar:

- bytes;
- solicitudes;
- tiempos;
- imágenes;
- fuentes;
- métricas de experiencia.

# 2. Core Web Vitals: contexto

Métricas como:

- LCP;
- INP;
- CLS;

ayudan a evaluar carga, interacción y estabilidad visual.

Los umbrales/evaluación pueden evolucionar; usa documentación actual cuando realices una auditoría formal.

Aquí aprendemos qué problema representa cada métrica.

# 3. LCP

Puede estar dominado por hero/texto/imagen principal.

Una imagen LCP:

- no debería descargarse gigantesca sin necesidad;
- normalmente no conviene lazy-load si es visible inicialmente;
- debe descubrirse/cargarse apropiadamente.

# 4. CLS

Cambios inesperados de layout pueden venir de:

- imágenes sin dimensiones;
- contenido insertado;
- fuentes;
- embeds.

Reserva espacio cuando sea posible.

# 5. INP

Relaciona capacidad de respuesta a interacciones.

En HTML/CSS puro hay poca lógica JS, pero CSS/layout pesado y recursos también forman parte del contexto de experiencia.

Se profundizará al estudiar JavaScript.

# 6. Imágenes

Optimiza:

- dimensiones;
- compresión;
- formato;
- srcset/sizes;
- lazy fuera de viewport.

# 7. Fuentes

Cada familia/peso/estilo puede añadir recursos.

Pregunta si realmente necesitas 300,400,500,600,700 en dos familias.

# 8. CSS

Evita:

- frameworks enormes sin usar;
- duplicación;
- imports encadenados innecesarios en escenarios críticos;
- reglas obsoletas.

Pero no sacrifiques mantenibilidad por ahorrar unos pocos bytes sin medir.

# 9. Caché

El servidor/CDN controla políticas HTTP de caché.

En un hosting estático puede existir configuración automática.

No puedes resolver toda estrategia de caché solo desde CSS.

# 10. Práctica guiada

Mide página antes.

Optimiza una imagen y fuentes.

Repite exactamente el mismo escenario y documenta diferencias.

# 11. Errores frecuentes

- comprimir sin baseline;
- lazy en LCP;
- quitar dimensiones;
- perseguir 100 de Lighthouse como objetivo absoluto;
- comparar mediciones bajo condiciones diferentes.

# 12. Reto
Informe antes/después con evidencia y explicación de qué cambió realmente.

# 13. Autoevaluación

1. ¿Qué representa LCP?
2. ¿CLS?
3. ¿Por qué dimensiones de imagen?
4. ¿Lazy siempre?
5. ¿Más fuentes cuestan?
6. ¿Lighthouse 100 garantiza calidad?

# 14. Checklist

- [ ] Baseline.
- [ ] Optimizo recursos.
- [ ] Repito medición.
- [ ] No persigo métricas vacías.

Continúa con metadatos.



## Laboratorio completo: Carga y tamaño de recursos

### Comprender antes de modificar

Rendimiento necesita una medición de referencia y una comparación bajo condiciones similares. Una ilustración local y fuente de sistema evitan solicitudes a terceros, pero no garantizan un sitio rápido en todos los dispositivos. Network permite ver cantidad de recursos, tamaño transferido, caché y tiempos. Registra si la caché estaba desactivada y qué limitación de red utilizaste.

Dimensiones de imagen ayudan a reservar espacio y reducir movimientos durante carga. Reducir bytes no siempre resuelve LCP, que depende del contenido principal, descubrimiento y descarga. lazy puede retrasar imágenes fuera de pantalla, pero perjudicar una imagen importante visible inicialmente. No comprimas una fotografía hasta volver ilegible un texto relevante. Separa métricas de laboratorio de datos reales de visitantes: una puntuación de una ejecución no demuestra comportamiento universal.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

Bajo HTTP se cargan HTML, CSS y una imagen local. No se descargan fuentes externas ni JavaScript. La imagen reserva proporción antes de completar la carga.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Una página sin dependencias remotas</h1><img src="../../recursos/img/aula.svg" alt="Mesas y pizarra de un aula" width="800" height="450"><p>El ejemplo utiliza una fuente del sistema y una ilustración local.</p><section><h2>Contenido adicional</h2><p>Duplica texto aquí para estudiar el desplazamiento y la carga diferida de imágenes situadas realmente fuera de la vista inicial.</p></section></main>
```

Las reglas específicas del tema son:

```css
main { max-width: 60rem; margin-inline: auto; }
```

### Experimento y explicación

Registra URL, navegador, tamaño transferido y número de solicitudes con caché desactivada. Añade una fotografía propia con sus dimensiones reales, mide y genera una variante más pequeña adecuada a su presentación. Compara calidad y bytes.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** Mides una versión sin caché y otra desde caché y atribuyes toda la mejora al CSS.

**Cómo resolver:** Repite con condiciones equivalentes. Network indica si el recurso viene de memoria/disco. Cambia una variable relevante por vez para que la comparación tenga sentido.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 27: DevTools, validación y depuración](../unidad27-devtools/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 29: SEO técnico básico y metadatos](../unidad29-seo/README.md)
