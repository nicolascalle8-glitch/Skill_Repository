import adsk.core, adsk.fusion, math

# Prototipo v3.2 - morcelador contenido. Modelo COMPLETO rehecho desde el v3.1 (no lo modifica).
# Crea un diseno NUEVO en Fusion (no toca archivos de Nick).
# Eje X = eje del instrumento; +X = hacia el paciente. Z+ arriba. Todo en mm. x = 0 es la cara frontal del mango.
#
# Cambios frente al v3.1 (pedido de Nick 2026-11-12):
#  1) El canal ya no es parte de las mitades del mango: es un TUBO SEPARADO (tubo_canal_mango) que entra por
#     detras al final del montaje y se atornilla con 2 M2 a la cola del mango. En el v3.1 la manga del canal
#     estaba pegada a la pared frontal y a la trasera, y el rotor (anillo cerrado) no se podia meter en la mitad.
#  2) Parte trasera fija: la cola del mango tiene una espiga con 2 pernos; la valvula se monta con bayoneta
#     (30 grados + clic), recibe el tunel de la funda con un O-ring, y la tapa aprieta la membrana con 3 M2.
#  3) Cuchilla impresa (cuchilla_impresa): tubo 12 / 10,4 con corona de 6 dientes y 2 lenguetas atras que
#     entran en 2 ranuras del anillo conducido (arrastre y tope axial sin pegante). ID 10,4 deja pasar la pinza de 10.
#  4) Mango mas delgado: las 2 18650 van una detras de otra (no lado a lado); empunadura ovalada de 27 mm
#     de ancho (antes caja de 44 x 42). Canon trasero D36 (antes D56 en todo el largo). Sin tapa: el pack 2S
#     queda adentro (se carga por conector, por definir).
#  5) Nada suelto: motor con 2 tornillos M2,6 en la cara, nariz del cartucho con 2 tornillos M2, 9 tornillos M3
#     entre mitades.
# Lo marcado "por calibrar" se mide en la pieza comprada antes de imprimir.

