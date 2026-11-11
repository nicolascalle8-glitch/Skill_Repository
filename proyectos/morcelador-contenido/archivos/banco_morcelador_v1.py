# banco_morcelador_v1.py  -  Fusion 360 API script
# Banco de pruebas para medir torque de corte del morcelador (Etapa 4)
# + discos de prueba del acople magnético (decidir A1 vs A2).
#
# Cómo correrlo:
#   Fusion 360 > Utilidades > Scripts y complementos > "+" > crear script Python
#   Pega este archivo, guarda y dale "Ejecutar". Crea un diseño nuevo.
#   Para cambiar medidas: Modificar > Cambiar parámetros, edita, y vuelve a correr
#   el script (lee los parámetros que ya existen en el diseño activo).
#
# Todo en mm. Valores marcados "por calibrar" se miden en la pieza real
# (motor, rodamiento, celda de carga, carro del riel) antes de imprimir.

import adsk.core, adsk.fusion, traceback

# nombre, valor, comentario
PARAMS = [
    ('eje_altura',      '45 mm',   'Altura del eje sobre la base [Criterio]'),
    ('rod_D',           '52 mm',   'Rodamiento 6808 diametro exterior (por calibrar)'),
    ('rod_d',           '40 mm',   'Rodamiento 6808 diametro interior (por calibrar)'),
    ('rod_B',           '7 mm',    'Rodamiento 6808 ancho (por calibrar)'),
    ('ajuste_presion',  '0.1 mm',  'Holgura a presion por lado [Supuesto, probeta]'),
    ('ajuste_libre',    '0.3 mm',  'Holgura libre por lado [Supuesto, probeta]'),
    ('motor_D',         '37 mm',   'Motorreductor JGB37 diametro (por calibrar)'),
    ('camisa_L',        '80 mm',   'Largo de la camisa del motor'),
    ('brazo_L',         '50 mm',   'Brazo de palanca: T = F x brazo_L'),
    ('eje_motor_d',     '6 mm',    'Eje del motor (por calibrar)'),
    ('tubo_D',          '11.5 mm', 'Tubo cuchilla, diametro exterior (por calibrar)'),
    ('celda_h',         '12.7 mm', 'Celda de carga 1 kg, alto (por calibrar)'),
    ('carro_h',         '13 mm',   'Riel MGN12 + carro MGN12H, alto total (por calibrar)'),
    ('iman_D',          '10 mm',   'Iman disco N52 diametro (por calibrar)'),
    ('iman_t',          '3 mm',    'Iman disco espesor (por calibrar)'),
    ('acople_pcd',      '30 mm',   'Circulo de imanes del acople de prueba'),
    ('acople_n',        '8',       'Numero de imanes por disco (par, polos alternos)'),
]

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        # siempre un diseno nuevo: nunca toca un archivo abierto de Nick
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = adsk.fusion.Design.cast(app.activeProduct)
        design.designType = adsk.fusion.DesignTypes.ParametricDesignType
        root = design.rootComponent

        # --- parametros de usuario (no pisa los que ya existen) ---
        up = design.userParameters
        for name, val, com in PARAMS:
            if up.itemByName(name) is None:
                unit = '' if name == 'acople_n' else 'mm'
                up.add(name, adsk.core.ValueInput.createByString(val), unit, com)

        def P(name):  # valor en mm
            p = up.itemByName(name)
            return p.value if name == 'acople_n' else p.value * 10.0

        cm = lambda v: v / 10.0
        VI = adsk.core.ValueInput.createByReal
        NEW = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        JOIN = adsk.fusion.FeatureOperations.JoinFeatureOperation
        CUT = adsk.fusion.FeatureOperations.CutFeatureOperation

        def new_comp(name):
            occ = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
            occ.component.name = name
            return occ.component

        def plane(comp, base, off_mm):
            pi = comp.constructionPlanes.createInput()
            pi.setByOffset(base, VI(cm(off_mm)))
            return comp.constructionPlanes.add(pi)

        def pt(sk, x, y, z):
            return sk.modelToSketchSpace(adsk.core.Point3D.create(cm(x), cm(y), cm(z)))

        def box(comp, x0, y0, z0, dx, dy, dz, op=NEW):
            sk = comp.sketches.add(plane(comp, comp.xYConstructionPlane, z0))
            sk.sketchCurves.sketchLines.addTwoPointRectangle(pt(sk, x0, y0, z0), pt(sk, x0 + dx, y0 + dy, z0))
            return comp.features.extrudeFeatures.addSimple(sk.profiles.item(0), VI(cm(dz)), op)

        def cyl_x(comp, x0, y, z, d, length, op=NEW):  # cilindro a lo largo de +X
            sk = comp.sketches.add(plane(comp, comp.yZConstructionPlane, x0))
            sk.sketchCurves.sketchCircles.addByCenterRadius(pt(sk, x0, y, z), cm(d / 2.0))
            return comp.features.extrudeFeatures.addSimple(sk.profiles.item(0), VI(cm(length)), op)

        def cyl_z(comp, x, y, z0, d, length, op=CUT):  # cilindro a lo largo de +Z
            sk = comp.sketches.add(plane(comp, comp.xYConstructionPlane, z0))
            sk.sketchCurves.sketchCircles.addByCenterRadius(pt(sk, x, y, z0), cm(d / 2.0))
            return comp.features.extrudeFeatures.addSimple(sk.profiles.item(0), VI(cm(length)), op)

        H = P('eje_altura')
        xs = 40.0                      # inicio de la camisa del motor
        L = P('camisa_L')
        bw, bt = 72.0, 12.0            # soporte de rodamiento: ancho, espesor

        # 1) Base (imprimir en 2 partes si no cabe; o usar MDF/aluminio)
        c = new_comp('base')
        box(c, 0, -60, -6, 300, 120, 6)

        # 2) Soportes de rodamiento x2 (6808 a presion)
        for i, x0 in enumerate([xs + 6, xs + L - 6 - bt]):
            c = new_comp('soporte_rodamiento_%d' % (i + 1))
            box(c, x0, -bw / 2, 0, bt, bw, H + P('rod_D') / 2 + 6)   # 6 mm de pared arriba
            cyl_x(c, x0, 0, H, P('rod_D') - 0.1, bt, CUT)               # -0.1 mm = interferencia leve [Supuesto]
            for y in (-bw / 2 + 8, bw / 2 - 8):
                cyl_z(c, x0 + bt / 2, y, 0, 4.4, 10)   # M4 a la base

        # 3) Camisa del motor + brazo de palanca (gira dentro de los rodamientos)
        c = new_comp('camisa_motor_brazo')
        cyl_x(c, xs, 0, H, P('rod_d') - 2 * P('ajuste_presion'), L)
        box(c, xs + L / 2 - 6, 0, H - 3, 12, P('brazo_L') + 6, 6, JOIN)
        cyl_x(c, xs - 1, 0, H, P('motor_D') + 2 * P('ajuste_presion'), L + 2, CUT)
        cyl_z(c, xs + L / 2, P('brazo_L'), H - 4, 3.4, 8)        # punto de carga (tornillo M3 / bola)

        # 4) Poste de la celda de carga (la punta del brazo empuja la celda)
        c = new_comp('poste_celda')
        post_top = H - 3 - P('celda_h') - 2.0                    # 2 mm de luz a la punta
        box(c, xs + L / 2 - 75, P('brazo_L') - 10, 0, 20, 20, post_top)
        for dx in (5.0, 15.0):                                   # M4, separacion 10 mm (por calibrar)
            cyl_z(c, xs + L / 2 - 75 + dx, P('brazo_L'), 0, 4.4, post_top + 1)

        # 5) Porta-tubo (une el eje del motor con el tubo cuchilla)
        c = new_comp('porta_tubo')
        xh = xs + L + 15.0                                       # eje sobresale ~15 mm (por calibrar)
        cyl_x(c, xh, 0, H, 26, 32)
        cyl_x(c, xh - 1, 0, H, P('eje_motor_d') + 2 * P('ajuste_presion'), 13, CUT)
        cyl_x(c, xh + 12, 0, H, P('tubo_D') + 2 * P('ajuste_presion'), 21, CUT)
        cyl_z(c, xh + 6, 0, H - 14, 2.8, 28)                     # prisionero M3 al eje (roscar)
        cyl_z(c, xh + 24, 0, H - 14, 2.8, 28)                    # prisionero M3 al tubo (roscar)

        # 6) Prensa del tejido sobre carro MGN12H (avanza hacia la cuchilla)
        c = new_comp('prensa_tejido')
        xc = xh + 32 + 60                                        # 60 mm de carrera libre
        z0 = P('carro_h')
        box(c, xc, -30, z0, 60, 60, H + 25 - z0)
        box(c, xc - 1, -18, H - 18, 46, 36, 36, CUT)             # bolsillo abierto hacia la cuchilla
        for dx in (20.0, 40.0):
            for dy in (-10.0, 10.0):                             # patron 20x20 M3 del carro
                cyl_z(c, xc + dx, dy, z0, 3.4, 12)

        # 7) Discos de prueba del acople magnetico (A1 vs A2), fuera del banco
        n = int(round(P('acople_n')))
        import math
        for i, name in enumerate(['acople_motriz', 'acople_conducido']):
            c = new_comp(name)
            x0 = 20.0 + i * 15.0
            cyl_x(c, x0, 0, -60, P('acople_pcd') + P('iman_D') + 6, 8, NEW)   # fuera de la base (y=0, z=-60)
            for k in range(n):
                a = 2 * math.pi * k / n
                y = P('acople_pcd') / 2 * math.cos(a)
                z = -60 + P('acople_pcd') / 2 * math.sin(a)
                cyl_x(c, x0 + 8 - P('iman_t') - 0.2, y, z, P('iman_D') + 2 * P('ajuste_presion'), P('iman_t') + 0.3, CUT)
            cyl_x(c, x0 - 1, 0, -60, P('eje_motor_d') + 2 * P('ajuste_presion'), 10, CUT)

        ui.messageBox('Listo: banco_morcelador_v1 creado.\nRevisa piezas "por calibrar" antes de imprimir.')
    except:
        if ui:
            ui.messageBox('Error:\n{}'.format(traceback.format_exc()))
