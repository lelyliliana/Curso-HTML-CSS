# Unidad 24: Transiciones y animaciones

[Volver al índice del curso](../README.md) · [Ver el curso en Aprende con Leli](https://lelyliliana.github.io/aprende-con-leli/cursos/html-css/)

## Qué aprenderás
Añadir movimiento con propósito, distinguir transition/animation y respetar preferencias de reducción de movimiento.

# 1. Transition

Interpola cambios de propiedades entre estados.

```css
.button {
  transition:
    transform 180ms ease,
    background-color 180ms ease;
}

.button:hover {
  transform: translateY(-2px);
}
```

# 2. No uses transition: all

```css
transition: all .2s;
```

puede animar propiedades inesperadas.

Declara las que realmente deben transicionar.

# 3. Animation

```css
@keyframes pulse {
  from { opacity: .6; }
  to { opacity: 1; }
}
```

Permite secuencias autónomas/múltiples pasos.

No necesitas keyframes para un simple cambio hover.

# 4. Rendimiento

Transform y opacity suelen poder animarse eficientemente.

Animar layout (width, top, etc.) puede requerir más trabajo de layout/paint.

“Solo transform” tampoco es una regla absoluta; mide si el caso importa.

# 5. Reduced motion

```css
@media (prefers-reduced-motion: reduce) {
  .decorative-motion {
    animation: none;
    transition: none;
  }
}
```

La adaptación depende del efecto. Puedes reducir distancia/duración o reemplazar movimiento por cambio no espacial.

# 6. Movimiento con propósito

Útil para:

- feedback;
- relación entre estados;
- orientación espacial.

Evita movimiento constante que distrae sin aportar.

# 7. No bloquees interacción

Una animación no debería impedir que una persona use la interfaz durante segundos innecesarios.

# 8. Práctica guiada

Crea botón, disclosure visual y tarjeta con feedback. Después activa reduced motion en DevTools/SO y comprueba alternativa.

# 9. Errores frecuentes

- transition all;
- animación decorativa infinita;
- ignorar reduced motion;
- movimiento como única señal;
- animar propiedades costosas sin necesidad.

# 10. Reto
Microinteracción con versión completa y reducida, explicando qué información conserva.

# 11. Autoevaluación

1. ¿Transition vs animation?
2. ¿Por qué evitar all?
3. ¿Qué propiedades suelen ser eficientes?
4. ¿Reduced motion = borrar todo siempre?
5. ¿Movimiento debe aportar qué?

# 12. Checklist

- [ ] Movimiento con propósito.
- [ ] Propiedades explícitas.
- [ ] Reduced motion.
- [ ] Interacción no bloqueada.

Continúa con componentes.



## Laboratorio completo: Movimiento opcional

### Comprender antes de modificar

Una transición interpola cambios de propiedades; una animación con keyframes define una secuencia. Ambas deben tener un propósito reconocible. Un pequeño desplazamiento puede señalar interacción, pero no debe sustituir el foco ni hacer inaccesible una acción. Animar transform suele evitar cambiar distribución del resto de elementos, aunque no garantiza rendimiento perfecto en cualquier dispositivo.

El ejemplo habilita movimiento solo cuando no se solicita reducción. Si la persona prefiere movimiento reducido, el enlace sigue cambiando de fondo y conserva el mismo contenido. La información no depende de que se reproduzca una secuencia. Evita transition:all: puede animar futuras propiedades que no pretendías mover. Para movimiento continuo o automático se requieren consideraciones adicionales de pausa y duración. No fuerces desplazamiento suave global sin evaluar las preferencias.

### Archivos y ejecución

Abre [ejemplo/index.html](ejemplo/index.html) desde tu copia del curso. El código fuente en GitHub se muestra como texto; para ver la página abre el archivo descargado o usa el servidor descrito en [Preparar el entorno](../docs/ENTORNO.md). HTML y CSS no necesitan compilarse.

El documento enlaza [ejemplo/styles.css](ejemplo/styles.css). Las primeras reglas de ese archivo proporcionan presentación común (fuente, color y foco); las posteriores corresponden al tema. Para estudiar HTML puedes desactivar temporalmente la hoja. No borres reglas comunes sin revisar su función.

### Qué debe ocurrir

En la preferencia habitual, hover eleva el enlace tres píxeles. Al emular reduce, no hay desplazamiento ni transición. El enlace funciona en ambas condiciones.

### Leer el código del ejemplo

Este fragmento es el contenido de body del archivo completo, no un segundo documento que deba pegarse después de html:

```html
<main><h1>Un cambio breve</h1><p><a class="tarjeta" href="#detalle">Consultar el taller</a></p><section id="detalle"><h2>Taller</h2><p>El contenido no depende de la animación.</p></section></main>
```

Las reglas específicas del tema son:

```css
.tarjeta { display: inline-block; padding: 1rem; border: 2px solid #075985; }
@media (prefers-reduced-motion: no-preference) {
  .tarjeta { transition: transform 150ms ease, background-color 150ms ease; }
  .tarjeta:hover { transform: translateY(-3px); }
}
.tarjeta:hover { background: #e0f2fe; }

```

### Experimento y explicación

Emula prefers-reduced-motion desde las herramientas del navegador. Compara la propiedad transform computada. Añade un cambio de color con duración breve solo bajo no-preference y conserva un estado inmediato al reducir movimiento.

Antes de modificar, escribe tu predicción. Guarda una copia del ejemplo, cambia una condición a la vez y compara lo observado. Conserva el archivo original como referencia; la solución está en [SOLUCIONES.md](SOLUCIONES.md).

### Diagnóstico de un fallo concreto

**Situación:** La animación repite una advertencia y es el único modo de reconocerla.

**Cómo resolver:** Escribe la advertencia como contenido visible persistente y permite una experiencia sin movimiento. Revisa si la repetición aporta valor o solo distracción.

### Práctica autónoma

Completa [PRACTICA.md](PRACTICA.md) antes de avanzar. Incluye la modificación, el resultado esperado y la evidencia de comprobación. Una captura puede apoyar el análisis, pero no sustituye probar el comportamiento indicado.

---

## Continuar el curso

- **Unidad anterior:** [Unidad 23: Pseudoclases y pseudoelementos](../unidad23-pseudo/README.md)
- **Volver al índice:** [Todas las unidades](../README.md)
- **Siguiente unidad:** [Unidad 25: Componentes y arquitectura CSS](../unidad25-componentes/README.md)
