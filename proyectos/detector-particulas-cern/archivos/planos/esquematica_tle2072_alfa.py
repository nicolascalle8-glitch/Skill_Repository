"""Esquemática del detector de partículas DIY de CERN S'Cool LAB (v1.2)
con TLE2072ACP (chip original, DIP-8). Variante alfa (1 x BPX61 sin vidrio).
Basada en DIY_particle_detector/hardware/V1.2 (CERN OHL v1.2)."""
import schemdraw
import schemdraw.elements as elm

schemdraw.use('matplotlib')
d = schemdraw.Drawing(show=False)
d.config(fontsize=10, unit=2.2, lw=1.1)

# ---------------- Sensor ----------------
d += elm.Ground().at((2.4, 0))
pd = elm.Photodiode().at((2.4, 0)).up().length(2.4).label('D1\nBPX61\n(sin vidrio)', loc='bottom', ofst=0.15)
d += pd
d += elm.Line().at(pd.end).up().length(0.6)
d += elm.Line().at((2.4, 3.0)).right().length(4.1)
nin = d.here
d += elm.Dot().at(nin)

# ---------------- Etapa 1: preamplificador de carga (TL074 A) ----------------
op1 = elm.Opamp(leads=True).anchor('in1').at((nin[0] + 1.6, nin[1])).right()
d += elm.Line().at(nin).to(op1.in1) if False else elm.Line().at(nin).right().length(1.6)
d += op1
d += elm.Label().at(op1.in1).label('2', loc='top', ofst=(0.25, 0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op1.in2).label('3', loc='bottom', ofst=(0.25, -0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op1.out).label('1', loc='top', ofst=(-0.3, 0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op1.center).label('U1A\nTLE2072', fontsize=9)

# Realimentación: R3 || (C1 serie C2)
d += elm.Line().at(nin).up().length(2.0)
fb1 = d.here
d += elm.Dot()
d += elm.Resistor().at(fb1).right().tox(op1.out[0] + 0.4).label('R3  40 MΩ', loc='bottom')
d += elm.Line().down().toy(op1.out[1])
d += elm.Dot()
out1 = d.here
d += elm.Line().at(fb1).up().length(1.4)
d += elm.Capacitor().right().length(2.2).label('C1 10 pF')
d += elm.Capacitor().right().tox(op1.out[0] + 0.4).label('C2 10 pF')
d += elm.Line().down().toy(fb1[1])
d += elm.Dot()
d += elm.Line().at(op1.out).right().tox(out1[0])

# Polarización In1+ (≈6,9 V): R1 / R2 / C3 — debajo del amplificador
d += elm.Line().at(op1.in2).left().length(0.7)
d += elm.Line().down().length(2.3)
nb1 = d.here
d += elm.Dot()
d += elm.Resistor().at(nb1).down().label('R2\n15 kΩ', loc='bottom')
d += elm.Ground()
d += elm.Line().at(nb1).right().length(1.6)
d += elm.Capacitor().down().label('C3\n100 nF', loc='bottom')
d += elm.Ground()
d += elm.Resistor().at(nb1).left().length(2.4).label('R1  4,7 kΩ', loc='top')
d += elm.Dot(open=True).label('+9 V', loc='left')
d += elm.Label().at((nb1[0] + 0.15, nb1[1] + 0.3)).label('≈6,9 V', loc='right', halign='left', fontsize=9, color='dimgray')

# Entrada de prueba (opcional), arriba a la izquierda del nodo de entrada
d += elm.Line().at((nin[0] - 0.9, nin[1])).up().length(0.6)
d += elm.Capacitor().up().length(1.6).label('Cprueba 1–2 pF', loc='bottom', fontsize=9)
d += elm.Dot(open=True).label('Entrada de prueba (generador)', loc='top', fontsize=8)
d += elm.Dot().at((nin[0] - 0.9, nin[1]))

# ---------------- Etapa 2: amplificador inversor (TL074 B) ----------------
d += elm.Capacitor().at(out1).right().length(2.2).label('C4\n470 nF')
d += elm.Resistor().right().length(2.4).label('R4\n4,7 kΩ')
n2 = d.here
d += elm.Dot()
op2 = elm.Opamp(leads=True).anchor('in1').at((n2[0] + 1.0, n2[1])).right()
d += elm.Line().at(n2).right().length(1.0)
d += op2
d += elm.Label().at(op2.in1).label('6', loc='top', ofst=(0.25, 0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op2.in2).label('5', loc='bottom', ofst=(0.25, -0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op2.out).label('7', loc='top', ofst=(-0.3, 0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op2.center).label('U1B\nTLE2072', fontsize=9)

d += elm.Line().at(n2).up().length(2.0)
fb2 = d.here
d += elm.Dot()
d += elm.Resistor().at(fb2).right().tox(op2.out[0] + 0.4).label('R5  1 MΩ', loc='bottom')
d += elm.Line().down().toy(op2.out[1])
d += elm.Dot()
out2 = d.here
d += elm.Line().at(fb2).up().length(1.4)
d += elm.Capacitor().right().tox(op2.out[0] + 0.4).label('C6  3,3 nF')
d += elm.Line().down().toy(fb2[1])
d += elm.Dot()
d += elm.Line().at(op2.out).right().tox(out2[0])

# Referencia In2+ (4,5 V): R6 / R7 / C7
d += elm.Line().at(op2.in2).left().length(0.7)
d += elm.Line().down().length(2.3)
nb2 = d.here
d += elm.Dot()
d += elm.Resistor().at(nb2).down().label('R7\n10 kΩ', loc='bottom')
d += elm.Ground()
d += elm.Line().at(nb2).right().length(1.6)
d += elm.Capacitor().down().label('C7\n100 nF', loc='bottom')
d += elm.Ground()
d += elm.Resistor().at(nb2).left().length(2.4).label('R6  10 kΩ', loc='top')
d += elm.Dot(open=True).label('+9 V', loc='left')
d += elm.Label().at((nb2[0] + 0.15, nb2[1] + 0.3)).label('4,5 V = REF', loc='right', halign='left', fontsize=9, color='dimgray')

# ---------------- Salida: filtro R8/C9 + C10/R9 ----------------
d += elm.Line().at(out2).right().length(0.6)
d += elm.Resistor().right().length(2.0).label('R8\n10 kΩ')
n9 = d.here
d += elm.Dot()
d += elm.Capacitor().at(n9).down().label('C9\n6,8 nF', loc='bottom')
d += elm.Ground()
d += elm.Capacitor().at(n9).right().length(2.0).label('C10\n100 nF')
no = d.here
d += elm.Dot()
d += elm.Resistor().at(no).down().label('R9\n2,2 kΩ', loc='bottom')
d += elm.Ground()
d += elm.Line().at(no).right().length(1.2)
d += elm.Dot(open=True).label('SALIDA\n(BNC / jack\nmicrófono)', loc='right', fontsize=9)

# ---------------- Alimentación y amplificadores sin usar ----------------
y0 = -9.0
d += elm.Battery().at((-3, y0)).up().reverse().label('BT1\n9 V', loc='bottom')
bt = d.here
d += elm.Switch().right().label('SW1')
d += elm.Line().right().length(1.0)
vcc = d.here
d += elm.Dot()
d += elm.Line().right().length(2.2)
d += elm.Vdd().label('+9 V')
d += elm.Capacitor(polar=True).at(vcc).down().length(2.2).label('C8\n47 µF', loc='bottom')
d += elm.Ground()
d += elm.Ground().at((-3, y0))

# Alimentación del TLE2072
px = 8.5
d += elm.Dot(open=True).at((px, y0 + 0.4)).label('+9 V', loc='top')
d += elm.Line().down().length(0.8)
p4 = d.here
d += elm.Dot().label('pin 8 (V+)', loc='right', color='firebrick')
d += elm.Capacitor().down().length(2.0).label('C5 100 nF\n(pegado al chip)', loc='bottom', ofst=(0.3,0), fontsize=9)
p11 = d.here
d += elm.Dot().label('pin 4 (GND)', loc='right', color='firebrick')
d += elm.Line().down().length(0.5)
d += elm.Ground()

# Notas
notas = ("Detector de partículas DIY de CERN S'Cool LAB v1.2 con TLE2072ACP (DIP-8, chip original). Variante alfa con 1 x BPX61 sin vidrio.\n"
         "Números rojos = pines del TLE2072 (iguales a la esquemática oficial). Alimentación: pin 8 = +9 V, pin 4 = GND.\n"
         "BPX61: cátodo a la entrada (pin 2), ánodo a GND → polarización inversa ≈ 6,9 V. Confirmar el cátodo con el multímetro antes de soldar.\n"
         "R3 de 40 MΩ: SMD 0805 o resistencia montada vertical, placa limpia (sin flux). Todo dentro de caja metálica totalmente oscura.\n"
         "Fuente: github.com/ozel/DIY_particle_detector (CERN OHL v1.2). Sin probar en hardware.")
d += elm.Label().at((-3, y0 - 5.6)).label(notas, loc='right', halign='left', fontsize=9)

d.save('esquematica_detector_TLE2072_alfa.png', dpi=170)
d.save('esquematica_detector_TLE2072_alfa.pdf')
d.save('esquematica_detector_TLE2072_alfa.svg')
print('ok')
