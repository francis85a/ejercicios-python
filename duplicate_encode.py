def duplicate_encode(word):
    word = word.lower ()
    resultado = ""
    
    for character in word:
        if word.count(character) > 1:
            resultado += ")"
        else:
            resultado += "("
        
    return resultado