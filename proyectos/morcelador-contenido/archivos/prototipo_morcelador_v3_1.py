import adsk.core, adsk.fusion, math

# Prototipo v3.1 - morcelador contenido (v3 + fijaciones).
# Cambios v3.1: nervios anillo/tubo (arrastre de la cuchilla), anillo E en el cubo del anillo, anillo DIN 471
# detras de la corona, cubo con prisionero M3 en el pinon, 8 tornillos M3 + insertos entre mitades del mango,
# clic (detent) en las 2 bayonetas. Motor 2 mm mas atras para dar espacio al anillo DIN 471.
# Prototipo v3 - morcelador contenido. Crea un diseno NUEVO (no toca archivos de Nick).
# Eje X = eje del instrumento; +X = hacia el paciente. Z+ arriba. Todo en mm.
# x = 0 es la cara frontal del mango.
# Mango sellado: rotor hueco (8 imanes N52 10x3, circulo D34) en 2 rodamientos 6805,
#   engranaje recto m1 43/17 desde motor fuera del eje (z = -30), canal central libre.
# Funda: adaptador rigido (bayoneta 2 pernos, 30 grados) + ventana + tunel + valvula trasera.
# Cartucho: bayoneta sobre el adaptador, anillo conducido + tubo cuchilla, buje, collar de bolsa,
#   iman de enclavamiento frente al sensor Hall del mango.
# Lo marcado "por calibrar" se mide en la pieza comprada antes de imprimir.

PARAMS = [
    ('motor_D', '28 mm', 'Motor del mango, diametro (por calibrar: Perplexity Uso B v2)'),
    ('motor_L', '60 mm', 'Motor del mango, largo cuerpo+caja sin eje (por calibrar)'),
    ('motor_eje_d', '4 mm', 'Eje del motor del mango (por calibrar)'),
    ('motor_boss_D', '8 mm', 'Resalte frontal del motor (por calibrar)'),
    ('mod', '1 mm', 'Modulo de los engranajes rectos'),
    ('z_corona', '43', 'Dientes corona (rotor)'),
    ('z_pinon', '17', 'Dientes pinon (motor); relacion = 43/17 = 2,53'),
    ('rod_D', '37 mm', 'Rodamiento 6805 (61805) diametro exterior (por calibrar)'),
    ('rod_d', '25 mm', 'Rodamiento 6805 diametro interior (por calibrar)'),
    ('rod_B', '7 mm', 'Rodamiento 6805 ancho (por calibrar)'),
    ('iman_D', '10 mm', 'Iman N52 10x3'), ('iman_t', '3 mm', 'Iman N52 10x3'),
    ('iman_pcd', '34 mm', 'Circulo de imanes motrices y conducidos'),
    ('iman_lock_D', '5 mm', 'Iman de enclavamiento (por calibrar)'),
    ('iman_lock_t', '2 mm', 'Iman de enclavamiento (por calibrar)'),
    ('pared', '0.8 mm', 'Pared frontal del mango (2 perimetros)'),
    ('funda_t', '0.4 mm', 'Ventana de la funda (real: pelicula ~0,3; impresa: 0,4)'),
    ('luz_giro', '0.2 mm', 'Luz axial entre pieza que gira y pared fija [Supuesto]'),
    ('tubo_D', '12 mm', 'Tubo 304 12x0,5 de prueba (real <= 11,5)'),
    ('tubo_d', '11 mm', 'Diametro interior del tubo'),
    ('tubo_L', '180 mm', 'Largo del tubo cuchilla (cortar del de 250)'),
    ('tunel_d', '12 mm', 'Tunel de la funda, interior'),
    ('valvula_d', '12.5 mm', 'Valvula trasera, interior'),
    ('celda18650_D', '18.8 mm', '18650 + holgura'),
    ('h_libre', '0.3 mm', 'Holgura por lado, ajuste libre [Supuesto, probeta]'),
    ('eclip_d', '15 mm', 'Ranura anillo E DIN 6799-15 en el cubo del anillo (por calibrar)'),
    ('eclip_D', '24 mm', 'Diametro exterior anillo E (por calibrar)'),
    ('clip_t', '1.2 mm', 'Espesor anillos elasticos (por calibrar)'),
    ('circlip_d', '23.9 mm', 'Ranura anillo DIN 471-25 en el vastago del rotor (por calibrar)'),
    ('circlip_D', '33 mm', 'Diametro exterior aprox. anillo DIN 471-25 (por calibrar)'),
    ('m3_paso', '3.4 mm', 'Agujero pasante M3'), ('m3_cabeza', '6 mm', 'Avellanado cabeza M3'),
    ('inserto_d', '4 mm', 'Agujero inserto de calor M3 (por calibrar con el inserto)'),
    ('m3_rosca', '2.5 mm', 'Agujero para roscar M3 (prisionero)'),
    ('nervio_w', '1.8 mm', 'Ancho de los nervios de arrastre anillo-tubo'),
    ('nervio_L', '5.5 mm', 'Largo de los nervios / ranuras del tubo'),
]


