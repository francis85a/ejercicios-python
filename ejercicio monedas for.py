def euros(cambio):
    cantidadMonedas = []
    tipoMonedas = [5, 2, 1]

    for moneda in tipoMonedas:
        if cambio < 0:
            return [0, 0, 0]
        cantidadMonedas.append(cambio // moneda)
        cambio %= moneda
    return cantidadMonedas


print (euros(8))
#>>> (1, 1, 1)  # una de 5 cents, una de 2 cents y una de 1 cent.
print (euros(5))
#>>> (1, 0, 0)  # una 5 cents, ninguna de 2 cents y ninguna de 1 cent.
print (euros(29))
#>>> (5, 2, 0)  # cinco de 5 cents, dos de 2 cents y ninguna de 1 cent.
print (euros(0))
#>>> (0, 0, 0) # ninguna de 5 cents, ninguna de 2 cents y 1 de cents.