tupla = ()
print(type(tupla))  # <class 'tuple'>

# tuplas mas rapidas que las listas
tupla = ('str', 10, 15.4, True, [1,2,3], (4,5,6))
print(tupla)  # <class 'tuple'>

cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')

curso_a = cursos[0]
curso_z = cursos[-1]
sub_tupla = cursos[:3]  # primeros 3
sub_tupla2 = cursos[:]  # subtupla con todos los elementos

print(curso_a)  # Python
print(curso_z)  # MongoDB
print(sub_tupla)  # ('Python', 'Flask', 'Django')
print(sub_tupla2)  # ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')

cursos = ['Python', 'Flask', 'Django', 'JavaScript']
cursos_tupla = tuple(cursos) # crear tupla de una lista
print(cursos_tupla)  # ('Python', 'Flask', 'Django', 'JavaScript')
print(type(cursos_tupla)) # tuple

niveles = ('basico', 'intermedio', 'avanzado')
niveles_lista = list(niveles)  # crear lista de una tupla
print(niveles_lista)  # ['basico', 'intermedio', 'avanzado']
print(type(niveles_lista)) # list

# uno, dos, tres, cuatro = 1,2,3,4
# ó
numeros = (1,2,3,4, 5, 6, 7)
# descomprimir tupla
uno, dos, tres, cuatro, *resto = numeros # agregar variable a cada valor de numeros
# en vez de poner: uno = numeros[0] etc
# y para el resto de los valores anteponer *var lo cual genera una lista con el resto de valores
# y para omitir el resto de los valores usar *_
# y para excluir un valor usar _
# uno, _, tres, cuatro, *_, nueve, diez = numeros
print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto)  # [5, 6, 7]

# comprimir tupla
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
tupla = (10, 20, 30, 40, 50) # mejor trabajar con tuplas
tupla2 = (100, 200, 300, 400, 500)
# objeto zip (direccion de memoria)
resultado = zip(lista, tupla) # combinacion debe ser exacta, elemento restantes son omitidos
print(resultado)  # <zip object at 0x00000264E7C67800>
resultado = tuple(resultado) # 5x5
print(resultado)  # ((1, 10), (2, 20), (3, 30), (4, 40), (5, 50))

resultado2 = zip(lista,tupla,lista2,tupla2)
print(resultado2)
resultado2 = tuple(resultado2)
print(resultado2)
