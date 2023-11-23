print('hi')
curso = 'Curso pro'
# variable
TITULO_CURSO = 'curso "PythonPro"'
# CONSTANTE EN MAYUS ES POR CONVENCIÓN
print(TITULO_CURSO)

""" comentar
lineas """

# tipos de datos
# tipado, diferentes tipos de datos para la misma variable
numero = -10,5
numero = 10/3
# res con decimales
numero = 10//3
# res solo entero
print(numero)

valor = True
# booleanos en mayuscula
print(valor)

# operadores lógicos and or not
res = True and True and False
print(res)

# tipo de dato
tipo = type(valor)
print(tipo)
# <class 'bool'>

# input siempre retorna string
""" word = input ('ingresar letras: ')
print(word) """

# input siempre retorna string
num = input('ingresar numero: ')
num = int(num)
# num = float(num)
print(num)

# solo al ingresar si, será True
auth = input('autoriza: si/no ') == 'si'
print(auth)

# mas var en una linea, 4 max
nombre, apellido, edad = 'Eduardo', 'García', '23'
print(nombre)
print(apellido)
print(edad)
