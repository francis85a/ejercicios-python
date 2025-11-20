import math

def roots(a, b, c):
    discriminante = b ** 2 - 4 * a * c 
    if discriminante < 0:
        return None
    elif discriminante == 0:
        raiz = -b / (2 * a)
        return round(raiz + raiz, 2)
    else:
        raiz_uno = (-b + math.sqrt(discriminante)) / (2 * a)
        raiz_dos = (-b - math.sqrt(discriminante)) / (2 * a)
        return round(raiz_uno + raiz_dos, 2)