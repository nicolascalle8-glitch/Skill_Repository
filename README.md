# Skill_Repository

Repositorio privado de Nick para skills de Claude y handovers de proyectos.

## Estructura

```
skills/            Skills de Claude (una carpeta por skill)
  auditor-handover/  Audita la saturación de un chat y arma handovers
proyectos/<proyecto>/
  CONTEXTO.md      Lo único que lee el chat nuevo para arrancar (corto, se reescribe)
  HANDOVER.md      Trazabilidad completa, con historial que nunca se borra
  archivos/        Código y textos largos que el CONTEXTO apunta
```

## Cómo se usa

1. En el chat que está fallando, escribe algo como: "audita este chat" o "haz el handover".
2. La skill pregunta el alcance y el proyecto, da un reporte con puntaje y semáforo, y pregunta si arma el handover.
3. Si dices que sí, actualiza el HANDOVER, reescribe el CONTEXTO y te da el mensaje para pegar en el chat nuevo (con el CONTEXTO incluido). El chat nuevo lee solo el CONTEXTO, sin releer el chat viejo.

## Instalar la skill en Claude

La skill se instala en Claude con el archivo `.skill` (botón "Save skill"). Este repo es el respaldo y el historial de versiones.
