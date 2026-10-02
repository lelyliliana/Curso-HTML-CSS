# Unidad 08 — Accesibilidad HTML

## Qué aprenderás
Evaluar una página con semántica, teclado, nombres accesibles y alternativas antes de depender de ARIA.

# 1. Accesibilidad no es una etapa final

Una página accesible comienza con HTML correcto:
- headings;
- landmarks;
- enlaces;
- botones;
- labels;
- alt;
- idioma.

Corregir todo al final suele ser más difícil.

# 2. Teclado

Prueba:
- Tab;
- Shift+Tab;
- Enter;
- Space donde corresponda.

Pregunta:
- ¿puedo alcanzar controles?
- ¿sé dónde está el foco?
- ¿el orden tiene sentido?
- ¿puedo activar?

# 3. Botón vs enlace

**Enlace:** navega.  
**Botón:** ejecuta una acción.

No uses `<div onclick>` para recrear un botón si existe `<button>`.

# 4. Nombre accesible

Un control necesita un nombre comprensible.

Puede venir de:
- texto;
- label;
- alt en ciertos contextos;
- aria-label/labelledby cuando realmente es necesario.

# 5. ARIA

Regla útil:
> HTML nativo primero.

ARIA puede añadir semántica/estado, pero no añade automáticamente comportamiento de teclado.

`role="button"` en un div no lo convierte mágicamente en un botón completo.

# 6. Encabezados

Usa jerarquía para estructura, no para tamaño.

No necesitas “rellenar” niveles solo por una regla mecánica, pero la jerarquía debe representar el contenido.

# 7. Landmarks

main/nav/header/footer/aside pueden facilitar navegación.

Evita demasiadas regiones sin nombres que no ayudan.

# 8. Imágenes

Revisa alt según función, como en Unidad 04.

# 9. Formularios

Labels, instrucciones y errores deben asociarse de forma comprensible.

Color por sí solo no debería ser la única forma de comunicar error.

# 10. Herramientas

Auditorías automáticas ayudan, pero no detectan todo.

Combina:
- teclado manual;
- inspector de accesibilidad;
- herramientas automáticas;
- pruebas con lector de pantalla cuando el alcance lo permita.

# 11. Práctica guiada

Audita una página:
1. CSS opcionalmente desactivado;
2. teclado;
3. headings;
4. landmarks;
5. nombres;
6. imágenes;
7. formulario.

Registra barrera→impacto→corrección.

# 12. Errores frecuentes
- ARIA para arreglar HTML incorrecto;
- div como botón;
- foco invisible;
- alt automático sin contexto;
- confiar solo en Lighthouse/validador.

# 13. Reto
Corrige cinco barreras y explica cómo verificaste cada una.

# 14. Autoevaluación
1. ¿Enlace/botón?
2. ¿ARIA añade teclado automáticamente?
3. ¿Qué es nombre accesible?
4. ¿Herramienta automática basta?
5. ¿Por qué probar teclado?

# 15. Checklist
- [ ] HTML nativo.
- [ ] Teclado.
- [ ] Foco/nombres.
- [ ] Alternativas.
- [ ] Verificación manual.

Continúa con CSS.
