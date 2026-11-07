# BITÁCORA — Detector de partículas DIY de CERN

Reglas: CONTRATO.md del repo Skill_Repository. Entradas nuevas arriba. Nada se borra. Esta bitácora es la misma que proyectos/detector-particulas-cern/BITACORA.md en GitHub.

## En curso
- (nada)

## Propuestas sin respuesta
- (ninguna)

---

## Entradas

### 2026-11-06 20:30 — Claude Opus 5.5 — HECHO
**Qué:** Handover 2026-11-06 — amarillo 73/100. Se abre el proyecto en el repo con todo lo del chat del 29 oct: planos TL074 (electrones), TLE2072 + BPX61 (alfa) y contador Arduino; sketch; revisión de valores con hoja de datos TI; calculadora de capacitores en serie. Siguiente tarea: montar y probar la variante alfa (DC → pulso de prueba en pin 1 → pin 7 → SALIDA).
**Archivos:** proyectos/detector-particulas-cern/ (CONTEXTO.md, HANDOVER.md, BITACORA.md, archivos/planos/*.py, archivos/arduino/contador_particulas.ino, archivos/calculos/capacitores_serie.py); registry/DRIVE.yml; proyectos/README.md.
**Fuentes:** chat del 29 oct 2026; diseño oficial github.com/ozel/DIY_particle_detector v1.2; hoja de datos TI TL074; artículo de PhysicsOpenLab.
**Verificado:** los 3 scripts de planos corren y generan PNG/PDF; capacitores_serie.py probado (10 pF + 10 pF = 5 pF). Nada probado en hardware; sketch sin compilar.
**Para Nick:** medir DC de los pines 1, 3, 5 y 7 y mandar foto del osciloscopio con el pulso de prueba; confirmar fuente radiactiva con el profesor.
**Para la siguiente IA:** leer solo CONTEXTO.md para arrancar. No tocar planos existentes: cada versión nueva en archivo aparte. Con punta ×10 el osciloscopio no baja de 20 mV/div.
