# Corridas programadas (sin Nick al frente)

Léelo cuando la skill corre desde una automatización de Perplexity, o cuando Nick pide
crear o cambiar esas corridas (para crearlas, usa la skill `automations`).

Hay dos corridas:

- **Diaria — sincronizar.** Solo la sección "Sincronizar con GitHub" (ver
  `references/sincronizar.md`). Antes, carga por nombre las skills guardadas de Nick. Si
  no hubo nada que subir, no hay commit, ni entrada, ni aviso. Si algo quedó bloqueado o en
  conflicto, manda una notificación a Nick con eso.
- **Semanal — revisión.** Lo de abajo.

En la revisión semanal nadie responde preguntas:

- Primero sincroniza (eso sí se aplica solo). Luego haz los pasos 1 a 5 y 7. En el paso 6
  no apliques nada: todo queda como PROPUESTA.
- Si desde el último reporte no hubo sesiones nuevas ni cambios en el repo, no hagas
  reporte: deja solo una línea en la bitácora ("Revisión semanal: sin actividad nueva").
- Al final manda una notificación a Nick (skill `perplexity-platform`) con el resumen corto
  del reporte (las 4 respuestas y las propuestas) y dónde quedó. Si el semáforo es rojo,
  que sea lo primero que diga.
