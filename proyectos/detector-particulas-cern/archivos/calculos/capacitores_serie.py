"""Suma de capacitores en serie.

Pide los valores uno por uno (con unidad: pF, nF, uF o F) y calcula la capacitancia total:
    1/Ct = 1/C1 + 1/C2 + ... + 1/Cn
Para terminar, presione Enter sin escribir nada.

Ejemplos de valores válidos: 10pF, 10 pF, 4.7nF, 4,7 nF, 100n, 47uF, 47µF, 0.000001
"""

# Multiplicadores de cada unidad (para pasar todo a faradios)
UNIDADES = {
    'pf': 1e-12, 'p': 1e-12,
    'nf': 1e-9,  'n': 1e-9,
    'uf': 1e-6,  'u': 1e-6, 'µf': 1e-6, 'µ': 1e-6,
    'mf': 1e-3,  'm': 1e-3,
    'f': 1.0,    '': 1.0,
}


def leer_capacitor(texto):
    """Convierte un texto como '10 pF' o '4,7nF' en faradios. Devuelve None si no se entiende."""
    texto = texto.strip().lower().replace(' ', '').replace(',', '.')
    # separar el número de la unidad
    i = 0
    while i < len(texto) and (texto[i].isdigit() or texto[i] in '.eE+-'):
        i += 1
    numero, unidad = texto[:i], texto[i:]
    if unidad not in UNIDADES:
        return None
    try:
        valor = float(numero)
    except ValueError:
        return None
    if valor <= 0:
        return None
    return valor * UNIDADES[unidad]


def formato(c):
    """Muestra una capacitancia en la unidad más cómoda."""
    for nombre, factor in [('µF', 1e-6), ('nF', 1e-9), ('pF', 1e-12)]:
        if c >= factor:
            return f'{c / factor:.4g} {nombre}'
    return f'{c / 1e-12:.4g} pF'


def capacitancia_serie(valores):
    """Capacitancia total de capacitores en serie (valores en faradios)."""
    return 1 / sum(1 / c for c in valores)


def main():
    print('Suma de capacitores en serie')
    print('Escriba cada valor con su unidad (ej: 10pF, 4.7nF, 47uF). Enter vacío para terminar.\n')
    valores = []
    while True:
        texto = input(f'C{len(valores) + 1}: ')
        if texto.strip() == '':
            break
        c = leer_capacitor(texto)
        if c is None:
            print('  No entendí ese valor. Use por ejemplo: 10pF, 4.7nF, 100n, 47uF')
            continue
        valores.append(c)
        print(f'  Total en serie hasta ahora: {formato(capacitancia_serie(valores))}')

    if not valores:
        print('No ingresó ningún capacitor.')
        return

    print('\nCapacitores ingresados:')
    for k, c in enumerate(valores, start=1):
        print(f'  C{k} = {formato(c)}')
    print(f'\nCapacitancia total en serie: {formato(capacitancia_serie(valores))}')


if __name__ == '__main__':
    main()
