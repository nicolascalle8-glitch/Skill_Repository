# Plantilla del HANDOVER.md

Copia esta estructura. El HANDOVER es el registro completo para trazabilidad; lo que la sesión nueva lee al arrancar es el CONTEXTO.md (ver `plantilla-contexto.md`), que se destila de aquí. Las secciones de "Estado actual" se reescriben en cada actualización; el "Historial de actualizaciones" solo crece (entradas nuevas arriba, nunca se borran las viejas).

Escribe en español simple y directo. Frases cortas. Nada de relleno.

---

```markdown
# HANDOVER — <Nombre del proyecto>

Última actualización: <AAAA-MM-DD HH:MM> (Bogotá)
Sesión de origen: <nombre o link de la sesión de Perplexity, si se tiene>
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
| ... | Nick / Perplexity / otra IA / tercero | ... | ... |

### Preguntas abiertas
Cosas que no se han decidido y hay que resolver.

### No volver a discutir
Temas ya cerrados que la sesión nueva no debe reabrir, con una línea de por qué.

### Archivos, links y entregables
| Qué | Dónde | Notas |
|---|---|---|

### Preferencias de trabajo para este proyecto
Cómo quiere Nick que se trabaje aquí (formato, tono, lo que no le gusta).

---

## 2. Mensaje de arranque para la sesión nueva

(Bloque corto que se pega como primer mensaje de una sesión nueva de Perplexity o de otra IA.)

> Vengo de una sesión anterior sobre <proyecto>. Para arrancar lee **solo** `proyectos/<proyecto>/CONTEXTO.md` del repo `nicolascalle8-glitch/Skill_Repository` (o el contexto que pego abajo). No releas la sesión vieja ni el HANDOVER completo; abre el HANDOVER o los `archivos/` solo si la tarea lo pide o yo pregunto por algo del pasado. Lo siguiente que necesito: <tarea concreta>. No reabras las decisiones vigentes.
>
> <aquí va pegado el CONTEXTO.md completo>

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