def gear_pts(N, m, backlash=0.1, alpha=math.radians(20)):
    """Contorno cerrado de un engranaje recto involuta (lista de (u, v) en mm)."""
    rp = m * N / 2.0
    rb = rp * math.cos(alpha)
    ra = rp + m
    rf = rp - 1.25 * m
    inv = lambda a: math.tan(a) - a
    psi = math.pi / (2 * N) - (backlash / 2.0) / rp
    def th(r):
        r = max(r, rb)
        return psi + inv(alpha) - inv(math.acos(rb / r))
    r0 = max(rf, rb)
    radii = [rf] if rf < rb else []
    radii += [r0 + (ra - r0) * i / 7.0 for i in range(8)]
    pts = []
    for k in range(N):
        phi = 2 * math.pi * k / N
        flank = [(r, th(r)) for r in radii]
        for r, t in flank:                       # flanco 1 (sube)
            pts.append((r * math.cos(phi - t), r * math.sin(phi - t)))
        for r, t in reversed(flank):             # flanco 2 (baja)
            pts.append((r * math.cos(phi + t), r * math.sin(phi + t)))
        a1 = phi + th(rf)
        a2 = phi + 2 * math.pi / N - th(rf)
        for i in (1, 2):                         # fondo
            a = a1 + (a2 - a1) * i / 3.0
            pts.append((rf * math.cos(a), rf * math.sin(a)))
    return pts


