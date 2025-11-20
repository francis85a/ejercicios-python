# Este programa contiene múltiples violaciones 
# a las convenciones de nombres de variables

# Instrucciones:
#  - Analiza el programa y encuentra todas las violaciones 
#    a las convenciones de nombres de variables descritas 
#    en la lista de chequeo del capítulo 11 "The powe of 
#    variable names" del libro "Clean Code" de Robert C. Martin.
#  - Para cada violación, explica por qué el nombre no cumple
#    con la convención y propon un nombre alternativo que 
#    respete las buenas prácticas.
#  - Refactoriza el programa para corregir todas las violaciones
#    y asegúrate de que sea más legible y mantenible.

NUMERO_PI = 3.14159  # tiene que tener minimo 8 caracteres y que sea entendible

LISTA_VALORES = [10, 20, 30, 40, 50]  # poniendo g solo no se entiende que quiere representar hay que poner un nombre que represente algo hay que ponerlo en mayuculas ya que es una constante

def calcular_promedio():
    promedio_lista_valores = sum(LISTA_VALORES) / len(LISTA_VALORES)  # temp no representa nada se debe poner un nombre mas representativo para el calculo que se va a hacer
    return promedio_lista_valores

def calcular_maximo():
    numero_maximo = max(LISTA_VALORES)  # z no representa nada es mejor ponerle un nombre a la variable como numero maximo ya que se esta buscando ese resultado
    return max(LISTA_VALORES)

def calcular_minimo():
    numero_minimo = min(LISTA_VALORES)  # y no representa nada es mejor ponerle un nombre a la variable como numero minimo ya que se esta buscando ese resultado
    return min(LISTA_VALORES)
 
# se deben poner sufijos o prefijos que identifiquen a la variable

color_red = 1
color_green = 2
color_blue = 3

# Función con un nombre que no describe su propósito
def mostrar_resultados():
    # Uso de nombres de variables booleanas poco claros
    esta_resuelto = True  # flag no daba significado ninguno
    if esta_resuelto:
        # Uso de nombres de variables que no describen su propósito
        resultados = calcular_promedio(LISTA_VALORES, NUMERO_PI)
        print('Resultado:', resultados)
 
for posicion in range(len(LISTA_VALORES)):
    print("Elemento", posicion, ":", LISTA_VALORES [posicion])

