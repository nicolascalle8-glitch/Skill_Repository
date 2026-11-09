# Plantillas

## 1. Reporte y plan (en la sesión)

```
## Depuración — <fecha>
Alcance: <memoria / archivos del Project / sesiones / hábitos>
Carga por sesión (aprox.): <X> tokens → después del plan: <Y> tokens

### Memoria
| Memoria | Tipo | Problema | Acción |

### Archivos del Project
| Archivo | Tamaño aprox. | Problema | Acción |

### Sesiones
| Sesión (link o nombre) | Grupo | Qué guardar antes |

### Al repo (se guarda antes de borrar nada)
| Archivo nuevo | Sale de |

### Hábitos
1. ...

### Para hacer a mano
- ...
```

Acciones posibles: unir, acortar, mover al repo, marcar vencido, pasar a histórico, borrar.

## 2. Ficha de investigación

Ruta: `proyectos/<proyecto>/archivos/investigaciones/<tema>-<aaaa-mm>.md`

```
# <Tema> — <fecha>
Estado: vigente | VENCIDA <fecha>
Pregunta: <qué se quería saber o decidir>
Conclusión: <2–3 frases>
Cifras clave:
- <dato> — <fuente> — <fecha del dato>
Supuestos y límites: <qué no cubre>
Vigencia: <hasta cuándo sirve y por qué>
Fuentes:
- <título> — <link>
Sale de: <sesión o reporte original, con link>
```

## 3. Memoria de cálculo (mínima)

Ruta: `proyectos/<proyecto>/archivos/calculos/<pieza-o-tema>.md`

Cuando exista `calculo-trazable`, se usa su formato en vez de este.

```
# <Pieza o ejercicio> — <fecha>
Estado: borrador | vigente | histórico
Etapa: <1–6>
Enunciado: <qué se calcula y para qué>

Datos y supuestos:
- <valor y unidad> [Dato | Medido | Norma | Supuesto] — <fuente o porqué>

Ecuaciones: <ecuación> — <libro, edición, número>

Resultados:
- <valor y unidad> [Calculado]

Verificación: <orden de magnitud, unidades, segundo método o caso conocido>
Por validar: <lo que puede cambiar el resultado>
Script u hoja: <ruta o link>
Sale de: <sesión original, con link>
```

## 4. Entrada de bitácora

Formato de la sección 7 de `CONTRATO.md`:

```
### AAAA-MM-DD HH:MM — Perplexity Computer (<modelo>) — HECHO
**Qué:** Depuración <alcance>. Ahorro aprox. <X> tokens por sesión.
**Archivos:** <rutas nuevas o cambiadas>
**Fuentes:** <sesión de la depuración>
**Verificado:** <qué se comprobó>
**Para Nick:** <lo que tiene que hacer a mano>
**Para la siguiente IA:** <dónde quedaron fichas y memorias de cálculo>
```
