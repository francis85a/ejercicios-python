def loose_change(cents):
    cents = int(cents)
    nombre_monedas = ["Pennies", "Nickels", "Dimes", "Quarters"]
    valor_monedas = [1, 5, 10, 25]

    diccionario = dict(zip(nombre_monedas, valor_monedas))
    monedas = list(sorted(diccionario.values()))
    diccionario_cero = dict.fromkeys(nombre_monedas, 0)
    value_to_name = {v: k for k, v in diccionario.items()}

    if cents <= 0:
        return diccionario_cero
       
    for valor in reversed(monedas):
        cantidad_monedas = cents // valor
        nombre = value_to_name[valor]
        diccionario_cero[nombre] = cantidad_monedas
        cents %= valor
    return diccionario_cero










if __name__ == '__main__':
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(5) == {'Nickels': 1, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(10) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 1, 'Quarters': 0}
    assert loose_change(25) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-1) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}


    print ("pasa casos test")