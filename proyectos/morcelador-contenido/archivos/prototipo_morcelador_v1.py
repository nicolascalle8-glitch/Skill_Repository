import adsk.core, adsk.fusion, math

# Prototipo v1 (Concepto A) - modelo para imprimir y verlo fisico.
# Eje X = eje del instrumento; frente (hacia el paciente) = +X. Todo en mm.
# Nucleo reutilizable (motor JGB37 + 2x18650) dentro de carcasa esteril;
# torque pasa por la pared con acople magnetico (8 imanes 10x3 por disco);
# cartucho con tubo de 12 mm, collar de bolsa e iman de enclavamiento.

def run(_context: str):
    app = adsk.core.Application.get()
    app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    design = adsk.fusion.Design.cast(app.activeProduct)
    design.designType = adsk.fusion.DesignTypes.ParametricDesignType
    root = design.rootComponent
    up = design.userParameters
    for n, v, com in [
        ('motor_caja_D', '37 mm', 'JGB37-520 caja reductora (plano vendedor)'),
        ('motor_L', '41 mm', 'JGB37 cuerpo+caja (suma de cotas, por calibrar)'),
        ('motor_pcd', '31 mm', 'Agujeros M3 del motor (hoja generica, por calibrar)'),
        ('iman_D', '10 mm', 'Iman N52 10x3'), ('iman_t', '3 mm', 'Iman N52 10x3'),
        ('acople_pcd', '26 mm', 'Circulo de imanes'),
        ('tubo_D', '12 mm', 'Tubo 304 12x0.5 (Perplexity)'),
        ('celda18650_D', '18.8 mm', '18650 + holgura'),
        ('pared_frontal', '0.8 mm', 'Pared nucleo y pared carcasa (cada una)'),
        ('holgura', '0.3 mm', 'Holgura nucleo-carcasa [Supuesto]')]:
        if up.itemByName(n) is None:
            up.add(n, adsk.core.ValueInput.createByString(v), 'mm', com)
    P = lambda n: up.itemByName(n).value * 10.0
    cm = lambda v: v / 10.0
    VI = adsk.core.ValueInput.createByReal
    NEW = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
    JOIN = adsk.fusion.FeatureOperations.JoinFeatureOperation
    CUT = adsk.fusion.FeatureOperations.CutFeatureOperation

    def comp(name):
        o = root.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        o.component.name = name
        return o.component
    def plane(c, base, off):
        pi = c.constructionPlanes.createInput()
        pi.setByOffset(base, VI(cm(off)))
        return c.constructionPlanes.add(pi)
    def pt(sk, x, y, z):
        return sk.modelToSketchSpace(adsk.core.Point3D.create(cm(x), cm(y), cm(z)))
    def ext(c, prof, L, op):
        # los cortes solo afectan los cuerpos de ESTE componente
        inp = c.features.extrudeFeatures.createInput(prof, op)
        inp.setDistanceExtent(False, VI(cm(L)))
        if op != NEW:
            inp.participantBodies = [c.bRepBodies.item(i) for i in range(c.bRepBodies.count)]
        return c.features.extrudeFeatures.add(inp)
    def box(c, x0, y0, z0, dx, dy, dz, op=NEW):
        sk = c.sketches.add(plane(c, c.xYConstructionPlane, z0))
        sk.sketchCurves.sketchLines.addTwoPointRectangle(pt(sk, x0, y0, z0), pt(sk, x0+dx, y0+dy, z0))
        return ext(c, sk.profiles.item(0), dz, op)
    def cx(c, x0, y, z, d, L, op=NEW):
        sk = c.sketches.add(plane(c, c.yZConstructionPlane, x0))
        sk.sketchCurves.sketchCircles.addByCenterRadius(pt(sk, x0, y, z), cm(d/2))
        return ext(c, sk.profiles.item(0), L, op)
    def cz(c, x, y, z0, d, L, op=CUT):
        sk = c.sketches.add(plane(c, c.xYConstructionPlane, z0))
        sk.sketchCurves.sketchCircles.addByCenterRadius(pt(sk, x, y, z0), cm(d/2))
        return ext(c, sk.profiles.item(0), L, op)
    def ring_pockets(c, x0, z_c, depth):
        r = P('acople_pcd') / 2
        for k in range(8):
            a = 2*math.pi*k/8
            cx(c, x0, r*math.cos(a), z_c + r*math.sin(a), P('iman_D') + 0.2, depth, CUT)

    w = P('pared_frontal'); h = P('holgura')
    disc_D = P('acople_pcd') + P('iman_D') + 3      # 39
    cham_D = disc_D + 1                               # 40
    r_lock = cham_D/2 + 2.5                           # 22.5: sensor Hall / iman de enclavamiento
    x_face = -22.5                                    # cara del motor (hombro)

    # 1) NUCLEO reutilizable (sellado en el producto real)
    c = comp('nucleo_reutilizable')
    cx(c, -70, 0, 0, 50, 70)                          # canon x -70..0
    box(c, -60, -21, -110, 30, 42, 90, JOIN)          # empunadura
    cx(c, -71, 0, 0, P('motor_caja_D') + 0.3, x_face + 71, CUT)   # alojamiento motor -71..x_face
    cx(c, x_face - 0.1, 0, 0, 12, -12.8 - x_face + 0.2, CUT)   # paso del eje
    cx(c, -12.8, 0, 0, cham_D, 12.8 - w, CUT)                  # camara del disco motriz
    for k in range(6):
        a = 2*math.pi*k/6
        cx(c, x_face - 0.1, P('motor_pcd')/2*math.cos(a), P('motor_pcd')/2*math.sin(a), 3.4, 9.9, CUT)
    for y in (-10, 10):
        cz(c, -45, y, -111, P('celda18650_D'), 71)            # 2x 18650
    cz(c, -45, 0, -41, 8, 25)                                  # paso de cables
    cx(c, -10.8, 0, -r_lock, 3.2, 10 - 0.0, CUT)               # bolsillo sensor Hall (A3144)

    c = comp('tapa_nucleo')
    cx(c, -74, 0, 0, 50, 4); cx(c, -74.1, 0, 0, 12, 4.2, CUT)  # agujero interruptor
    c = comp('tapa_baterias')
    box(c, -60, -21, -113, 30, 42, 3)

    # 2) Disco motriz (va en el eje del motor, dentro del nucleo)
    c = comp('disco_motriz')
    cx(c, -9.3, 0, 0, disc_D, 8)
    ring_pockets(c, -1.3 - P('iman_t') - 0.3, 0, P('iman_t') + 0.3)
    cx(c, -9.4, 0, 0, 6.2, 8.2, CUT)
    cz(c, -5.3, 0, -20, 2.8, 20)                               # prisionero M3

    # 3) CARCASA ESTERIL (desechable) + tapa
    c = comp('carcasa_esteril')
    cx(c, -75, 0, 0, 54, 75 + h + w)                           # -75..1.1
    box(c, -75, -23, -116, 47, 46, 96, JOIN)
    cx(c, -76, 0, 0, 50 + 2*h, 76 + h, CUT)                    # hueco canon, deja pared frontal
    box(c, -76, -21 - h, -113 - h, 46 + h, 42 + 2*h, 93 + h, CUT)
    c = comp('tapa_carcasa')
    cx(c, -77, 0, 0, 54, 2); box(c, -77, -23, -116, 2, 46, 96, JOIN)

    # 4) CARTUCHO desechable (disco conducido + tubo + collar de bolsa)
    x0 = h + w + h                                              # 1.4
    c = comp('cartucho')
    cx(c, x0, 0, 0, 54, 25)
    cx(c, x0 - 10, 0, 0, 58, 10, JOIN)                          # falda que abraza la carcasa
    cx(c, x0 - 10.1, 0, 0, 54.4, 10.1, CUT)
    cx(c, x0, 0, 0, cham_D, 10, CUT)                            # camara disco conducido
    cx(c, x0 + 25, 0, 0, 20, 20, JOIN)                          # nariz
    cx(c, x0 + 9.9, 0, 0, P('tubo_D') + 0.6, 35.2, CUT)         # buje del tubo
    cx(c, x0, 0, -r_lock, 3.2, 3, CUT)                          # iman de enclavamiento (bolsa)

    c = comp('disco_conducido')
    cx(c, x0 + 0.3, 0, 0, disc_D, 8)
    ring_pockets(c, x0 + 0.3, 0, P('iman_t') + 0.3)
    cx(c, x0 + 0.2, 0, 0, P('tubo_D') + 0.2, 8.2, CUT)

    c = comp('collar_bolsa')
    cx(c, x0 + 37, 0, 0, 30, 8); cx(c, x0 + 36.9, 0, 0, 20.4, 8.2, CUT)
    cx(c, x0 + 40, 0, 0, 30.2, 2, CUT); cx(c, x0 + 40, 0, 0, 27, 2, JOIN); cx(c, x0 + 39.9, 0, 0, 20.4, 2.2, CUT)  # ranura para amarrar la bolsa

    c = comp('tubo_cuchilla_acero_COMPRADO')
    cx(c, x0 + 0.6, 0, 0, P('tubo_D'), 250); cx(c, x0 + 0.5, 0, 0, P('tubo_D') - 1, 250.2, CUT)

    bad = [design.timeline.item(i).name for i in range(design.timeline.count)
           if design.timeline.item(i).healthState != adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState]
    print('unhealthy:', bad)
    for o in root.occurrences:
        b = o.component.bRepBodies
        bb = b.item(0).boundingBox if b.count else None
        print(o.component.name, b.count, [round(v*10, 1) for v in (bb.minPoint.x, bb.minPoint.y, bb.minPoint.z, bb.maxPoint.x, bb.maxPoint.y, bb.maxPoint.z)] if bb else '')
    vp = app.activeViewport
    cam = vp.camera; cam.viewOrientation = adsk.core.ViewOrientations.IsoTopRightViewOrientation
    cam.isFitView = True; vp.camera = cam
