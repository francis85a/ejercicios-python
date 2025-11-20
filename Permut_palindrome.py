def permute_a_palindrome(characters): 
    unique = ""
    for char in characters:
        ocurrence = characters.count(char)
        if not unique and ocurrence % 2:            
            unique = char
        elif unique == char:
            continue
        elif ocurrence % 2:
            return False
        else:
            continue
    return True 