# Plantilla del HANDOVER.md

Copia esta estructura. Las secciones de "Estado actual" se reescriben en cada actualización; el "Historial de actualizaciones" solo crece (entradas nuevas arriba, nunca se borran las viejas).

Escribe en español simple y directo. Frases cortas. Nada de relleno.

---

```markdown
# HANDOVER — <Nombre del proyecto>

Última actualización: <AAAA-MM-DD HH:MM> (Bogotá)
Chat de origen: <nombre o link del chat, si se tiene>
Auditoría más reciente: <🟢/🟡/🔴> <puntaje>/100

---

## 1. Estado actual

### Qué es el proyecto
2–4 frases: qué se está haciendo, para quién y para qué.

### Dónde vamos
Qué está hecho, qué está en curso y cuál es el próximo paso concreto.

### Decisiones vigentes
| Fecha | Decisión | Por qué | Quién la tomó |
|---|---|---|---|
| AAAA-MM-DD | ... | ... | Nick / acordado |

### Hitos
| Fecha | Hito | Estado |
|---|---|---|
| AAAA-MM-DD | ... | ✅ hecho / ⏳ en curso / 🔜 próximo |

### Pendientes
| Pendiente | Responsable | Fecha límite | Bloqueado por |
|---|---|---|---|
| ... | Nick / Claude / tercero | ... | ... |

### Preguntas abiertas
Cosas que no se han decidido y hay que resolver.

### No volver a discutir
Temas ya cerrados que el chat nuevo no debe reabrir, con una línea de por qué.

### Archivos, links y entregables
| Qué | Dónde | Notas |
|---|---|---|

### Preferencias de trabajo para este proyecto
Cómo quiere Nick que se trabaje aquí (formato, tono, lo que no le gusta).

---

## 2. Mensaje de arranque para el chat nuevo

(Bloque corto que se pega como primer mensaje.)

> Vengo de un chat anterior sobre <proyecto>. Lee el HANDOVER en `proyectos/<proyecto>/HANDOVER.md` del repo `nicolascalle8-glitch/Skill_Repository` (o el texto que pego abajo). Estado: <1 frase>. Lo siguiente que necesito: <tarea concreta>. No reabras lo que está en "No volver a discutir".

---

## 3. Historial de actualizaciones

### <AAAA-MM-DD HH:MM> — <🟢/🟡/🔴> <puntaje>/100
- **Nuevo:** decisiones o hitos que aparecieron desde la entrada anterior.
- **Cerrado:** pendientes resueltos.
- **Cambiado:** decisiones reemplazadas (antes → ahora, y por qué).
- **Reemplazado / ya no aplica:** ~~texto viejo~~ → motivo.

### <entrada anterior...>
```

---

## Reglas al actualizar un HANDOVER existente

- La sección 1 se reescribe con lo vigente. Lo que sale de ahí se registra en la entrada nueva del historial (no desaparece sin rastro).
- La sección 3 solo se agrega: la entrada nueva va arriba, las viejas quedan intactas.
- Si una decisión cambió, en "Decisiones vigentes" queda la nueva, y en el historial queda `antes → ahora`.
