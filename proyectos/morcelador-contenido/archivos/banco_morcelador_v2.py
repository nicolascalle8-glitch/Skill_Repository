import adsk.core, adsk.fusion, math

# banco_morcelador_v2 - banco para medir el torque de corte (motor nuevo, Perplexity 2026-11-11).
# Crea un diseno NUEVO. Todo en mm. Eje del motor = X, a la altura eje_altura sobre la base.
# Cambios frente a v1:
#  - Motor clase 36-37 mm: NFP-36GP-555 1260# (D36, eje 8) por defecto; Pololu #4748: motor_D 37, eje 6.
#  - Rodamientos 6809 (45x58x7): con 6808 (ID 40) la camisa quedaba con pared de 1,3-1,8 mm.
#  - Motor sujeto con placa frontal + 3 prisioneros M3 radiales (montaje del motor NO ENCONTRADO).
#  - brazo_L 80: con el bloqueo del NFP (~0,69-0,77 N.m) la celda de 1 kg ve <= ~1 kg.
#  - Tubo de prueba 12x0,5; discos de acople con circulo D34 (igual que el v3).

PARAMS = [
    ('eje_altura', '45 mm', 'Altura del eje sobre la base [Criterio]'),
    ('rod_D', '58 mm', 'Rodamiento 6809 diametro exterior (por calibrar)'),
    ('rod_d', '45 mm', 'Rodamiento 6809 diametro interior (por calibrar)'),
    ('rod_B', '7 mm', 'Rodamiento 6809 ancho (por calibrar)'),
    ('ajuste_presion', '0.1 mm', 'Holgura a presion por lado [Supuesto, probeta]'),
    ('ajuste_libre', '0.3 mm', 'Holgura libre por lado [Supuesto, probeta]'),
    ('motor_D', '36 mm', 'NFP-36GP-555 D36 (Pololu #4748: 37) (por calibrar)'),
    ('motor_cara_hueco', '28 mm', 'Hueco de la placa frontal para el resalte del motor (por calibrar)'),
    ('camisa_L', '80 mm', 'Largo de la camisa del motor'),
    ('brazo_L', '80 mm', 'Brazo de palanca: T = F x brazo_L'),
    ('eje_motor_d', '8 mm', 'Eje NFP 8 mm (Pololu: 6 mm) (por calibrar)'),
    ('tubo_D', '12 mm', 'Tubo de prueba 304 12x0,5'),
    ('celda_h', '12.7 mm', 'Celda de carga 1 kg, alto (por calibrar)'),
    ('carro_h', '13 mm', 'Riel MGN12 + carro MGN12H, alto total (por calibrar)'),
    ('iman_D', '10 mm', 'Iman N52 10x3'), ('iman_t', '3 mm', 'Iman N52 10x3'),
    ('acople_pcd', '34 mm', 'Circulo de imanes (igual que el v3)'),
]


