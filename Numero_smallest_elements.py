def first_n_smallest(caracter_lista, numero):
    
    if numero == 0:
        return []
    
    sorted_caracter_lista = sorted(caracter_lista)
    
    numero_pequeño = sorted_caracter_lista[:numero]
    
    lista_nueva = []
    
    for caracter in caracter_lista:
        
        if caracter in numero_pequeño and len(lista_nueva) < numero:
            lista_nueva.append(caracter)
            numero_pequeño.remove(caracter)
    
    return lista_nueva