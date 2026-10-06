# Proyecto: sitio informativo de una iniciativa ficticia

[Lección](README.md) · [Índice](../README.md) · [Solución de referencia](../ejemplos/sitio-final/README.md)

## Elige un propósito

Diseña una biblioteca, club de ciencia o exposición comunitaria ficticia. Debe ayudar a una persona a conocer actividades y encontrar información específica. No utilices una institución real sin autorización ni copies datos personales.

## Requisitos funcionales

- Al menos tres páginas con navegación coherente y página actual identificada.
- Inicio presenta propósito, audiencia y acciones hacia contenido real del sitio.
- Una página de actividades incluye al menos tres actividades, materiales y horario tabular cuando corresponda.
- Una página permite practicar un formulario con etiquetas y validación. Si no tiene backend, indica el alcance y usa datos ficticios; no prometas envío.
- Hay un recorrido de ida y regreso entre páginas y destinos internos.
- Todos los recursos necesarios pertenecen al proyecto o tienen una dependencia externa explícita y válida.

## Requisitos de presentación y acceso

Usa CSS organizado, tokens y al menos un componente reutilizado. Selecciona flujo, Flex o Grid por la relación del contenido. Mantén orden DOM lógico, foco visible, alternativas de imagen, labels y encabezados adecuados. Prueba ancho estrecho de 320 px CSS, uno intermedio y uno amplio, además de ampliación al 200%. Si una tabla necesita desplazarse, hazlo en su región sin perder encabezados.

## Etapas

1. Redacta propósito, audiencia y mapa de páginas.
2. Dibuja wireframes estrecho/amplio y define el orden de lectura.
3. Construye HTML comprensible sin CSS.
4. Define sistema visual y componentes.
5. Resuelve distribución y contenido variable.
6. Verifica navegación, formularios y teclado.
7. Mide recursos, aplica una mejora relevante y compara bajo las mismas condiciones.
8. Publica en hosting estático y comprueba la URL pública.
9. Completa README y registro de pruebas.

## Casos de aceptación

| Caso | Resultado esperado |
|---|---|
| Abrir página secundaria directamente | Carga completa, sin depender de haber pasado por Inicio |
| Llegar a una actividad desde Inicio | Destino correcto y contenido identificable |
| Recorrer con teclado | Todas las acciones disponibles, foco visible y orden lógico |
| Formulario inválido | No se trata como envío válido; se mantiene acceso a los controles |
| Formulario válido de demostración | Navegación prevista y explicación honesta del alcance |
| Texto largo y zoom | Sin recorte de información ni pérdida de acciones |
| Recursos bajo HTTP | Sin 404 de recursos necesarios |
| CSS desactivado | Contenido y relaciones comprensibles |
| Preferencia reduce | Movimiento prescindible desactivado o reducido |

## Entrega y revisión propia

Conserva código, recursos, wireframes, URL pública y [plantilla de documentación](PLANTILLA_PROYECTO.md) completada. Evalúa con [rúbrica](RUBRICA.md) y [checklist](CHECKLIST.md). Si una comprobación no pudo realizarse, registra qué falta; no la marques como aprobada.

[Consultar solución razonada](SOLUCIONES.md) · [Volver al índice](../README.md)