def run(_context: str):
    app = adsk.core.Application.get()
    app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    design = adsk.fusion.Design.cast(app.activeProduct)
    design.designType = adsk.fusion.DesignTypes.ParametricDesignType
    root = design.rootComponent
    up = design.userParameters
    for n, v, com in PARAMS:
        if up.itemByName(n) is None:
            up.add(n, adsk.core.ValueInput.createByString(v), 'mm', com)
    P = lambda n: up.itemByName(n).value * 10.0
    cm = lambda v: v / 10.0
    VI = adsk.core.ValueInput.createByReal
    NEW = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
    JOIN = adsk.fusion.FeatureOperations.JoinFeatureOperation
    CUT = adsk.fusion.FeatureOperations.CutFeatureOperation
    AX = {'x': 0, 'y': 1, 'z': 2}

    def comp(name):
        o = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        o.component.name = name
        return o.component

    def sketch_at(c, axis, a_world, L):
        bp = {'x': c.yZConstructionPlane, 'y': c.xZConstructionPlane, 'z': c.xYConstructionPlane}[axis]
        nrm = bp.geometry.normal
        s = [nrm.x, nrm.y, nrm.z][AX[axis]]
        start = a_world if s > 0 else a_world + L
        pi = c.constructionPlanes.createInput()
        pi.setByOffset(bp, VI(cm(start * s)))
        pl = c.constructionPlanes.add(pi)
        pl.isLightBulbOn = False
        return c.sketches.add(pl), start

    def p3(sk, x, y, z):
        return sk.modelToSketchSpace(adsk.core.Point3D.create(cm(x), cm(y), cm(z)))

    def W(axis, a, u, v):
        return {'x': (a, u, v), 'y': (u, a, v), 'z': (u, v, a)}[axis]

    def ext(c, prof, L, op):
        inp = c.features.extrudeFeatures.createInput(prof, op)
        inp.setDistanceExtent(False, VI(cm(L)))
        if op != NEW:   # solo cuerpos de este componente
            inp.participantBodies = [c.bRepBodies.item(i) for i in range(c.bRepBodies.count)]
        return c.features.extrudeFeatures.add(inp)

    def cyl(c, axis, a0, u, v, d, L, op=NEW):
        sk, s = sketch_at(c, axis, a0, L)
        sk.sketchCurves.sketchCircles.addByCenterRadius(p3(sk, *W(axis, s, u, v)), cm(d / 2.0))
        return ext(c, sk.profiles.item(0), L, op)

    def box(c, x0, y0, z0, dx, dy, dz, op=NEW):
        sk, s = sketch_at(c, 'z', z0, dz)
        sk.sketchCurves.sketchLines.addTwoPointRectangle(p3(sk, x0, y0, s), p3(sk, x0 + dx, y0 + dy, s))
        return ext(c, sk.profiles.item(0), dz, op)

    H = P('eje_altura'); xs = 40.0; L = P('camisa_L')
    ap, al = P('ajuste_presion'), P('ajuste_libre')
    bw, bt = P('rod_D') + 20, 12.0
    yb = P('brazo_L') + 20

    c = comp('base')                                   # imprimir en 2 o usar MDF
    box(c, 0, -60, -6, 300, 60 + yb, 6)

    for i, x0 in enumerate([xs + 6, xs + L - 6 - bt]):
        c = comp('soporte_rodamiento_%d' % (i + 1))
        box(c, x0, -bw / 2, 0, bt, bw, H + P('rod_D') / 2 + 6)
        cyl(c, 'x', x0 - 0.1, 0, H, P('rod_D') - 0.1, bt + 0.2, CUT)    # 6809 a presion (-0,1)
        for y in (-bw / 2 + 6, bw / 2 - 6):
            cyl(c, 'z', -0.1, x0 + bt / 2, y, 4.4, 10, CUT)            # M4 a la base

    c = comp('camisa_motor_brazo')
    cyl(c, 'x', xs, 0, H, P('rod_d') - 2 * ap, L)
    box(c, xs + L / 2 - 6, 0, H - 3, 12, P('brazo_L') + 6, 6, JOIN)
    cyl(c, 'x', xs + L, 0, H, P('rod_d') - 2 * ap, 3, JOIN)          # placa frontal (tope del motor)
    cyl(c, 'x', xs - 0.1, 0, H, P('motor_D') + 2 * ap, L + 0.1, CUT)
    cyl(c, 'x', xs + L - 0.1, 0, H, P('motor_cara_hueco'), 3.2, CUT)
    cyl(c, 'z', H - 4, xs + L / 2, P('brazo_L'), 3.4, 8, CUT)          # punto de carga
    for xp in (xs + 26, xs + L - 26):                                  # prisioneros M3 (roscar 2,5)
        cyl(c, 'z', H, xp, 0, 2.5, P('rod_d') / 2 + 1, CUT)
        cyl(c, 'y', 0, xp, H, 2.5, P('rod_d') / 2 + 1, CUT)
        cyl(c, 'y', -P('rod_d') / 2 - 1, xp, H, 2.5, P('rod_d') / 2 + 1, CUT)

    c = comp('poste_celda')
    post_top = H - 3 - P('celda_h') - 2.0
    box(c, xs + L / 2 - 75, P('brazo_L') - 10, 0, 20, 20, post_top)
    for dx in (5.0, 15.0):                                            # M4, separacion por calibrar
        cyl(c, 'z', -0.1, xs + L / 2 - 75 + dx, P('brazo_L'), 4.4, post_top + 0.2, CUT)

    c = comp('porta_tubo')
    xh = xs + L + 3 + 2
    cyl(c, 'x', xh, 0, H, 26, 32)
    cyl(c, 'x', xh - 0.1, 0, H, P('eje_motor_d') + 2 * ap, 13.1, CUT)
    cyl(c, 'x', xh + 12, 0, H, P('tubo_D') + 2 * ap, 20.1, CUT)
    cyl(c, 'z', H - 14, xh + 6, 0, 2.8, 28, CUT)
    cyl(c, 'z', H - 14, xh + 24, 0, 2.8, 28, CUT)

    c = comp('tubo_prueba_COMPRADO')
    cyl(c, 'x', xh + 12, 0, H, P('tubo_D'), 100)
    cyl(c, 'x', xh + 11.9, 0, H, P('tubo_D') - 1, 100.2, CUT)

    c = comp('prensa_tejido')
    xc = xh + 32 + 60
    z0 = P('carro_h')
    box(c, xc, -30, z0, 60, 60, H + 25 - z0)
    box(c, xc - 0.1, -18, H - 18, 46.1, 36, 36, CUT)
    for dx in (20.0, 40.0):
        for dy in (-10.0, 10.0):
            cyl(c, 'z', z0 - 0.1, xc + dx, dy, 3.4, 12, CUT)

    disc = P('acople_pcd') + P('iman_D') + 4
    for i, name in enumerate(['acople_prueba_motriz', 'acople_prueba_conducido']):
        c = comp(name)
        x0 = 20.0 + i * 15.0
        cyl(c, 'x', x0, 0, -60, disc, 8)
        for k in range(8):
            a = 2 * math.pi * k / 8
            cyl(c, 'x', x0 + 8 - P('iman_t') - 0.2, P('acople_pcd') / 2 * math.cos(a),
                -60 + P('acople_pcd') / 2 * math.sin(a), P('iman_D') + 2 * ap, P('iman_t') + 0.3, CUT)
        cyl(c, 'x', x0 - 0.1, 0, -60, P('eje_motor_d') + 2 * ap, 8.2, CUT)

    for o in root.occurrences:
        cc = o.component
        for i in range(cc.bRepBodies.count):
            cc.bRepBodies.item(i).name = cc.name
    bad = [design.timeline.item(i).name for i in range(design.timeline.count)
           if design.timeline.item(i).healthState != adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState]
    print('timeline:', design.timeline.count, 'no sanas:', bad)
    bodies = adsk.core.ObjectCollection.create()
    for o in root.occurrences:
        for i in range(o.bRepBodies.count):
            bodies.add(o.bRepBodies.item(i))
            bb = o.bRepBodies.item(i).boundingBox
            print(o.component.name, [round(v * 10, 1) for v in (bb.minPoint.x, bb.minPoint.y, bb.minPoint.z,
                                                                bb.maxPoint.x, bb.maxPoint.y, bb.maxPoint.z)])
    ii = design.createInterferenceInput(bodies)
    ii.areCoincidentFacesIncluded = False
    res = design.analyzeInterference(ii)
    print('interferencias:', [(r.entityOne.name, r.entityTwo.name) for r in res])
    vp = app.activeViewport
    cam = vp.camera
    cam.viewOrientation = adsk.core.ViewOrientations.IsoTopRightViewOrientation
    cam.isFitView = True
    vp.camera = cam
