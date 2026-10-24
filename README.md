# Skill_Repository

Repositorio privado de Nick para skills de Claude y handovers de proyectos.

## Estructura

```
skills/            Skills de Claude (una carpeta por skill)
  auditor-handover/  Audita la saturación de un chat y arma handovers
proyectos/         Un HANDOVER.md por proyecto, con historial que nunca se borra
```

## Cómo se usa

1. En el chat que está fallando, escribe algo como: "audita este chat" o "haz el handover".
2. La skill pregunta el alcance y el proyecto, da un reporte con puntaje y semáforo, y pregunta si arma el handover.
3. Si dices que sí, actualiza `proyectos/<proyecto>/HANDOVER.md` y te da el mensaje para pegar en el chat nuevo.

## Instalar la skill en Claude

La skill se instala en Claude con el archivo `.skill` (botón "Save skill"). Este repo es el respaldo y el historial de versiones.
