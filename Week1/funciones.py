#Función básica: Valor absoluto#

def valor_absoluto(x):
    return abs(x)

# Ejemplo de uso
print(valor_absoluto(-5))  # Salida: 5

#Función de suma#
def suma(a, b):
    return a + b

# Ejemplo de uso
print(suma(3, 4))  # Salida: 7

#Operaciones aritméticas#
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else 'Indefinido'
    return suma, resta, multiplicacion, division

# Ejemplo de uso
resultados = operaciones(6, 3)
print(resultados)  # Salida: (9, 3, 18, 2.0)

#Racionales#
from fractions import Fraction

def valor_absoluto_racional(x):
    if isinstance(x, Fraction):
        return abs(x)
    else:
        raise ValueError("El parámetro debe ser un número racional")

# Ejemplo de uso
fraccion = Fraction(3, 4)
print(valor_absoluto_racional(fraccion))  # Salida: 3/4

#Valor absoluto en suma#
def valor_absoluto_suma(a, b):
    return abs(a + b)

# Ejemplo de uso
print(valor_absoluto_suma(-3, 2))  # Salida: 1