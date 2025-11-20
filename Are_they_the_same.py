def comp(number_list_a, number_list_b):

    if number_list_a is None:
        return False
    
    if number_list_b is None:
        return False
    
    if len(number_list_a) != len(number_list_b):
        return False
    
    number_list_b_copy = number_list_b[:]

    for element in number_list_a:
        number_square = element ** 2
        if number_square in number_list_b:
             number_list_b.remove(number_square)
        else:
            return False
    return True


if __name__ == '__main__':

    array_a = []
    array_b = []
    assert comp(array_a, array_b)

    array_a = None
    array_b = []
    assert not comp(array_a, array_b)

    array_a = []
    array_b = None
    assert not comp(array_a, array_b)

    array_a = [121, 144, 19, 161, 19, 144, 19, 11]
    array_b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert comp(array_a, array_b)
    
    array_a = [121, 144, 19, 161, 19, 144, 19, 11]
    array_b = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
    assert not comp(array_a, array_b)

    array_a = [121, 144, 19, 161, 19, 144, 19, 11]
    array_b = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    assert not comp(array_a, array_b)