# Datos del café (SCG) y del reactor — 2026-11
Estado: vigente
Pregunta: ¿qué valores con fuente reemplazan los [Supuesto] del modelo del horno vertical (composición, propiedades del lecho, emisividad del tubo, TGA, cinética de lípidos)?
Conclusión: La investigación de Gemini (2026-11-08) sirve como base, pero tiene 6 errores de atribución. Quedaron verificados la composición de Ballesteros 2014, el TGA de Ben Abdallah 2023 y Zuluaga 2024, la cinética TGL, el cp/k del char de Gupta 2003 (madera blanda, no café) y la densidad de Guendouz 2023. Entraron a base.toml solo la celulosa y la lignina (aprobado por Nick, 2026-11-08 21:17).

Cifras clave (verificadas en la REVISIÓN del 2026-11-08 20:11):
- Celulosa 12.40 ± 0.79 % bs [Dato] — Ballesteros et al. 2014, Food Bioprocess Technol 7:3493, Tabla 1 — SCG, método NREL
- Hemicelulosa 39.10 ± 1.94 % bs (manano 19.07, galactano 16.43, arabinano 3.60) — Ballesteros 2014, Tabla 1
- Lignina AIL 17.59 + ASL 6.31 = 23.90 % bs [Dato] — Ballesteros 2014, Tabla 1
- Proteína 17.44, N 2.79, grasa 2.29 (éter de petróleo, 1 h), cenizas 1.30 % bs — Ballesteros 2014, Tabla 1
- Glucano 8.7, AIL 16.8, ASL 1.9, extractivos 29.8 % — Oliva et al. 2022, Biomass Conv. Bioref., doi 10.1007/s13399-022-03173-x (el "hemicelulosa 34.0" de Gemini es una suma suya, no del artículo)
- Elemental: C 46.41, H 6.59, O 42.57, S 0.29, cenizas 1.62 % — Taleb et al. 2020, Sci Rep
- Densidad aparente suelta 387 kg/m³, porosidad 52 % (SCG seco a 105 °C) — Guendouz et al. 2023, ALJEST 9(3)
- TGA a 10 °C/min en N2: Ti/Tm/Tf 171 / 303.8 / 501.7 °C, −Rp 6.83 %/min, pérdida 73.6 % — Ben Abdallah et al. 2023, J Therm Anal Calorim 148:2501 (residuo 20.49 %: el artículo no dice a qué temperatura)
- TGA: picos DTG 74 / 303 / 331 / 396 °C, residuo ≈22 % — Zuluaga et al. 2024, Molecules 29:5866 (los ácidos grasos van en 396 °C)
- TGL → acroleína + 3 FFA: A = 7e12 1/s, E = 45 700 kcal/kmol = 191.2 kJ/mol (×4.184) — Debiagi et al. 2015, Energy Fuels 29:6544, Tabla 5; también Choi et al. 2020, Energies 13:6605
- Choi 2020, Tabla 7, reacciones 20/21: E = 108 kJ/mol, A = 1.2e5 y 2.2e6 1/s
- cp de madera blanda 1172 → 1726 J/kgK; cp de char 768 → 1506 J/kgK (313–713 K); k de char ≈0.0946 W/mK — Gupta, Yang & Roy 2003, Fuel 82:919 (madera blanda, NO café)

Con fuente que existe pero número sin confirmar [Por validar]:
- Lípidos 13.4–21.5 % bs — Atabani et al. 2019, Fuel 254 (revisión; datos de segunda mano)
- Densidad 380 ± 20 kg/m³ (Polvo B) — Sousa & Ferreira 2018, Particuology 43:92
- Emisividad del inoxidable muy oxidado ≈0.67–0.70, ligeramente oxidado 0.33–0.40 — Incropera, Tabla A.11 ("stainless steels, typical", no AISI 304)
- Mussatto 2011 (celulosa 8.6, hemicelulosa 36.7); Semaan 2022 (AIL 21.1, proteína 24); Kordoghli 2026 (son áreas de picos DTG, no composición)

Descartados (no usar):
- Emisividad "NASA CR-1431, Tabla 389": esa tabla no existe en ese documento. Buscar TPRC Vol. 7 (Touloukian & DeWitt 1970).
- "Lignina 27 ± 1 % Klason (Taleb 2020)": es el rendimiento de lignina aislada; no respalda el 28 % de legacy.
- "Aouadja 2023, cp 1400, k 0.038–0.054": el artículo es de Nasr et al. 2023, Energies 16:7440, una revisión de materiales de construcción.
- "k del SCG 0.20 por hilo caliente (Guendouz)": el hilo caliente se usó en el concreto.
- Áreas DTG de la mezcla (Ben Abdallah): mal copiadas; el artículo da 3.9 / 10.5 / 48.9.
- Cardoso 2018 (k 0.096–0.112, cp 905–1245): es grano tostado entero, no SCG.
- Polinomio de cp de char de Gupta citado por Gemini: no reproduce 768 a 313 K (da ≈704).
- Colantoni 2021 (C 68.52, H 11.04): valores raros, no abrió.

Supuestos y límites: no hay k ni cp del lecho de SCG medidos por encima de 150 °C, ni ΔH de la pirólisis del aceite. La composición NREL (Ballesteros) no se mezcla con las fracciones CRECK de Choi 2020 (34.9 / 18.9 / 21.6 / 15.8 % en base con 6.1 % de humedad). El N del GIEM (0.418 % bs) está muy por debajo de la literatura (2.3–2.8 %): hay que confirmarlo.
Vigencia: no vence (propiedades y cinética). Se revisa si el GIEM mide lípidos, densidad o un TGA propio.
Fuentes:
- Investigación — datos del café y del reactor (Gemini) — https://docs.google.com/document/d/1V0surrX-eTDgg7Mrz_901qPwmTgXFKbSZSs947Y-8B8/edit
- Revisión: BITACORA.md, entrada 2026-11-08 20:11
Sale de: chat del subproyecto A (motor nuevo), 2026-11-08; revisión hecha por un agente revisor con WebSearch.
