from itertools import product


def genera_bar_code(numero_righe):
    array_new_ean = []
    volte = 0
    k = 13
    for numero in product(range(10), repeat=k):
        new_ean = "".join(map(str, numero))
        array_new_ean.append(new_ean)
        volte += 1
        if volte == numero_righe:
            break
    return array_new_ean
