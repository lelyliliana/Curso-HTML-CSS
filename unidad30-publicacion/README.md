# Unidad 30 — Publicación de un sitio estático

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

# 4. GitHub Pages — concepto

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