PARAMS = [
    ('motor_D', '28 mm', 'Motor del mango, diametro (por calibrar: B2-1 RS-380 + caja 28 sin aprobar)'),
    ('motor_L', '61 mm', 'Motor del mango, largo cuerpo+caja sin eje (por calibrar, B2-1 aprox 60,7)'),
    ('motor_eje_d', '4 mm', 'Eje del motor del mango (por calibrar)'),
    ('motor_boss_D', '8 mm', 'Resalte frontal del motor (por calibrar)'),
    ('motor_pcd', '20 mm', 'Circulo de los 2 tornillos M2,6 de la cara del motor (por calibrar)'),
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
    ('cuch_D', '12 mm', 'Cuchilla impresa, diametro exterior'),
    ('cuch_d', '10.4 mm', 'Cuchilla impresa, diametro interior (pinza de 10 pasa)'),
    ('cuch_L', '150 mm', 'Cuchilla impresa, largo'),
    ('lengueta_w', '1.8 mm', 'Ancho de las lenguetas de arrastre de la cuchilla'),
    ('lengueta_L', '5.5 mm', 'Largo de las lenguetas de arrastre'),
    ('tunel_d', '12 mm', 'Tunel de la funda, interior'),
    ('valvula_d', '12.5 mm', 'Valvula trasera, interior'),
    ('canal_D', '16.6 mm', 'Tubo del canal del mango, exterior'),
    ('canal_d', '14.2 mm', 'Tubo del canal del mango, interior (tunel 13,6 + holgura)'),
    ('celda18650_D', '18.8 mm', '18650 + holgura'),
    ('grip_w', '27 mm', 'Ancho de la empunadura'),
    ('h_libre', '0.3 mm', 'Holgura por lado, ajuste libre [Supuesto, probeta]'),
    ('eclip_d', '15 mm', 'Ranura anillo E DIN 6799-15 en el cubo del anillo (por calibrar)'),
    ('eclip_D', '24 mm', 'Diametro exterior anillo E (por calibrar)'),
    ('clip_t', '1.2 mm', 'Espesor anillos elasticos (por calibrar)'),
    ('circlip_d', '23.9 mm', 'Ranura anillo DIN 471-25 en el vastago del rotor (por calibrar)'),
    ('circlip_D', '33 mm', 'Diametro exterior aprox. anillo DIN 471-25 (por calibrar)'),
    ('m3_paso', '3.4 mm', 'Agujero pasante M3'), ('m3_cabeza', '6 mm', 'Cajera cabeza M3'),
    ('inserto_d', '4 mm', 'Agujero inserto de calor M3 (por calibrar con el inserto)'),
    ('inserto_m2_d', '3.2 mm', 'Agujero inserto de calor M2 (por calibrar)'),
    ('m3_rosca', '2.5 mm', 'Agujero para roscar M3 (prisionero)'),
    ('m2_paso', '2.2 mm', 'Agujero pasante M2'), ('m2_rosca', '1.6 mm', 'Agujero M2 autorroscante'),
    ('oring_D', '16 mm', 'Fondo de la ranura del O-ring 13 x 1,5 de la valvula (por calibrar)'),
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
        for r, t in flank:
            pts.append((r * math.cos(phi - t), r * math.sin(phi - t)))
        for r, t in reversed(flank):
            pts.append((r * math.cos(phi + t), r * math.sin(phi + t)))
        a1 = phi + th(rf)
        a2 = phi + 2 * math.pi / N - th(rf)
        for i in (1, 2):
            a = a1 + (a2 - a1) * i / 3.0
            pts.append((rf * math.cos(a), rf * math.sin(a)))
    return pts


def run(_context: str):
    app = adsk.core.Application.get()
    # siempre un diseno nuevo; solo reutiliza un v3.2 sin guardar (lo vacia y lo rehace)
    d0 = adsk.fusion.Design.cast(app.activeProduct)
    reuse = (d0 is not None and not app.activeDocument.isSaved and
             any(o.component.name == 'tubo_canal_mango' for o in d0.rootComponent.occurrences))
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
        """Sector anular (r1..r2, angulos t1..t2 en grados; 0 = +Y, 90 = +Z) extruido en X."""
        sk, s = sketch_at(c, 'x', x0, L)
        a1, a2 = math.radians(t1), math.radians(t2)
        q = lambda r, a: p3(sk, s, r * math.cos(a), r * math.sin(a))
        am = (a1 + a2) / 2.0
        arcs = sk.sketchCurves.sketchArcs
        lines = sk.sketchCurves.sketchLines
        o = arcs.addByThreePoints(q(r2, a1), q(r2, am), q(r2, a2))
        i = arcs.addByThreePoints(q(r1, a1), q(r1, am), q(r1, a2))
        def near(arc, target):
            a, b = arc.startSketchPoint, arc.endSketchPoint
            return a if a.geometry.distanceTo(target) < b.geometry.distanceTo(target) else b
        for ang in (a1, a2):
            lines.addByTwoPoints(near(o, q(r2, ang)), near(i, q(r1, ang)))
        best = min((sk.profiles.item(k) for k in range(sk.profiles.count)),
                   key=lambda p: p.areaProperties().area)
        return ext(c, best, L, op)

    def ring_x(c, x0, L, r_in, r_out, op=CUT):
        sk, s = sketch_at(c, 'x', x0, L)
        for r in (r_in, r_out):
            sk.sketchCurves.sketchCircles.addByCenterRadius(p3(sk, *W('x', s, 0, 0)), cm(r))
        prof = [sk.profiles.item(k) for k in range(sk.profiles.count) if sk.profiles.item(k).profileLoops.count == 2][0]
        return ext(c, prof, L, op)

    def slot_w(r, w):
        return math.degrees(w / r)

    def ring_pockets(c, x0, depth):
        r = P('iman_pcd') / 2.0
        for k in range(8):
            a = 2 * math.pi * k / 8
            cyl(c, 'x', x0, r * math.cos(a), r * math.sin(a), P('iman_D') + 0.2, depth, CUT)

    def bayonet(c, r_in, r_out, x_pin, x_edge, bases):
        """Ranura en L (entrada axial a +30 grados, giro hasta 0) + clic de 0,5 mm. x_edge = borde abierto."""
        sw = slot_w(r_in, 3.4) / 2
        rr1, rr2 = r_in - 0.1, r_out + 0.1
        sgn = 1 if x_edge > x_pin else -1
        for base in bases:
            if sgn > 0:   # borde abierto hacia +X
                sector_x(c, x_pin - 1.7, x_edge - x_pin + 1.7 + 0.1, rr1, rr2, base + 30 - sw, base + 30 + sw)
            else:
                sector_x(c, x_edge - 0.1, x_pin + 1.7 - x_edge + 0.1, rr1, rr2, base + 30 - sw, base + 30 + sw)
            sector_x(c, x_pin - 1.7, 3.4, rr1, rr2, base - sw, base + 30 + sw)
        for base in bases:   # clic en el borde de la ranura que queda abajo al imprimir (no flota); deja 2,9 mm
            x0 = x_pin - 1.7 if sgn > 0 else x_pin + 1.7 - 0.5
            sector_x(c, x0, 0.5, rr1, rr2, base + 4, base + 6, JOIN)

    hl = P('h_libre'); w = P('pared'); ft = P('funda_t'); lz = P('luz_giro')
    m = P('mod'); Zg = int(round(P('z_corona'))); Zp = int(round(P('z_pinon')))
    rp_g = m * Zg / 2.0; rp_p = m * Zp / 2.0
    zm = -(rp_g + rp_p)                       # centro del motor (z), = -30 con 43/17 m1
    head_D = P('iman_pcd') + P('iman_D') + 4  # 48
    cav_head = head_D + 2 * 0.6               # 49.2
    tun_D = P('tunel_d') + 1.6                # tunel OD 13,6 (pared 0,8)
    cD, cd = P('canal_D'), P('canal_d')
    head_OD = 56.0                            # cabeza del mango (imanes + rodamientos)
    bar_D = 36.0                              # canon trasero
    hous_D = 34.0                             # alojamiento del motor
    x_head = -38.0                            # la cabeza va de x -38 a 0
    x_tail = -110.0                           # cara trasera del cuerpo
    x_sp = -116.0                             # cola (espiga de la valvula) x -116..-110 -> canal de 116 mm
    sp_D = 28.0                               # espiga
    xm_face = -37.5                           # cara del motor
    x_gc = -34.5                              # fondo de la camara de engranajes
    gx = -65.0                                # centro de la empunadura
    gw = P('grip_w'); gs = (P('celda18650_D') + 0.5) / 2   # medio paso entre las 2 celdas (9.65)
    zg_top, zg_bot = -40.0, -127.0            # empunadura
    ad_ID = head_OD + 2 * hl; ad_OD = ad_ID + 4   # adaptador 56.6 / 60.6
    ca_ID = ad_OD + 2 * hl; ca_OD = ca_ID + 4     # falda del cartucho 61.2 / 65.2
    va_ID = sp_D + 2 * hl; va_OD = va_ID + 5      # falda de la valvula 28.6 / 33.6

    # ---------------- 1) MANGO (reutilizable, sellado, 2 mitades) ----------------
    c = comp('mango_cuerpo')
    cyl(c, 'x', x_head, 0, 0, head_OD, -x_head)                        # cabeza
    cyl(c, 'x', x_tail, 0, 0, bar_D, x_head - x_tail, JOIN)            # canon trasero
    cyl(c, 'x', x_tail, 0, zm, hous_D, -23.0 - x_tail, JOIN)           # alojamiento motor + pinon
    cyl(c, 'x', x_sp, 0, 0, sp_D, x_tail - x_sp, JOIN)                 # espiga de la valvula
    for xs in (-1, 1):                                                  # empunadura ovalada
        cyl(c, 'z', zg_bot, gx + xs * gs, 0, gw, zg_top - zg_bot, JOIN)
    box(c, gx - gs, -gw / 2, zg_bot, 2 * gs, gw, zg_top - zg_bot, JOIN)
    # cavidades
    cyl(c, 'x', -7.6, 0, 0, cav_head, 7.6 - w, CUT)                    # camara del rotor
    cyl(c, 'x', -14.2, 0, 0, P('rod_D') + 0.1, 7.4, CUT)               # asiento rodamiento delantero
    cyl(c, 'x', -16.0, 0, 0, 33, 1.8, CUT)                             # hombro
    cyl(c, 'x', -23.2, 0, 0, P('rod_D') + 0.1, 7.2, CUT)               # asiento rodamiento trasero
    cyl(c, 'x', x_gc, 0, 0, 2 * (rp_g + m) + 3, -23.2 - x_gc, CUT)     # camara corona (+ anillo DIN 471)
    cyl(c, 'x', x_gc, 0, zm, 2 * (rp_p + m) + 2, -24.0 - x_gc, CUT)    # camara pinon (+ cubo)
    cyl(c, 'x', xm_face - 0.1, 0, zm, P('motor_boss_D') + 0.6, x_gc - xm_face + 0.2, CUT)  # paso del resalte
    cyl(c, 'x', xm_face - P('motor_L') - 5.0, 0, zm, P('motor_D') + 0.2, P('motor_L') + 5.1, CUT)  # motor (+5 terminales)
    for y in (-1, 1):                                                   # 2 tornillos M2,6 de la cara del motor
        yy = y * P('motor_pcd') / 2
        cyl(c, 'x', xm_face - 0.1, yy, zm, 2.9, x_gc - xm_face + 0.2, CUT)
        cyl(c, 'x', x_gc - 1.7, yy, zm, 6.0, 1.8, CUT)                  # cajera de la cabeza
    cyl(c, 'x', -104.0, 0, 0, 32, -38.5 + 104.0, CUT)                  # bahia electronica x -104..-38.5
    box(c, -103.5, -5, -20, 6, 10, 8, CUT)                              # paso de cables motor -> bahia
    for xs in (-1, 1):
        cyl(c, 'z', -119.0, gx + xs * gs, 0, P('celda18650_D'), 68.0, CUT)   # 2 x 18650 en linea
    cyl(c, 'z', -52.0, gx, 0, 8, 9.0, CUT)                              # paso de cables celdas -> motor
    box(c, -19.75, -2.3, -27.2, 5.5, 4.6, 2.0, CUT)                    # bolsillo sensor Hall (abajo)
    # tornillos M3 entre mitades: pasante + cabeza en la mitad derecha (+Y), inserto en la izquierda (-Y)
    TOWERS = [(-60, 13), (-92, 13)]
    for (bx, bz) in TOWERS:
        cyl(c, 'y', -12, bx, bz, 8, 24, JOIN)                           # torres dentro de la bahia
    SCREWS = [(-19, 23), (-10, -23), (-60, 13), (-92, 13), (-107, 12),
              (gx - 12, -123), (gx + 12, -123), (gx - 14, -47.5), (gx + 14, -47.5)]
    for (bx, bz) in SCREWS:
        cyl(c, 'y', 0, bx, bz, P('m3_paso'), 7.1, CUT)
        cyl(c, 'y', 7, bx, bz, P('m3_cabeza'), 30, CUT)
        cyl(c, 'y', -7, bx, bz, P('inserto_d'), 7.05, CUT)
    # hueco del tubo del canal (el tubo se mete por detras al final) y asiento de su brida
    cyl(c, 'x', x_sp - 0.1, 0, 0, cD + 0.2, -x_sp + 0.2, CUT)
    cyl(c, 'x', x_sp - 0.1, 0, 0, 25.4, 2.6, CUT)                       # cajera de la brida (2,5)
    for y in (-10.5, 10.5):
        cyl(c, 'x', x_sp + 2.4, y, 0, P('inserto_m2_d'), 4.1, CUT)      # insertos M2 de la brida
    # pernos de las bayonetas: adaptador (x = -12) y valvula (x = -113), en +Y y -Y
    cyl(c, 'y', head_OD / 2 - 0.5, -12, 0, 3, 2.5, JOIN)
    cyl(c, 'y', -head_OD / 2 - 2.0, -12, 0, 3, 2.5, JOIN)
    cyl(c, 'y', sp_D / 2 - 0.5, -113, 0, 3, 3.0, JOIN)
    cyl(c, 'y', -sp_D / 2 - 2.5, -113, 0, 3, 3.0, JOIN)
    # mitades (plano XZ): cada una se imprime con la cara de corte en la cama
    si = c.features.splitBodyFeatures.createInput(c.bRepBodies.item(0), c.xZConstructionPlane, True)
    c.features.splitBodyFeatures.add(si)
    for i in range(c.bRepBodies.count):
        b = c.bRepBodies.item(i)
        b.name = 'mango_mitad_' + ('der' if b.boundingBox.maxPoint.y > 0.01 else 'izq')

    c = comp('tubo_canal_mango')                                        # se instala al final, por detras
    cyl(c, 'x', x_sp + 2.5, 0, 0, cD, -x_sp - 2.5)
    cyl(c, 'x', x_sp, 0, 0, 25.0, 2.5, JOIN)                            # brida
    cyl(c, 'x', x_sp - 0.1, 0, 0, cd, -x_sp + 0.2, CUT)
    for y in (-10.5, 10.5):
        cyl(c, 'x', x_sp - 0.1, y, 0, P('m2_paso'), 2.7, CUT)
        cyl(c, 'x', x_sp - 0.1, y, 0, 4.0, 1.4, CUT)                    # cajera cabeza M2

    # ---------------- 2) Tren motriz (dentro del mango) ----------------
    c = comp('rotor_hueco')
    cyl(c, 'x', -7.0, 0, 0, head_D, 6.0)                               # cabeza con imanes
    cyl(c, 'x', -33.5, 0, 0, P('rod_d'), 26.5, JOIN)                   # vastago
    cyl(c, 'x', -33.6, 0, 0, 20, 32.7, CUT)                            # hueco central D20 (tubo del canal 16,6)
    ring_x(c, -32.5, P('clip_t') + 0.1, P('circlip_d') / 2, P('rod_d') / 2 + 0.5)   # ranura anillo DIN 471
    ring_pockets(c, -1.0 - P('iman_t') - 0.2, P('iman_t') + 0.2)       # imanes al ras de la cara
    box(c, -31.1, -15, P('rod_d') / 2 - 1.0, 8.1, 30, 3, CUT)          # plano D para la corona

    c = comp('corona_43T')
    poly_x(c, -31.0, 6.0, gear_pts(Zg, m))
    cyl(c, 'x', -25.0, 0, 0, P('rod_d') + 4, 2.0, JOIN)                # cubo-separador
    cyl(c, 'x', -31.1, 0, 0, P('rod_d') + 0.1, 8.2, CUT)
    box(c, -31.0, -13, P('rod_d') / 2 - 0.95, 8.0, 26, 2.0, JOIN)      # plano D
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
    cyl(c, 'x', xm_face + 1.5, 0, zm, P('motor_eje_d'), -25.0 - xm_face - 1.5, JOIN)

    c = comp('pack_2S_18650_COMPRADO')
    for xs in (-1, 1):
        cyl(c, 'z', -118.5, gx + xs * gs, 0, 18.4, 65.0)

    # ---------------- 3) FUNDA esteril (adaptador + ventana + tunel) y VALVULA ----------------
    c = comp('funda_adaptador_tunel')
    cyl(c, 'x', -22.0, 0, 0, ad_OD, 22.0)
    cyl(c, 'x', -22.1, 0, 0, ad_ID, 22.1, CUT)
    cyl(c, 'x', 0.0, 0, 0, ad_OD, ft, JOIN)                            # ventana
    cyl(c, 'x', -121.0, 0, 0, tun_D, 121.0 + ft, JOIN)                 # tunel hasta dentro de la valvula
    cyl(c, 'x', -121.1, 0, 0, P('tunel_d'), 121.2 + ft, CUT)
    bayonet(c, ad_ID / 2, ad_OD / 2, -12.0, -22.0, (0, 180))
    cyl(c, 'z', ad_OD / 2 - 0.3, -6, 0, 3, 2.8, JOIN)                  # pernos para el cartucho (+Z, -Z)
    cyl(c, 'z', -ad_OD / 2 - 2.5, -6, 0, 3, 2.8, JOIN)

    c = comp('valvula_cuerpo')                                          # bayoneta sobre la espiga del mango
    cyl(c, 'x', x_sp, 0, 0, va_OD, x_tail - x_sp)                      # falda x -116..-110
    cyl(c, 'x', x_sp - 0.1, 0, 0, va_ID, x_tail - x_sp + 0.2, CUT)
    cyl(c, 'x', -124.0, 0, 0, va_OD, 8.0, JOIN)                        # placa x -124..-116
    cyl(c, 'x', -121.0, 0, 0, tun_D + 0.2, 5.1, CUT)                   # recibe el tunel (5 mm)
    cyl(c, 'x', -119.5, 0, 0, P('oring_D'), 2.0, CUT)                  # ranura O-ring
    cyl(c, 'x', -124.1, 0, 0, P('valvula_d'), 3.2, CUT)
    cyl(c, 'x', -124.1, 0, 0, 18.4, 1.6, CUT)                          # alojamiento membrana (1,5)
    bayonet(c, va_ID / 2, va_OD / 2, -113.0, x_tail, (0, 180))
    TAPA = [(12 * math.cos(math.radians(a)), 12 * math.sin(math.radians(a))) for a in (90, 210, 330)]
    for (u, v) in TAPA:
        cyl(c, 'x', -124.1, u, v, P('m2_rosca'), 6.1, CUT)

    c = comp('valvula_tapa')
    cyl(c, 'x', -128.0, 0, 0, 30, 4.0); cyl(c, 'x', -128.1, 0, 0, P('valvula_d'), 4.2, CUT)
    for (u, v) in TAPA:
        cyl(c, 'x', -128.1, u, v, P('m2_paso'), 4.2, CUT)
    c = comp('membrana_valvula_SILICONA')
    cyl(c, 'x', -124.0, 0, 0, 18, 1.4)                                 # con corte en cruz (no modelado)
    c = comp('oring_13x1_5_COMPRADO')
    cyl(c, 'x', -119.4, 0, 0, P('oring_D') - 0.1, 1.8); cyl(c, 'x', -119.5, 0, 0, tun_D + 0.1, 2.0, CUT)

    # ---------------- 4) CARTUCHO desechable ----------------
    x_rb = ft + lz                                                     # cara trasera del anillo 0.6
    c = comp('cartucho_cuerpo')
    cyl(c, 'x', -21.0, 0, 0, ca_OD, 21.0 + 8.5)                        # falda + cuerpo (x -21..8.5)
    cyl(c, 'x', -21.1, 0, 0, ca_ID, 21.1 + ft, CUT)
    cyl(c, 'x', 8.5, 0, 0, 30, 7.5, JOIN)                              # cuello (buje) x 8.5..16
    cyl(c, 'x', ft - 0.01, 0, 0, cav_head, 7.2 - ft + 0.01, CUT)       # camara del anillo
    cyl(c, 'x', 7.1, 0, 0, 18.6, 9.0, CUT)                             # buje
    sw = slot_w(ca_ID / 2, 3.4) / 2
    s1, s2 = ca_ID / 2 - 0.1, ca_OD / 2 + 0.1
    for base in (90, 270):
        sector_x(c, -21.1, 21.1 - 6 + 1.7, s1, s2, base + 30 - sw, base + 30 + sw)
        sector_x(c, -6 - 1.7, 3.4, s1, s2, base - sw, base + 30 + sw)
    for base in (90, 270):
        sector_x(c, -6 + 1.7 - 0.5, 0.5, s1, s2, base + 4, base + 6, JOIN)
    cyl(c, 'z', -ca_ID / 2 - P('iman_lock_t') - 0.2, -17, 0, P('iman_lock_D') + 0.2,
        P('iman_lock_t') + 0.3, CUT)                                   # iman de enclavamiento
    cyl(c, 'y', 11.0, 12.5, 0, P('m2_rosca'), 4.1, CUT)                # 2 tornillos M2 de la nariz
    cyl(c, 'y', -15.1, 12.5, 0, P('m2_rosca'), 4.1, CUT)

    c = comp('anillo_conducido')
    cyl(c, 'x', x_rb, 0, 0, head_D, 6.0)
    cyl(c, 'x', x_rb + 6.0, 0, 0, 18, 18.5 - x_rb - 6.0, JOIN)        # cubo dentro del buje
    cyl(c, 'x', x_rb - 0.1, 0, 0, P('cuch_D') + 0.1, 18.5 - x_rb + 0.2, CUT)
    ring_pockets(c, x_rb, P('iman_t') + 0.2)
    lw, lL = P('lengueta_w'), P('lengueta_L')
    rc = P('cuch_D') / 2
    box(c, x_rb - 0.1, -(lw + 0.2) / 2, rc - 0.5, lL + 0.3, lw + 0.2, 1.5, CUT)      # ranuras de las lenguetas
    box(c, x_rb - 0.1, -(lw + 0.2) / 2, -rc - 1.0, lL + 0.3, lw + 0.2, 1.5, CUT)
    ring_x(c, 16.0, P('clip_t') + 0.1, P('eclip_d') / 2, 9.5)          # ranura anillo E

    c = comp('anillo_E_DIN6799_15_COMPRADO')
    cyl(c, 'x', 16.05, 0, 0, P('eclip_D'), P('clip_t')); cyl(c, 'x', 15.95, 0, 0, P('eclip_d'), P('clip_t') + 0.2, CUT)

    c = comp('cartucho_nariz_collar')
    cyl(c, 'x', 10.0, 0, 0, 34, 35.0)
    cyl(c, 'x', 9.9, 0, 0, 30.3, 6.1, CUT)                             # manguito sobre el cuello
    cyl(c, 'x', 16.0, 0, 0, P('eclip_D') + 2, 2.8, CUT)                # espacio del anillo E
    cyl(c, 'x', 18.7, 0, 0, P('cuch_D') + 0.8, 26.4, CUT)              # paso de la cuchilla
    cyl(c, 'x', 20.0, 0, 0, 18.4, 3.0, CUT)                            # sello labial 12x18x3 (por calibrar)
    cyl(c, 'x', 38.0, 0, 0, 40, 3.0, CUT); cyl(c, 'x', 38.0, 0, 0, 30, 3.0, JOIN)   # ranura de la bolsa
    cyl(c, 'x', 37.9, 0, 0, P('cuch_D') + 0.8, 3.2, CUT)
    cyl(c, 'y', 15.0, 12.5, 0, P('m2_paso'), 2.2, CUT)                 # 2 tornillos M2 al cuello
    cyl(c, 'y', -17.2, 12.5, 0, P('m2_paso'), 2.2, CUT)

    c = comp('cuchilla_impresa')
    xf = x_rb + P('cuch_L')
    cyl(c, 'x', x_rb, 0, 0, P('cuch_D'), P('cuch_L'))
    cyl(c, 'x', x_rb - 0.1, 0, 0, P('cuch_d'), P('cuch_L') + 0.2, CUT)
    box(c, x_rb, -lw / 2, rc - 0.3, lL, lw, 1.1, JOIN)                 # lenguetas de arrastre (+Z, -Z)
    box(c, x_rb, -lw / 2, -rc - 0.8, lL, lw, 1.1, JOIN)
    for k in range(6):                                                  # corona de 6 dientes
        sector_x(c, xf - 2.0, 2.1, P('cuch_d') / 2 - 0.2, rc + 0.2, 60 * k, 60 * k + 20)

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
            print(o.component.name, b.item(i).name, [round(v * 10, 1) for v in (bb.minPoint.x, bb.minPoint.y, bb.minPoint.z,
                                                                                   bb.maxPoint.x, bb.maxPoint.y, bb.maxPoint.z)])
    bodies = adsk.core.ObjectCollection.create()
    for o in root.occurrences:
        for i in range(o.bRepBodies.count):
            bodies.add(o.bRepBodies.item(i))
    ii = design.createInterferenceInput(bodies)
    ii.areCoincidentFacesIncluded = False
    res = design.analyzeInterference(ii)
    print('cuerpos:', bodies.count)
    print('interferencias:', [(r.entityOne.name, r.entityTwo.name, round(r.interferenceBody.volume * 1000, 2)) for r in res])
    vp = app.activeViewport
    cam = vp.camera
    cam.viewOrientation = adsk.core.ViewOrientations.IsoTopRightViewOrientation
    cam.isFitView = True
    vp.camera = cam
