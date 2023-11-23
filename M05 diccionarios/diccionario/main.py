# los diccionarios son mutables, podemos modificarlos, no se rigen por indices, solo con llave:valor
diccionario = {}
diccionario = dict()

# llave:valor
diccionario = {"total": 55}
diccionario = {"total": 55, "descuento": True, "subtotal": 15}
diccionario = {"total": 55, 10: "curso", (1,2,3): True}

# JSON = diccionario
usuario = {
  'nombre': 'nombre user',
  'edad': 23,
  'skills': {
    'programacion': True,
    'basedatos': False
  },
  'medallas': ['básico', 'intermedio']
}

# metodo items
for key, value in diccionario.items():
  print(key, value)

# metodo get
calificaciones = usuario.get('calificaciones', [])
if calificaciones:
  for calificacion in calificaciones:
    print(calificacion)
# si la lista está vacio no recorremos los valores

# metodo dict complication
usuarios = [ 'alfa', 'beta', 'gama']
diccionario = { usuario: position + 1
               for position, usuario in enumerate(usuarios)}
print(diccionario)

elementos = {} # diccionario
elementos['nombre'] = 'Cody'
elementos[(1,2,3)]='la llave es tupla'

elementos['nombre'] = 'Codigo' # actualizar valor de la llave
print(elementos)
print(len(elementos)) # 2 elementos

elementos = {'a':1,'b':2,'a':4}  # llave a será una sola, porq no se permiten llaves duplicadas
print(elementos)  # {'a': 4, 'b': 2} # a mantiene ultimo valor

diccionario = {'a': 1,'b':2,'c':3,'d':4}
valor = diccionario['d'] # 4
print(valor)

print('a' in diccionario) # True

# get
valor = diccionario.get('z')  # None
valor = diccionario.get('z', 'la llave no existe')  # si no existe retornar, la llave no existe
# setdefault
valor = diccionario.setdefault('z', 5) # agregar si no existe
print(valor)
print(diccionario)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'z': 5}

# keys
llaves = diccionario.keys()  # dict_keys(['a', 'b', 'c', 'd', 'z'])
llaves = tuple(diccionario.keys())  # ('a', 'b', 'c', 'd', 'z')
print(llaves)

# values
valores = diccionario.values()  # dict_values([1, 2, 3, 4, 5])
valores = tuple(diccionario.values())  # (1, 2, 3, 4, 5)
print(valores)

# items
elementos = diccionario.items()
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('z', 5)])
elementos = tuple(diccionario.items())
# (('a', 1), ('b', 2), ('c', 3), ('d', 4), ('z', 5))
print(elementos)

# eliminar elemento del diccionario
del diccionario['a']  # {'b': 2, 'c': 3, 'd': 4, 'z': 5}
# pop
valor = diccionario.pop('b')  # {'c': 3, 'd': 4, 'z': 5}

diccionario.clear()
print(diccionario)

