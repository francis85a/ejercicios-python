def esMatrizIdentidad(matriz):

    fila = 0
    posicion = 0
    if len(matriz[fila]) != len(matriz):
        return False
    
    for objeto in matriz:
        for elemento in objeto:
            if fila == posicion and matriz[fila][posicion] != 1:
                return False
            if fila != posicion and matriz[fila][posicion] != 0:
                return False
            posicion += 1
        fila += 1
    return True



if __name__ == '__main__':

    matrix1 = [[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]]
    assert esMatrizIdentidad(matrix1)

    matrix2 = [[1,0,0],
            [0,1,0],
            [0,0,0]]

    assert not esMatrizIdentidad(matrix2)

    matrix3 = [[2,0,0],
            [0,2,0],
            [0,0,2]]

    assert not esMatrizIdentidad(matrix3)

    matrix6 = [[1,0,0,0],  
            [0,1,0,2],  
            [0,0,1,0],  
            [0,0,0,1]]

    assert not esMatrizIdentidad(matrix6)

    matrix7 = [[1, -1, 1],
            [0, 1, 0],
            [0, 0, 1]]
    assert not esMatrizIdentidad(matrix7)          



    matrix4 = [[1,0,0,0],
            [0,1,1,0],
            [0,0,0,1]]

    assert not esMatrizIdentidad(matrix4)


    matrix5 = [[1,0,0,0,0,0,0,0,0]]

    assert not esMatrizIdentidad(matrix5)