def run(_context: str):
    app = adsk.core.Application.get()
    # siempre un diseno nuevo; solo reutiliza un v3.1 sin guardar (lo vacia y lo rehace)
    d0 = adsk.fusion.Design.cast(app.activeProduct)
    reuse = (d0 is not None and not app.activeDocument.isSaved and
             any(o.component.name == 'anillo_E_DIN6799_15_COMPRADO' for o in d0.rootComponent.occurrences))
    if reuse:
        r0 = d0.rootComponent
        while r0.occurrences.count:
            r0.occurrences.item(0).deleteMe()
        while d0.userParameters.count:
            d0.userParameters.item(0).deleteMe()
    else:
        app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    design = adsk.fusion.Design.cast(app.activeProduct)
    design.designType = adsk.fusion.DesignTypes.ParametricDesignType
    root = design.rootComponent
    up = design.userParameters
    for n, v, com in PARAMS:
        if up.itemByName(n) is None:
            unit = '' if n.startswith('z_') else 'mm'
            up.add(n, adsk.core.ValueInput.createByString(v), unit, com)
    def P(n):
        p = up.itemByName(n)
        return p.value if n.startswith('z_') else p.value * 10.0
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

    def base_plane(c, axis):
        return {'x': c.yZConstructionPlane, 'y': c.xZConstructionPlane, 'z': c.xYConstructionPlane}[axis]

    def sketch_at(c, axis, a_world, L):
        """Plano normal a 'axis' ubicado para extruir L desde a_world hacia +axis."""
        bp = base_plane(c, axis)
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
        # coordenadas del mundo: a sobre el eje, (u, v) en el plano
        return {'x': (a, u, v), 'y': (u, a, v), 'z': (u, v, a)}[axis]

    def ext(c, prof, L, op):
        inp = c.features.extrudeFeatures.createInput(prof, op)
        inp.setDistanceExtent(False, VI(cm(L)))
        if op != NEW:   # los cortes/uniones solo afectan cuerpos de ESTE componente
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

    def poly_x(c, x0, L, pts, cy=0.0, cz=0.0, op=NEW):
        sk, s = sketch_at(c, 'x', x0, L)
        sk.isComputeDeferred = True
        P3 = [p3(sk, s, cy + u, cz + v) for (u, v) in pts]
        lines = sk.sketchCurves.sketchLines
        first = prev = lines.addByTwoPoints(P3[0], P3[1])
        for q in P3[2:]:
            prev = lines.addByTwoPoints(prev.endSketchPoint, q)
        lines.addByTwoPoints(prev.endSketchPoint, first.startSketchPoint)
        sk.isComputeDeferred = False
        return ext(c, sk.profiles.item(0), L, op)

    def sector_x(c, x0, L, r1, r2, t1, t2, op=CUT):
        """Sector anular (r1..r2, angulos t1..t2 en grados, en el plano YZ) extruido en X."""
        sk, s = sketch_at(c, 'x', x0, L)
        a1, a2 = math.radians(t1), math.radians(t2)
        q = lambda r, a: p3(sk, s, r * math.cos(a), r * math.sin(a))
        am = (a1 + a2) / 2.0
        arcs = sk.sketchCurves.sketchArcs
        lines = sk.sketchCurves.sketchLines
        # arcos por 3 puntos del mundo (evita depender del sentido del boceto)
        o = arcs.addByThreePoints(q(r2, a1), q(r2, am), q(r2, a2))
        i = arcs.addByThreePoints(q(r1, a1), q(r1, am), q(r1, a2))
        def near(arc, target):
            a, b = arc.startSketchPoint, arc.endSketchPoint
            return a if a.geometry.distanceTo(target) < b.geometry.distanceTo(target) else b
        for ang in (a1, a2):
            lines.addByTwoPoints(near(o, q(r2, ang)), near(i, q(r1, ang)))
        # elegir el perfil mas pequeno (el sector)
        best = min((sk.profiles.item(k) for k in range(sk.profiles.count)),
                   key=lambda p: p.areaProperties().area)
        return ext(c, best, L, op)

    def ring_x(c, x0, L, r_in, r_out, op=CUT):
        sk, s = sketch_at(c, 'x', x0, L)
        for r in (r_in, r_out):
            sk.sketchCurves.sketchCircles.addByCenterRadius(p3(sk, *W('x', s, 0, 0)), cm(r))
        # el perfil anular es el que tiene 2 lazos (no el disco interior)
        prof = [sk.profiles.item(k) for k in range(sk.profiles.count) if sk.profiles.item(k).profileLoops.count == 2][0]
        return ext(c, prof, L, op)

    def slot_w(r, w):  # ancho angular (grados) de una ranura de ancho w a radio r
        return math.degrees(w / r)

    def ring_pockets(c, x0, depth):
        r = P('iman_pcd') / 2.0
        for k in range(8):
            a = 2 * math.pi * k / 8
            cyl(c, 'x', x0, r * math.cos(a), r * math.sin(a), P('iman_D') + 0.2, depth, CUT)

    hl = P('h_libre'); w = P('pared'); ft = P('funda_t'); lz = P('luz_giro')
    m = P('mod'); Zg = int(round(P('z_corona'))); Zp = int(round(P('z_pinon')))
    rp_g = m * Zg / 2.0; rp_p = m * Zp / 2.0
    zm = -(rp_g + rp_p)                  # centro del motor (z), = -30 con 43/17 m1
    head_D = P('iman_pcd') + P('iman_D') + 4          # 48
    cav_head = head_D + 2 * 0.6                        # 49.2
    tun_D = P('tunel_d') + 1.6                         # tunel OD 13,6 (pared 0,8 = 2 perimetros)
    canal = tun_D + 2 * hl                             # 13.6
    manga = canal + 2 * w                              # 15.2
    bar_D = 56.0                                        # canon del mango
    x_back = -118.0                                     # canal del mango = 118 mm (<= 120)
    xm_face = -37.5                                     # cara del motor (2 mm mas atras que v3)
    x_gc = -34.5                                        # fondo de la camara de engranajes
    ad_ID = bar_D + 2 * hl; ad_OD = ad_ID + 4          # adaptador 56.6 / 60.6
    ca_ID = ad_OD + 2 * hl; ca_OD = ca_ID + 4          # falda del cartucho 61.2 / 65.2

    # ---------------- 1) MANGO (reutilizable, sellado) ----------------
    c = comp('mango_cuerpo')
    cyl(c, 'x', x_back, 0, 0, bar_D, -x_back)                          # canon
    box(c, -100, -17, -48, 78, 34, 48, JOIN)                           # alojamiento motor (x -100..-22)
    box(c, -100, -22, -132, 42, 44, 92, JOIN)                          # empunadura
    # cavidades
    cyl(c, 'x', -116, 0, 0, 52, 77, CUT)                               # bahia electronica x -116..-39
    cyl(c, 'x', -7.6, 0, 0, cav_head, 7.6 - w, CUT)                    # camara del rotor
    cyl(c, 'x', -14.2, 0, 0, P('rod_D') + 0.1, 7.4, CUT)               # asiento rodamiento delantero
    cyl(c, 'x', -16.0, 0, 0, 33, 1.8, CUT)                             # nervio (hombro)
    cyl(c, 'x', -23.2, 0, 0, P('rod_D') + 0.1, 7.2, CUT)               # asiento rodamiento trasero
    cyl(c, 'x', x_gc, 0, 0, 2 * (rp_g + m) + 3, -23.2 - x_gc, CUT)     # camara corona (+ anillo DIN 471)
    cyl(c, 'x', x_gc, 0, zm, 2 * (rp_p + m) + 2, -23.2 - x_gc, CUT)    # camara pinon (+ cubo)
    cyl(c, 'x', xm_face - 0.1, 0, zm, P('motor_boss_D') + 0.6, x_gc - xm_face + 0.2, CUT)   # paso del eje/resalte
    cyl(c, 'x', xm_face - P('motor_L') - 2.5, 0, zm, P('motor_D') + 0.6, P('motor_L') + 2.5, CUT)
    for y in (-10, 10):
        cyl(c, 'z', -132.1, -79, y, P('celda18650_D'), 72.1, CUT)     # 2 x 18650
    cyl(c, 'z', -62, -79, 0, 8, 18, CUT)                               # paso de cables
    box(c, -19.75, -2.3, -27.2, 5.5, 4.6, 2.0, CUT)                   # bolsillo sensor Hall (abajo)
    # tornillos M3 entre mitades: pasante + cabeza en la mitad derecha (+Y), inserto en la izquierda (-Y)
    for (bx, bz) in [(-108, 17), (-108, -17), (-60, 17)]:
        cyl(c, 'y', -16, bx, bz, 9, 32, JOIN)                          # torres dentro de la bahia
    SCREWS = [(-108, 17), (-108, -17), (-60, 17), (-19, 23), (-10, -23), (-64, -100), (-64, -70), (-94, -85)]
    for (bx, bz) in SCREWS:
        cyl(c, 'y', 0, bx, bz, P('m3_paso'), 7.1, CUT)
        cyl(c, 'y', 7, bx, bz, P('m3_cabeza'), 30, CUT)
        cyl(c, 'y', -7, bx, bz, P('inserto_d'), 7.05, CUT)
    # manga del canal (separa el canal del interior sellado) y canal
    cyl(c, 'x', x_back, 0, 0, manga, -x_back, JOIN)
    cyl(c, 'x', x_back - 0.1, 0, 0, canal, -x_back + 0.2, CUT)
    # pernos de la bayoneta del adaptador (+Y y -Y, x = -12)
    cyl(c, 'y', 27.5, -12, 0, 3, 2.5, JOIN)
    cyl(c, 'y', -30.0, -12, 0, 3, 2.5, JOIN)
    # mitades para imprimir (plano XZ): cada una se imprime con la cara de corte en la cama
    si = c.features.splitBodyFeatures.createInput(c.bRepBodies.item(0), c.xZConstructionPlane, True)
    c.features.splitBodyFeatures.add(si)
    for i in range(c.bRepBodies.count):
        b = c.bRepBodies.item(i)
        b.name = 'mango_mitad_' + ('der' if b.boundingBox.maxPoint.y > 0.01 else 'izq')

    c = comp('mango_tapa_baterias')
    box(c, -100, -22, -135, 42, 44, 3)

    # ---------------- 2) Tren motriz (dentro del mango) ----------------
    c = comp('rotor_hueco')
    cyl(c, 'x', -7.0, 0, 0, head_D, 6.0)                               # cabeza con imanes
    cyl(c, 'x', -33.5, 0, 0, P('rod_d'), 26.5, JOIN)                   # vastago (mas largo para el anillo DIN 471)
    cyl(c, 'x', -33.6, 0, 0, 20, 32.7, CUT)                            # hueco central D20
    ring_x(c, -32.5, P('clip_t') + 0.1, P('circlip_d') / 2, P('rod_d') / 2 + 0.5)   # ranura anillo DIN 471
    ring_pockets(c, -1.0 - P('iman_t') - 0.2, P('iman_t') + 0.2)       # imanes al ras de la cara
    box(c, -31.1, -15, P('rod_d') / 2 - 1.0, 8.1, 30, 3, CUT)          # plano D para la corona

    c = comp('corona_43T')
    poly_x(c, -31.0, 6.0, gear_pts(Zg, m))
    cyl(c, 'x', -25.0, 0, 0, P('rod_d') + 4, 2.0, JOIN)                # cubo-separador
    cyl(c, 'x', -31.1, 0, 0, P('rod_d') + 0.1, 8.2, CUT)
    box(c, -31.0, -13, P('rod_d') / 2 - 0.95, 8.0, 26, 2.0, JOIN)      # plano D
    # recorta las esquinas del plano D que salen del cubo (chocaban con el asiento del rodamiento)
    sk, s = sketch_at(c, 'x', -25.0, 2.1)
    for r in (14.5, 22.0):
        sk.sketchCurves.sketchCircles.addByCenterRadius(p3(sk, *W('x', s, 0, 0)), cm(r))
    ext(c, max((sk.profiles.item(k) for k in range(sk.profiles.count)),
               key=lambda p: p.areaProperties().area), 2.1, CUT)

    c = comp('pinon_17T')
    poly_x(c, -31.0, 6.0, gear_pts(Zp, m), 0, zm)
    cyl(c, 'x', -34.3, 0, zm, 10, 3.3, JOIN)                           # cubo trasero
    cyl(c, 'x', -34.4, 0, zm, P('motor_eje_d'), 9.5, CUT)
    cyl(c, 'z', zm, -32.65, 0, P('m3_rosca'), 5.2, CUT)                # prisionero M3 (roscar)

    c = comp('espaciador_rodamientos')
    cyl(c, 'x', -16.0, 0, 0, 28, 2.0); cyl(c, 'x', -16.1, 0, 0, P('rod_d') + 0.2, 2.2, CUT)

    for i, x0 in enumerate([-23.0, -14.0]):
        c = comp('rodamiento_6805_COMPRADO_%d' % (i + 1))
        cyl(c, 'x', x0, 0, 0, P('rod_D'), P('rod_B'))
        cyl(c, 'x', x0 - 0.1, 0, 0, P('rod_d'), P('rod_B') + 0.2, CUT)

    c = comp('anillo_DIN471_25_COMPRADO')
    cyl(c, 'x', -32.4, 0, 0, P('circlip_D'), P('clip_t'))
    cyl(c, 'x', -32.5, 0, 0, P('circlip_d'), P('clip_t') + 0.2, CUT)

    c = comp('motor_mango_COMPRADO')
    cyl(c, 'x', xm_face - P('motor_L'), 0, zm, P('motor_D'), P('motor_L'))
    cyl(c, 'x', xm_face, 0, zm, P('motor_boss_D'), 1.5, JOIN)
    cyl(c, 'x', xm_face + 1.5, 0, zm, P('motor_eje_d'), -25.0 - xm_face - 1.5, JOIN)   # eje hasta el frente del pinon (por calibrar)

    # ---------------- 3) FUNDA esteril (adaptador + ventana + tunel) y valvula ----------------
    c = comp('funda_adaptador_tunel')
    cyl(c, 'x', -22.0, 0, 0, ad_OD, 22.0)
    cyl(c, 'x', -22.1, 0, 0, ad_ID, 22.1, CUT)
    cyl(c, 'x', 0.0, 0, 0, ad_OD, ft, JOIN)                            # ventana
    cyl(c, 'x', -123.0, 0, 0, tun_D, 123.0 + ft, JOIN)                 # tunel
    cyl(c, 'x', -123.1, 0, 0, P('tunel_d'), 123.2 + ft, CUT)
    rr1, rr2 = ad_ID / 2 - 0.1, ad_OD / 2 + 0.1
    for base in (0, 180):                                              # bayoneta: entrada a 30, giro a 0
        sw = slot_w(ad_ID / 2, 3.4) / 2
        sector_x(c, -22.1, 22.1 - 12 + 1.7, rr1, rr2, base + 30 - sw, base + 30 + sw)
        sector_x(c, -12 - 1.7, 3.4, rr1, rr2, base - sw, base + 30 + sw)
    for base in (0, 180):                                              # clic: resalte de 0,5 mm (deja 2,9 mm para un perno de 3) antes del cierre
        sector_x(c, -12 + 1.7 - 0.5, 0.5, rr1, rr2, base + 4, base + 6, JOIN)
    cyl(c, 'z', ad_OD / 2 - 0.3, -6, 0, 3, 2.8, JOIN)                  # pernos para el cartucho (+Z, -Z)
    cyl(c, 'z', -ad_OD / 2 - 2.5, -6, 0, 3, 2.8, JOIN)

    c = comp('valvula_cuerpo')
    cyl(c, 'x', -127.0, 0, 0, 22, 6.0)
    cyl(c, 'x', -127.1, 0, 0, P('valvula_d'), 6.2, CUT)
    cyl(c, 'x', -123.0, 0, 0, tun_D + 0.1, 2.1, CUT)                   # recibe el tunel
    cyl(c, 'x', -127.1, 0, 0, 18.4, 1.6, CUT)                          # alojamiento membrana
    c = comp('valvula_tapa')
    cyl(c, 'x', -131.0, 0, 0, 22, 4.0); cyl(c, 'x', -131.1, 0, 0, P('valvula_d'), 4.2, CUT)
    c = comp('membrana_valvula_SILICONA')
    cyl(c, 'x', -127.0, 0, 0, 18, 1.4)                                 # con corte en cruz (no modelado)

    # ---------------- 4) CARTUCHO desechable ----------------
    x_rb = ft + lz                                                     # cara trasera del anillo 0.6
    c = comp('cartucho_cuerpo')
    cyl(c, 'x', -21.0, 0, 0, ca_OD, 21.0 + 8.5)                        # falda + cuerpo (x -21..8.5)
    cyl(c, 'x', -21.1, 0, 0, ca_ID, 21.1 + ft, CUT)
    cyl(c, 'x', 8.5, 0, 0, 30, 7.5, JOIN)                              # cuello (buje) x 8.5..16
    cyl(c, 'x', ft - 0.01, 0, 0, cav_head, 7.2 - ft + 0.01, CUT)       # camara del anillo
    cyl(c, 'x', 7.1, 0, 0, 18.6, 9.0, CUT)                             # buje
    s1, s2 = ca_ID / 2 - 0.1, ca_OD / 2 + 0.1
    for base in (90, 270):                                             # bayoneta: entrada a +30, giro
        sw = slot_w(ca_ID / 2, 3.4) / 2
        sector_x(c, -21.1, 21.1 - 6 + 1.7, s1, s2, base + 30 - sw, base + 30 + sw)
        sector_x(c, -6 - 1.7, 3.4, s1, s2, base - sw, base + 30 + sw)
    for base in (90, 270):
        sector_x(c, -6 + 1.7 - 0.5, 0.5, s1, s2, base + 4, base + 6, JOIN)
    cyl(c, 'z', -ca_ID / 2 - P('iman_lock_t') - 0.2, -17, 0, P('iman_lock_D') + 0.2,
        P('iman_lock_t') + 0.3, CUT)                                   # iman de enclavamiento

    c = comp('anillo_conducido')
    cyl(c, 'x', x_rb, 0, 0, head_D, 6.0)
    cyl(c, 'x', x_rb + 6.0, 0, 0, 18, 18.5 - x_rb - 6.0, JOIN)        # cubo dentro del buje
    cyl(c, 'x', x_rb - 0.1, 0, 0, P('tubo_D'), 18.5 - x_rb + 0.2, CUT)
    ring_pockets(c, x_rb, P('iman_t') + 0.2)
    rt = P('tubo_d') / 2 + 0.05                                        # nervios: entran en las ranuras del tubo
    for zs in (1, -1):
        box(c, x_rb, -P('nervio_w') / 2, zs * (rt + 0.6) if zs < 0 else rt, P('nervio_L'), P('nervio_w'), 0.6, JOIN)
    ring_x(c, 16.0, P('clip_t') + 0.1, P('eclip_d') / 2, 9.5)          # ranura anillo E

    c = comp('anillo_E_DIN6799_15_COMPRADO')
    cyl(c, 'x', 16.05, 0, 0, P('eclip_D'), P('clip_t')); cyl(c, 'x', 15.95, 0, 0, P('eclip_d'), P('clip_t') + 0.2, CUT)

    c = comp('cartucho_nariz_collar')
    cyl(c, 'x', 10.0, 0, 0, 34, 35.0)
    cyl(c, 'x', 9.9, 0, 0, 30.3, 6.1, CUT)                             # manguito sobre el cuello
    cyl(c, 'x', 16.0, 0, 0, P('eclip_D') + 2, 2.8, CUT)                # espacio del anillo E
    cyl(c, 'x', 18.7, 0, 0, P('tubo_D') + 0.8, 26.4, CUT)              # paso del tubo
    cyl(c, 'x', 20.0, 0, 0, 18.4, 3.0, CUT)                            # sello labial 12x18x3 (por calibrar)
    cyl(c, 'x', 38.0, 0, 0, 40, 3.0, CUT); cyl(c, 'x', 38.0, 0, 0, 30, 3.0, JOIN)   # ranura de la bolsa
    cyl(c, 'x', 37.9, 0, 0, P('tubo_D') + 0.8, 3.2, CUT)

    c = comp('tubo_cuchilla_COMPRADO')
    cyl(c, 'x', x_rb, 0, 0, P('tubo_D'), P('tubo_L'))
    cyl(c, 'x', x_rb - 0.1, 0, 0, P('tubo_d'), P('tubo_L') + 0.2, CUT)
    for zs in (1, -1):                                                  # ranuras de arrastre (Dremel), 2 mm x nervio_L
        box(c, x_rb - 0.1, -(P('nervio_w') + 0.2) / 2, -7 if zs < 0 else 4.5, P('nervio_L') + 0.3, P('nervio_w') + 0.2, 2.5, CUT)

    # ---------------- nombres, revision ----------------
    for o in root.occurrences:
        cc = o.component
        if cc.bRepBodies.count == 1:
            cc.bRepBodies.item(0).name = cc.name
    bad = [design.timeline.item(i).name for i in range(design.timeline.count)
           if design.timeline.item(i).healthState != adsk.fusion.FeatureHealthStates.HealthyFeatureHealthState]
    print('timeline:', design.timeline.count, 'no sanas:', bad)
    for o in root.occurrences:
        b = o.component.bRepBodies
        for i in range(b.count):
            bb = b.item(i).boundingBox
            print(o.component.name, b.count, [round(v * 10, 1) for v in (bb.minPoint.x, bb.minPoint.y, bb.minPoint.z,
                                                                         bb.maxPoint.x, bb.maxPoint.y, bb.maxPoint.z)])
    bodies = adsk.core.ObjectCollection.create()
    for o in root.occurrences:
        for i in range(o.bRepBodies.count):
            bodies.add(o.bRepBodies.item(i))
    ii = design.createInterferenceInput(bodies)
    ii.areCoincidentFacesIncluded = False
    res = design.analyzeInterference(ii)
    print('interferencias:', [(r.entityOne.name, r.entityTwo.name, round(r.interferenceBody.volume * 1000, 2)) for r in res])
    vp = app.activeViewport
    cam = vp.camera
    cam.viewOrientation = adsk.core.ViewOrientations.IsoTopRightViewOrientation
    cam.isFitView = True
    vp.camera = cam
