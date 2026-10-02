# Unidad 28 — Rendimiento web básico

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

# 2. Core Web Vitals — contexto

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
