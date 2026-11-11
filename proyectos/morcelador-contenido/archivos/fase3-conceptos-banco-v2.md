# Morcelador contenido – Phase 3: concepts and bench rig (v2)

Nov 10, 2026 · Draft for Nick and Dr. Calle · CONFIDENTIAL – do not share before the SIC filing

Tags: **[Dato]** = from the Phase 1 report with a source · **[EST]** = my estimate, must be measured · **[Criterio]** = engineering judgment.

## 1. What we are designing

A hand-held, battery-powered morcellator that only cuts inside a containment bag, for laparoscopic myomectomy and hysterectomy. First market: Colombia (INVIMA registration, SIC patent).

| # | Spec | Target used in this phase (v2, with Dr. Calle's answers) |
|---|---|---|
| 1 | Hand-held, wireless | No cable, no console, no foot pedal. Battery in the handpiece. **Lighter than his current handpiece** (he finds it heavy). |
| 2 | Partially or fully disposable | Compare both (Concept A vs B). |
| 3 | Contained / in-bag | The blade cannot run unless it is inside a bag that is in place. |
| 4 | Cost | **Handpiece (the device, bought new) < 2,000,000 COP** (≈ USD 620 at TRM 3,228.26, 6 Nov 2026) [Dato]. Disposables are sold separately, with their own price. |
| 5 | INVIMA + patentable in Colombia | Aim for class IIa [Dato: likely class under Decreto 4725/2005]. Novelty is in the combination cartridge + bag + interlock, because a cordless morcellator alone is prior art (LiNA EP 2593025) [Dato]. |
| 6 | **Port size (new)** | **Everything that enters the abdomen fits a 12 mm trocar** (Dr. Calle). Blade tube ≈ 11–11.5 mm outer diameter [Criterio]. |
| 7 | **Fragments (new)** | No pieces left in the cavity, and no stopping to search for them (his main complaint). |

## 2. Concept A – Sealed core + single-use sterile kit (recommended)

**How it works.** A sealed reusable core (motor, gearbox, battery, electronics) is never sterilized. In the OR it is dropped into a sterile single-use shell using a transfer shield, the same method Stryker uses for batteries [Dato]. The shell has a sealed front wall. Torque passes through that wall with a face magnetic coupling: a magnet rotor on the core side, a magnet rotor in the disposable cartridge. Nothing goes through the wall, so the seal is never broken.

**Reusable core (non-sterile, wiped down):**

- BLDC motor + planetary gearhead, Li-ion pack (2S–3S) with BMS, motor driver + MCU, Hall sensors.
- Housing sealed to IP68 [Criterio], cleaned with a hospital disinfectant wipe between cases.
- Charging: inductive (Qi-type) coil on a dock outside the sterile field. No metal contacts on the housing [EST: no source found, needs validation].
- Driving magnet rotor behind the front face.

**Single-use sterile kit (EtO or gamma):**

