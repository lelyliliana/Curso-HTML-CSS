# Unidad 16 — Flexbox

## Qué aprenderás
Distribuir ítems en un eje principal, controlar alineación y comprender grow, shrink, basis y wrap.

# 1. Contenedor e ítems

```css
.toolbar {
  display: flex;
}
```

`.toolbar` es **flex container**.

Sus hijos directos se convierten en **flex items**.

Una propiedad como `justify-content` va normalmente en el contenedor, no en cada hijo.

# 2. Ejes

Con:

```css
flex-direction: row;
```

main axis suele ser horizontal en escritura izquierda→derecha.

cross axis es perpendicular.

Si cambias a column, los ejes cambian.

No memorices “justify = horizontal”.

# 3. justify-content

Distribuye ítems a lo largo del **main axis**.

# 4. align-items

Alinea ítems en el **cross axis** dentro de la línea.

# 5. gap

```css
display: flex;
gap: 1rem;
```

Crea espacio entre ítems sin márgenes laterales manuales.

# 6. flex-wrap

```css
flex-wrap: wrap;
```

Permite crear múltiples líneas cuando no cabe.

Si existe wrap, `align-content` puede distribuir líneas cuando hay espacio adicional en cross axis.

# 7. flex shorthand

```css
.item {
  flex: 1 1 15rem;
}
```

Conceptualmente:
- grow: crecer;
- shrink: encoger;
- basis: tamaño base.

No memorices `flex:1` sin comprender qué comportamiento necesitas.

# 8. min-width:auto

Los flex items pueden negarse a encogerse por su tamaño mínimo intrínseco.

En algunos layouts:

```css
.item {
  min-width: 0;
}
```

permite que contenido se encoja/trunque según diseño.

Úsalo después de diagnosticar, no como reset universal.

# 9. Auto margins

```css
.login {
  margin-inline-start: auto;
}
```

Puede empujar un ítem consumiendo espacio libre en el eje principal.

# 10. Orden visual

`order` puede cambiar visualmente el orden sin cambiar DOM.

Eso puede crear diferencias con navegación por teclado/lectores.

No lo uses para corregir una estructura HTML incorrecta.

# 11. Práctica guiada

Construye:
- barra con logo/nav/acción;
- grupo de botones;
- tarjetas que envuelvan.

Cambia row→column y predice justify/align.

# 12. Errores frecuentes
- justify = horizontal siempre;
- propiedades del contenedor en hijos;
- flex:1 sin entender;
- order para arreglar DOM;
- overflow por min-width intrínseco.

# 13. Reto
Componente de tarjetas flexible desde móvil a escritorio usando wrap y tamaños intrínsecos.

# 14. Autoevaluación
1. ¿Quién es flex container?
2. ¿Quiénes son items?
3. ¿Qué eje usa justify?
4. ¿Qué cambia con column?
5. ¿Qué hace wrap?
6. ¿Por qué order puede afectar accesibilidad?

# 15. Checklist
- [ ] Distingo container/item.
- [ ] Comprendo ejes.
- [ ] Uso gap/wrap.
- [ ] Comprendo flex shorthand.
- [ ] Mantengo orden lógico.

Continúa con Grid.
