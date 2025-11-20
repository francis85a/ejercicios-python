def letter_check(array): 
    first_string = array[0].lower()
    second_string = array [1].lower()
    
    for character in second_string:
        if character not in first_string:
            return False
    return True