def duplicate_encode(palabra):
    palabra = palabra.lower ()
    conteo_letras = {} 
    
    for letra in palabra:
        
        if letra in conteo_letras:
            conteo_letras[letra] += 1
        
        else:
            conteo_letras[letra] = 1    

    resultado = ""
    
    for letra in palabra:
        
        if conteo_letras[letra] > 1:
            resultado += ")"
            
        else:
            resultado += "("
            
    return resultado