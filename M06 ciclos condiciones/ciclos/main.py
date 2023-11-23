# None var vacía, no se sabe el valor aun, para no ocupar espacio en memoria
res = None # o Falso, todo lo vacío es falso
print(res)
print(type(res))

res = 10
res = res > 10
if res:
    print('cumple cond') # saltar 4 espacios por convención
# ó
if res > 10:
    print('cumple cond')  # saltar 4 espacios por convención

if res > 10 and res < 20:
    print('cumple cond')  # saltar 4 espacios por convención
else:
    print('no cumple cond')  # saltar 4 espacios por convención

print(res)

calificacion = 6
color = None

if calificacion == 10:
    print('aprobaste')  # saltar 4 espacios por convención
elif calificacion == 9 or calificacion == 6:
    print('aprobaste')  # saltar 4 espacios por convención
elif calificacion >=7:
    color = 'verde'
else:
    print('no aprobaste')  # saltar 4 espacios por convención

# o operador ternario
color = 'verde' if calificacion >= 7 else 'rojo'
print(color)

listado = [1]
listado = []
nombre = 'cody'
variable = nombre or 'codigo'  # cody
variable = '' or 0 or [] or True  # True
variable = listado or nombre # [1] o cody si []
print(variable)

numero = 1234
contador = 1
while contador <= 10:
    print(contador) # de 1 a 10
    contador = contador + 1

contador_digitos = 0
while numero >= 1:
    contador_digitos += 1
    numero = numero / 10
    print(contador_digitos)  # 4 (digitos)
else:
    print('fin ciclo')

usuarios = ['us1', 'us2', 'us3', 'us4']
for usuario in usuarios:
    print(usuario)

titulo_curso = 'Python'
for caracter in titulo_curso:
    
    """ if caracter == 'h':
        break
    print(caracter) # P y t """
    if caracter == 'o':
        continue
    print(caracter) # P y t h n

