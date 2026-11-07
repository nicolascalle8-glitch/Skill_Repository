"""Plano adicional: contador de partículas con Arduino Uno.
Usa el amplificador C del TL074 (pines 8, 9, 10) como comparador.
Se conecta al plano principal (esquematica_detector_TL074) en el pin 7 y en GND."""
import schemdraw
import schemdraw.elements as elm

schemdraw.use('matplotlib')
d = schemdraw.Drawing(show=False)
d.config(fontsize=10, unit=2.2, lw=1.1)

# Comparador U1C
op = elm.Opamp(leads=True).at((6, 0)).anchor('in1').right()
d += op
d += elm.Label().at(op.center).label('U1C\nTL074CN\ncomparador', fontsize=9)
d += elm.Label().at(op.in1).label('9', loc='top', ofst=(0.25, 0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op.in2).label('10', loc='bottom', ofst=(0.3, -0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op.out).label('8', loc='top', ofst=(-0.3, 0.05), fontsize=9, color='firebrick')

# Señal: desde Out2 (pin 7) del plano principal
d += elm.Line().at(op.in1).left().length(5.5)
d += elm.Dot(open=True).label('Desde pin 7\n(Out2 de U1B)\n≈4,5 V + pulsos', loc='left', fontsize=9)

# Umbral ajustable: +9 V - R10 - RV1 - R11 - GND (columna debajo del pin 10), cursor al pin 10
colx = op.in2[0] - 3.2
ytop = op.in2[1] - 1.4
d += elm.Vdd().at((colx, ytop)).label('+9 V')
d += elm.Resistor().at((colx, ytop)).down().length(2.0).label('R10\n39 kΩ', loc='bottom')
p = elm.Potentiometer().down().length(2.2).flip().label('RV1 10 kΩ\n(trimmer)', loc='bottom', ofst=0.3)
d += p
d += elm.Resistor().down().length(2.0).label('R11\n39 kΩ', loc='bottom')
d += elm.Ground()
xr = p.tap[0] - 0.7
d += elm.Line().at(op.in2).left().tox(xr)
d += elm.Line().down().toy(p.tap[1])
d += elm.Line().right().tox(p.tap[0])
d += elm.Label().at((xr - 0.15, p.tap[1] + 1.3)).label('Umbral\n≈4,0–5,0 V', loc='left', halign='right', fontsize=9, color='dimgray')

# Salida del comparador -> divisor -> Arduino D2
d += elm.Line().at(op.out).right().length(0.8)
d += elm.Resistor().right().length(2.2).label('R12\n10 kΩ')
nd = d.here
d += elm.Dot()
d += elm.Resistor().at(nd).down().label('R13\n15 kΩ', loc='bottom')
d += elm.Ground()
d += elm.Line().at(nd).right().length(2.0)
ard = elm.Ic(pins=[elm.IcPin(name='D2', side='left'), elm.IcPin(name='GND', side='left')],
             size=(3.6, 2.4), pinspacing=1.2, edgepadH=0.6, label='Arduino Uno\n(USB al PC)', lblsize=10, lblofst=0.4)
ard = ard.at(d.here).anchor('inL1')
d += ard
d += elm.Line().at(ard.inL2).left().length(0.8)
d += elm.Line().up().length(0.6)
d += elm.Label().label('GND del detector', loc='top', fontsize=9)
d += elm.Label().at((ard.inL2[0]-0.9, ard.inL2[1]+0.9)).label('', fontsize=1)
d += elm.Label().at((nd[0] + 0.15, nd[1] + 0.3)).label('máx ≈4,8 V', loc='right', halign='left', fontsize=9, color='dimgray')

# U1D sigue como seguidor
op4 = elm.Opamp(leads=True).at((14, -6.5)).anchor('in2').right()
d += op4
d += elm.Label().at(op4.center).label('U1D\nsin usar', fontsize=8)
d += elm.Label().at(op4.in1).label('13', loc='top', ofst=(0.3, 0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op4.in2).label('12', loc='bottom', ofst=(0.3, -0.05), fontsize=9, color='firebrick')
d += elm.Label().at(op4.out).label('14', loc='top', ofst=(-0.3, 0.05), fontsize=9, color='firebrick')
d += elm.Line().at(op4.in1).up().length(1.0)
d += elm.Line().right().tox(op4.out[0] + 0.4)
d += elm.Line().down().toy(op4.out[1])
d += elm.Line().left().tox(op4.out[0])
d += elm.Line().at(op4.in2).left().length(0.8)
d += elm.Dot(open=True).label('REF 4,5 V', loc='left', fontsize=9)

notas = ("Plano adicional al de 'esquematica_detector_TL074': contador de partículas con Arduino Uno.\n"
         "U1C deja de ser seguidor: se quitan el puente 8–9 y la unión 10–REF, y se conecta como aparece aquí. U1D sigue igual.\n"
         "Cada pulso baja la señal del pin 7 por debajo del umbral → la salida (pin 8) sube → el Arduino cuenta un flanco de subida en D2.\n"
         "Ajuste de RV1: sin fuente, bajar el umbral (pin 10) por debajo de 4,5 V hasta que deje de contar ruido, y dejar un pequeño margen. Si queda sobre 4,5 V cuenta todo el tiempo.\n"
         "R12/R13 bajan la salida del TL074 (≈1,5–7,5 V) a ≈0,9–4,5 V, dentro de lo que acepta el Arduino. GND del Arduino = GND del detector.\n"
         "Sin probar en hardware.")
d += elm.Label().at((-1, -11.5)).label(notas, loc='right', halign='left', fontsize=9)

d.save('esquematica_arduino_contador.png', dpi=170)
d.save('esquematica_arduino_contador.pdf')
print('ok')
