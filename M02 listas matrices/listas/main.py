# lista
# lista = list()
# lista = []
lista = ['nombre', 10, 15.6, True]
lista2 = ['apellido', 5, 0.2, False]
print(lista)

# tartar de usar listas con el mismo tipo de var
lista_bool = [True, True, (2<10), (4>3 and 10) != 11]
print(lista_bool)

print(lista[0]) # nombre
print(lista[-1]) # true

lista[1] = 20 # modificar indice 1
print(lista)

# [s:e] [s:] [:e] start end
sub_lista = lista[0:1]  # nombre
sub_lista = lista[1:3]  # [20, 15.6]
sub_lista = lista[1:]  # [20, 15.6, True] desde el indice 1 en adelante # N: ultimos
sub_lista = lista[:3]  # ['nombre', 20, 15.6] los primeros 3 # :N primeros
sub_lista = lista[0:3:2]  # ['nombre', 15.6] salto de 2 en 2
sub_lista = lista[::-1]  # [True, 15.6, 20, 'nombre'] al reves 
print(sub_lista)

# agregar elemento
lista.append('add')
print(lista)
print(len(lista)) # 5 elementos
lista.insert(1, 'rails') # inserta elemento en indice 1, no lo reemplaza
print(lista)

# extender lista con otra lista
lista.extend(lista2)
print(lista)
# ['nombre', 'rails', 20, 15.6, True, 'add', 'apellido', 5, 0.2, False]

lista.remove('rails') # remover este elemento
print(lista)

del lista[1] # borrar elemento del indice 1
print(lista)

lista.clear() # limpiar lista
print(len(lista))  # 0 elementos

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
lista.sort()  # ordenar de menor a mayor
lista.sort(reverse=True)  # ordenar de mayor a menor
print(lista)

lista.sort() # ordenar
print(lista[0]) # el numero menor
print(lista[-1])  # el numero mayor
# ó
print(min(lista))
print(max(lista))

# se encuentra este elemento en esta lista?
print(10 in lista)  # False
print(5 in lista)  # True
print(11 not in lista)  # True , 11 no se encuentra
print(8 not in lista)  # False , 8 no se encuentra

index = lista.index(5)
print(index) # indice 3

# matriz
col_a = [10, 20]
col_b = [30, 40]
matriz = [col_a, col_b]
print(matriz)  # [[10, 20], [30, 40]]
print(matriz[0][0])  # en posicion x0, y0 está el 10
print(matriz[1][0])  # en posicion x1, y0 está el 30
print(matriz[1][1])  # en posicion x1, y1 está el 40
