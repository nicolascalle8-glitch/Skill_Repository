# Transferencia de energía en bacterias púrpuras (física cuántica + biología) — 2026-05

Estado: histórico (chat cerrado; proyecto de clase de física moderna)
Pregunta: cómo el artículo PNAS 2023 conecta la biología de la fotosíntesis con la física cuántica (Hamiltoniano de Frenkel, Teoría de Förster Generalizada) y qué resultados obtuvo; si un modelo lagrangiano de osciladores acoplados (LH2–LH3) sirve como simulación clásica.
Conclusión: La transferencia entre proteínas antena LH2 ocurre en el régimen intermedio y se describe con la Teoría de Förster Generalizada (MCFT), validada contra HEOM. A menor distancia entre proteínas, transferencia más rápida; los pasos rápidos entre LH2 cercanos aumentan el transporte de larga distancia. Para la parte clásica del proyecto, el teorema de Ehrenfest justifica usar un lagrangiano de osciladores acoplados como analogía.

Cifras clave (tal como se reportaron en el chat; [Por validar] contra el artículo):
- Distancia LH2–LH2 de 25 Å → transferencia en 5.7 ps — Wang et al., PNAS 2023 — dato de 2023
- Distancias de 28–31 Å → 10–14 ps — mismo artículo
- Tiempo calculado con GFT 10.2 ps vs. HEOM 9.1 ps — mismo artículo
- Los pasos rápidos aumentan la distancia de transporte ≈ 15 % — mismo artículo
- Nanodiscos: 17.8 ± 0.1 nm y 20.4 ± 0.2 nm; proteína de cinturón ApoE422K — mismo artículo
- LH2 absorbe ≈ 850 nm, LH3 ≈ 820 nm (Phaeospirillum molischianum) — mismo artículo
- Estructuras cryoEM en el PDB: 7TV3 y 8FB9 — mismo artículo

Ecuaciones usadas:
- Hamiltoniano de Frenkel: H = Σ ε_m |m⟩⟨m| + Σ_{m≠n} J_mn |m⟩⟨n|
- Tasa MCFT (forma de solapamiento): k_D→A = (2π/ħ²) Σ |V_αβ|² ∫ E_D(ω) A_A(ω) dω

Supuestos y límites: las cifras se copiaron del resumen del chat, no se volvieron a leer del artículo. El chat también produjo dos presentaciones (14+3 y 10 diapositivas) que no se guardaron aquí.
Vigencia: teoría y resultados publicados; no vence. Revisar si hay artículos más nuevos antes de citarlo como estado del arte.

Fuentes:
- Wang et al. (2023). Elucidating interprotein energy transfer dynamics within the antenna network from purple bacteria. PNAS. https://doi.org/10.1073/pnas.2220477120
- Renger, T. (2021). Artículo de revisión sobre teoría de transferencia de excitación (PMC8237266): Hamiltoniano de Frenkel, direccionalidad, balance detallado y mención explícita del teorema de Ehrenfest en la sección de teoría. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8237266/

Sale de: https://claude.ai/chat/3b2c4cb1-92a8-464e-8c34-a061c513ab61
