# Morcelador contenido – Roadmap and guide

Nov 10, 2026 · CONFIDENTIAL until the SIC filing · Companion doc: "Morcelador contenido – Fase 3 concepts and bench rig"

## 1. Navigation chart

Each stage ends in a **gate**: a yes/no check. Don't start the next stage until the gate is passed. ✅ = done · ▶ = now · ⬜ = later.

| # | Stage | Main output | Gate (to move on) | Lead tool | Status |
|---|---|---|---|---|---|
| 0 | Set up | NDA + inventor/ownership agreement, questions answered, Drive folder | Agreement signed by Nick + Dr. Calle; 5 questions answered | Gemini + Nick | ▶ |
| 1 | Research | Phase 1 report | Report delivered | Claude | ✅ |
| 2 | Colombia patent check | List of competitor patents filed in Colombia | Know which patents can block us in Colombia | Comet | ▶ |
| 3 | Concept | Concept A vs B, scored | Dr. Calle approves one concept | Claude (draft ✅) + Dr. Calle | ▶ |
| 4 | Bench test | Cutting torque, speed, g/min on ex vivo tissue | Real torque number with range | Nick builds; Copilot firmware; Claude rig CAD | ⬜ |
| 5 | Sizing | Motor, gearbox, magnetic coupling, battery | Numbers checked a 2nd way (MATLAB) | Claude + Nick | ⬜ |
| 6 | Prototype v1 | Fusion model, printed handpiece + cartridge, phantom bag tests | Cuts inside a bag on the bench, interlock works | Claude (script) + Nick (Fusion, print) | ⬜ |
| 7 | Patent filing | Claims + description, filed at SIC as invention patent | Filing number from SIC | Claude drafts, Perplexity prior art, **patent attorney files** | ⬜ |
| 8 | Company + quality | SAS, ISO 13485-lite QMS, risk file (ISO 14971), design history file | Company exists; design frozen | Gemini (docs) + accountant/consultant | ⬜ |
| 9 | Verification + funding | Bag leak tests, biocompatibility, sterilization, electrical safety; grant applications | Test reports pass | External labs; Gemini drafts grants | ⬜ |
| 10 | INVIMA + launch | Registro or notificación sanitaria, manufacturing partner, first users | INVIMA number issued | Regulatory consultant + Nick | ⬜ |

**Rule:** nothing public (posts, posters, pitches, school projects) before Stage 7 is passed.

## 2. Who does what (to save Claude credits)

| Tool | Use it for | Don't use it for |
|---|---|---|
| **Claude** | Decisions at gates, architecture, calculations, CAD scripts, patent claims, reviewing what the other AIs bring back | Simple lookups, browsing databases, formatting documents |
| **Perplexity** | Quick facts with sources: patents, standards, prices, laws | Clicking through websites |
| **Comet** | Websites with search forms: SIC/SIPI, SECOP II, INVIMA registros, distributor sites | Analysis or design |
| **Gemini** | Everything in Google Drive/Docs: bitácora, agreements, emails to Dr. Calle, design history file, grant forms | Engineering calculations |
| **Copilot** | Code: ESP32 logging firmware, Python/MATLAB data analysis, edits to the Fusion script | Research |

**How to keep it cheap:**

- Come back to Claude only at a gate, with the other AI's output as a file (CSV, PDF, text).
- One Claude chat per stage. When a chat gets long, ask Claude for a handover and open a new chat.
- Claude writes the prompt for the other AI; you paste it and bring back the answer.

## 3. What to do now (Stage 0 and 2)

### 3.1 You – send Dr. Calle the 5 questions

Done (answered 2026-11-10). Still to ask: typical / largest fibroid size and current morcellation time per case.

### 3.2 Gemini – agreement drafts + Drive folder

Done (2026-11-10): folder, bitácora, NDA and inventor/ownership agreement, with corrections. Next: Nick picks options A/B, fills [CONFIRMAR], lawyer review.

### 3.3 Comet – Colombia patent check (retry)

Comet must open SIPI in a real browser tab (the site needs a live session). Prompt is in the Claude doc "Roadmap and guide", section 3.3.

**Bring back to Claude:** Comet's table + Dr. Calle's OK on Concept A. That's the Stage 2 and Stage 3 gate.

## 4. Later stages – short guide

**Stage 4 – Bench test.** Claude writes one Fusion script for the rig (cradle, lever, clamp, rail). Copilot writes ESP32 + HX711 logging code. You build, test on butcher tissue, send the CSV. Gate: torque range in N·m.

**Stage 5 – Sizing.** Claude sizes motor, gearbox, coupling, battery from your data. You check in MATLAB. Gate: both match.

**Stage 6 – Prototype v1.** Claude writes the parametric Fusion script. You iterate in Fusion, print (after `puerta-fabricacion`), test in a bag on a box trainer with tissue phantoms. Gate: cuts in the bag, interlock stops the motor when the bag is off. **No patients.**

**Stage 7 – Patent.** Perplexity updates the prior-art table. Claude drafts claims around: bag sealed to the cartridge collar + magnet interlock sensed through the shell + magnetic torque through the same wall. A Colombian patent attorney reviews and files as an invention patent (can be converted to a utility model later, Decision 486 Art. 35). Gate: SIC filing number. After this, you can talk about it.

**Stage 8 – Company + quality.** Create the SAS (also needed for Ruta N grants and for INVIMA). Gemini sets up the design history file and risk file templates in Drive. Gate: design frozen (a design change after INVIMA filing needs a new registration).

**Stage 9 – Verification + funding.** Bag leak tests (FDA 2023 bag test list as reference), biocompatibility, sterilization validation with a contract sterilizer, electrical/battery safety at a test lab. Apply to Minciencias / iNNpulsa / Ruta N calls. Gate: test reports pass.

**Stage 10 – INVIMA + launch.** A regulatory consultant files (class IIa today, or notificación sanitaria if the new decree is issued). Manufacturing partner with ISO 13485. First users: Dr. Calle and colleagues. Gate: INVIMA number.

## 5. Open items

| Item | Blocks | Who |
|---|---|---|
| Competitor patents filed in Colombia | Stage 3, 7 | Comet |
| Fibroid size + current morcellation time | Speed target | Dr. Calle |
| Real cutting torque | Stage 5 | Bench test |
| Real prices (Storz, BOWA, LiNA distributors) | Business case | Comet / Nick asks distributors |
| Final status of the decree replacing 4725 | Stage 10 | Perplexity, every 2–3 months |