- Clamshell shell + transfer shield + latch + gasket. **The outside of the shell is the only surface the surgeon touches**; the core is loaded by a non-sterile person (circulating nurse) and the scrub closes the lid, so sterile gloves never touch the wiped-down core (Dr. Calle's condition).
- Cartridge: driven magnet rotor, **≈ 11–11.5 mm guarded rotating blade tube** (fits the 12 mm trocar), tenaculum channel.
- Containment bag **already sealed to the cartridge collar** at the factory, rolled to pass the 12 mm port: no separate bag port, less trocar friction on the bag (main cause of bag damage in studies [Dato]).
- **All fragments stay in the bag**, so nothing falls into the cavity and there is nothing to search for afterwards.
- **Bag-in-place interlock:** a small magnet in the bag collar is sensed by a Hall sensor in the core, through the shell wall. No signal = motor won't start.
- Option: cartridge ID tag (NFC) read through the wall, so only a fresh kit runs [Criterio].

**Where the coupling goes – open decision:**

| Option | Coupling torque | Pros | Cons |
|---|---|---|---|
| A1 – gearbox in the core, coupling at the blade side | ≈ 0.11–0.33 N·m (blade torque × 2 margin, 11 mm tube) [EST] | Cheap disposable (no gears). Coupling slips free on a blade jam = hardware torque limit that protects the bag. | Magnets about 40–45 mm outer diameter (KTR: 0.15 N·m at 38 mm, 1 N·m at 53 mm) [Dato, vendor] – fits a handpiece body. |
| A2 – coupling at motor speed, gear stage in the cartridge | ≈ 10× smaller torque with a 10:1 stage [EST] | Small, light coupling. | Plastic gear stage thrown away each case; less clear torque limit. |

I lean to **A1** [Criterio]. Final choice after the bench test gives the real torque.

## 3. Concept B – Fully disposable

Same cartridge + bag + interlock, but motor, battery and electronics inside one single-use unit (like LiNA Xcise [Dato]).

- Pros: no cleaning validation, no transfer step, no charging dock, simpler INVIMA file.
- Cons: motor + battery + electronics thrown away every case (cost and e-waste); battery must survive EtO/gamma and shelf life; closest prior art is LiNA's patent.

## 4. Scoring against the specs

Scale 1–5 (5 = best). [Criterio].

| Spec | Concept A (sealed core + kit) | Concept B (fully disposable) |
|---|---|---|
| 1 Hand-held, wireless, light | 5 | 5 |
| 2 Disposable / ecological | 4 – only shell, blade, bag thrown away | 2 – motor and battery thrown away |
| 3 Contained in-bag | 5 – bag pre-joined + interlock | 5 – same |
| 4 Device < 2M COP | 4 – core with commodity parts est. USD 100–250 [EST], under the USD 620 cap; premium Maxon parts (USD 330–650) [EST] don't fit | 2 – the device is thrown away each case, so the cap applies every case: est. USD 80–200 per case [EST] |
| 5 INVIMA + patent | 4 – IIa likely; extra cleaning/transfer validation; strong combination claim | 4 – IIa likely; simpler file; weaker novelty vs LiNA |
| **Total** | **22** | **18** |

**Recommendation:** Concept A, pending Dr. Calle's OK.

## 5. First numbers (to be replaced by bench data)

All [EST], checked with a Python script.

- Blade radius r = 5.5 mm (≈ 11 mm tube). Cutting force assumed 10–30 N → **T = 0.055–0.165 N·m**.
- At 1000 rpm: shaft power 5.8–17.3 W; electrical with 65 % efficiency **9–27 W**.
- Battery for 30 min of continuous cutting at 27 W: **≈ 13 Wh**. A 3S pack of 2.5 Ah cells gives about 27 Wh (2× margin); a 2S pack may be enough, which helps weight.
- **Trade-off:** an 11 mm tube removes about half the tissue per turn of a 15 mm tube (inner area ratio ≈ 0.55). Speed has to come from rpm, a continuous peel and a good tenaculum feed.
- **The cutting force drives everything.** No public data exist for fibroid coring torque. That is why the bench rig comes next.

## 6. Bench rig to measure cutting torque

**Goal:** measure torque, speed, feed force and g/min for an ≈ 11 mm rotating tube in ex vivo tissue. Run a 15 mm tube once as reference.

**Tissue:** ex vivo animal tissue (beef heart, beef tongue). Real fibroid tissue only with ethics committee and pathology approval.

**Setup:**

1. Motor cradle dynamometer: motor + gearhead in two bearings; 50 mm lever arm on a 1 kg load cell (0.25 N·m = 5 N).
2. Blades: ≈ 11–11.5 mm stainless tube (main) and 15–16 mm tube (reference), internal sharpened bevel.
3. Feed: tissue in a 3D-printed clamp on a linear rail; second load cell for push force.
4. Speed: Hall sensor + magnet on the shaft.
5. Logging: ESP32 + 2× HX711, serial to Python/MATLAB, 50–100 Hz.
6. Safety: blade guard, clear PETG shield, emergency stop, gloves.

**Test matrix:** 300 / 600 / 1000 / 1500 rpm × feed force 5 / 10 / 20 N × 3 repeats. Weigh tissue before and after for g/min.

**Parts to print (X2D / K2 Pro):** motor cradle, lever arm, tissue clamp, rail carriage, shield frame. Run them through puerta-fabricacion first.

## 7. Dr. Calle's answers (2026-11-10)

1. **Cost cap:** applies to each device (handpiece) bought new. Disposables sold separately.
2. **Port:** largest trocar 12 mm.
3. **Blade:** rotating blade chosen.
4. **Today:** old corded morcellator; heavy, slow, fibroid doesn't come out in one strip, fragments fall in the cavity. → Targets: light, fast, continuous strip, all fragments kept in the bag.
5. **Sterile shell:** accepted if the shell is sterile and his gloves never touch the wiped-down core.

**Still to ask:** typical and largest fibroid size, and current morcellation time per case.
