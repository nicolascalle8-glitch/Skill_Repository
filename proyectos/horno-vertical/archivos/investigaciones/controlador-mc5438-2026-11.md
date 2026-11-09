# Ficha — Controlador Maxthermo MC-5438 (horno vertical)

Hecha: 2026-11-09 (Claude Opus 5.5). Fuentes: Doc de Perplexity (https://docs.google.com/document/d/1lairm_wlDatv9MnkhmZN58nJezyGwt_F1qoirpmV4uI/edit) y Doc de Claude (https://docs.google.com/document/d/1ZswMN3ejfi6rCBTDzbaTeR0DSDLTycyiXrMs7Ydrz3Y/edit), en Drive: Proyectos IA / horno-vertical / investigaciones. Los PDF están en esa misma carpeta. No hace falta volver a leer los Docs: lo útil está aquí.

M = manual oficial Maxthermo "MC-5x38 Operational Manual" (página impresa P.n = página n+1 del PDF). T = copia de Terwin. S = catálogo del distribuidor STI-GAS (igual al catálogo oficial C).
"Verif. Claude" = Claude lo releyó en la fuente el 2026-11-09. "Perplexity" = viene solo de la tabla de Perplexity, con su página, sin releer.

## Lo que importa para B y C

| Dato | Valor | Fuente | Estado |
|---|---|---|---|
| Salida para SSR | Pulso de voltaje. M: 20 VDC/20 mA; C: 24 VDC/20 mA (no coinciden) | M P.23; C 3, 9 | Perplexity |
| Tiempo de ciclo Ct1 | Por defecto 15 s, rango 0~150 s; el manual recomienda 1 s para salida a SSR | M P.4, P.8 | Perplexity |
| Banda P (P1) | 0.0~3000, por defecto 30.0. **Unidad no documentada** (% o °C) | M P.4; T P.3, P.12; S | Verif. Claude |
| Integral i1 / derivativo d1 | Segundos. M: I 0~3600 (defecto 240), D 0~900 (defecto 60). S/C: I 0~7200, D 0~1800 (no coinciden) | M P.4; S | S verif. Claude; M Perplexity |
| Autotune | Parámetro At = yes. Oscila la salida 0/100 % alrededor de SV+SVOF+ATOF; no describe el algoritmo | M P.3, P.10 | Perplexity |
| Modo manual | Existe: parámetro Man (Man1 con memoria, Man2 sin memoria), OutL 0.0~100.0 %, lámpara MAN, arranque "CoLd = manual". **No hay paso a paso** | M P.1, P.3, P.4 | Verif. Claude |
| HOLD (no es manual) | 3 s en la ventana PV/SV detiene la salida; solo con OUTM = 1 o 2 | M P.1; T P.1 | Verif. Claude |
| Soft start | Sout 0~100 % (defecto 30) mientras PV < SSv (defecto 120), con límite StmE 0~10 min | M P.4, P.8 | Perplexity |
| % de salida (MV) | Se muestra (OUT1 %). OutL legible por comunicación (índice 03). Registro histórico: no | M P.1, P.5, P.21 | Perplexity |
| Comunicación | Opcional, código de pedido G: 1 = RS-232, 2 = RS-485. Modbus RTU, 8 bits, sin paridad, 1 de inicio y 1 de parada; 2.4–38.4 kbaud (defecto 9.6 k); Addr 0~31. **Sin USB** | M P.17, P.6; S | Verif. Claude |
| Índices Modbus (hex) | Sv 02, OutL 03, At 04, mAn 05, P1 19, i1 1A, d1 1B, Ct1 1C, Pv 100. **No se documentan los códigos de función ni el tipo de registro** | M P.21 | Índices: Perplexity; lo que falta: verif. Claude |
| Rampa/meseta | 1 perfil de hasta 8 segmentos (1 rampa + 1 meseta = 1 segmento), tiempos 0.00~99.59 h.m, repeticiones 1~1000. **Abrir el nivel PROG "needs to contact distributor"** y exige OUTM = 8 o 9 | M P.18, P.19, P.20; T P.4, P.9; S | Verif. Claude |
| Rampa sin programa | rAmP 0.0~200.0 °/min | M P.3, P.7 | Perplexity |
| Entrada | 1 entrada de medición (inP1) + entrada 2 opcional (SV remoto o CT). Termopar K 0~1200 °C, también J/T/R/E/S/B/N, Pt100. 0.3 % FS, 14 bit, muestreo 300 ms | M P.17, P.23; C 2, 3 | Perplexity |
| Alarmas | MC-5438: máximo 2 ("3-Three set alarm *(except MC-5438)") | S | Verif. Claude |

## Horno "Max-Therma"
No se encontró ningún horno con ese nombre (Perplexity y Claude, 2026-11-09). Hipótesis sin verificar: "Max-Therma" es el controlador. Potencia, voltaje, T máx., dimensiones y ubicación del termopar de control: **no encontrado**. No volver a buscar en la web: sale de la placa del horno o del GIEM.

## Consecuencias para el ensayo térmico (conclusiones de Claude)
1. La corrida en vacío con potencia fija necesita el modo manual: probar en el equipo cómo se entra y cómo se fija OutL.
2. Para registrar u_ssr desde el PC hace falta la opción G = 2 (RS-485) y un adaptador USB–RS-485. Probar con la función Modbus 03 sobre Pv (100) y OutL (03).
3. Si el nivel PROG está bloqueado, la rampa se hace con rAmP.
4. Antes de pasar Kp del modelo al controlador hay que establecer la unidad de P1 en el equipo o con el distribuidor.
5. Para el modelo (control.t_ciclo): 1 s si se sigue la recomendación del manual para SSR; el valor real se lee en el equipo.
