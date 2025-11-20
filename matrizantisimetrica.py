def esAntisimetrica(matriz):
       
        fila = 0
        posicion = 0
        if len(matriz[fila]) != len(matriz):
                return False

        for objeto in matriz:
              cero = 0
              if matriz[fila][posicion] != cero:
                return False
              fila += 1
              posicion += 1
        return True




 
if __name__ == '__main__':
    matriz1 = [[1,0,0,0],
                [0,1,1,0],
                [0,0,0,1]] 
    assert not esAntisimetrica(matriz1)

    matriz2 = [[1,0,0,0,0,0,0,0,0]]
    assert not esAntisimetrica(matriz2)

    matriz3 = ([[0, 1, 2], 
        [-1, 0, -2], 
        [2, 2,  3]] )
    assert not esAntisimetrica(matriz3)

    matriz4 = ([[1, 2, 5],
                [0, 1, -9],
                [0, 0, 1]])
    assert not esAntisimetrica(matriz4)

    
    matriz5 = ([[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]])
    assert esAntisimetrica(matriz5)


    matriz6 = ([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])
    assert esAntisimetrica(matriz6)

    print("pasa los casos test")
