def esAntisimetrica(matriz):
     posicion = 0
     fila = 0
     cero = 0
     if len(matriz[fila]) != len(matriz):
         return False
     
     while fila <= len(matriz) - 1:
        while posicion <= len(matriz[fila]) - 1:
                if matriz[fila][posicion] != -matriz[posicion][fila]:
                     return False
                posicion += 1
        fila += 1
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

    
    matriz5 = ([[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]])
    assert esAntisimetrica(matriz5)


    matriz6 = ([[0, 1, 2], 
                     [-1, 0, 3], 
                     [-2, -3, 0]])
    assert esAntisimetrica(matriz6)