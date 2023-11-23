# funciones
""" def suma():
    numero_uno = int(input('ingresa num: '))
    numero_dos = int(input('ingresa otro num: '))
    resultado = numero_uno + numero_dos
    print(resultado) """
# con parametros


def suma(numero_uno, numero_dos): # solo suma y retorna el resultado
    resultado = numero_uno + numero_dos
    # print(resultado)
    return resultado, 'fun 2 val' # resultado, msj # no retornar mas de 3 valores, usar destructuring (desempaquetar)


""" numero_uno = int(input('ingresa num: '))
numero_dos = int(input('ingresa otro num: '))

resultado, msj = suma(numero_uno, numero_dos)  # argumentos = valores de entrada
print('el resultado es : ', resultado)  # el resultado es :  (165, 'fun 2 val') (tupla)
print(msj)  # fun 2 val """

def area_circulo(radio, pi=3.14): # valor predeterminado, usar =numero pegado sin espacio por convencion
    return pi * (radio ** 2) # elevado a 2


# resultado = area_circulo(10, 3.14)  # 314.0
# resultado = area_circulo(10)  # 314.0
""" resultado = area_circulo(pi=3.1416, radio=10)  # con nombre no importa el orden
print(resultado) """

# def promedio(listado): # un parámetro
# def promedio(*listado): # sumar tod* al parámetro
def promedio(*args): # sumar tod* al parámetro # por convencion nombrar args
    print(type(args)) # tuple
    return sum(args) / len(args)

# resultado = promedio([10, 10, 5, 7, 10])  # 8.4 # un argumento
""" resultado = promedio(10, 10, 5, 7, 10)  # err # 5 argumentos # 8.4 con (*listado)
print(resultado) """


# entre funciones def debe dejar 2 lineas por convencion
def combinacion(p1, p2, *args, p4=500):
    print(p1)
    print(p2)
    print(args)
    print(p4)
# combinacion(10, 20, 1, 2, 3, 4, 5, p4=1000)


def usuarios(**kwards): # por convencion par diccionario
    print(kwards)  # {'edu': [10, 10, 8], 'fer': [10, 9, 9]}
    print(type(kwards))  # <class 'dict'>

# usuarios(edu=[10,10,8], fer=[10,9,9])


def combinacion(*args, **kwards): # tupla, diccionario(clave:valor)
    print(args)  # (1, 2, 3, 4, 5)
    print(kwards)  # {'cody': True, 'curso': 'Python'}

# combinacion(1,2,3,4,5, cody=True, curso='Python')


# Scope poseen alcances diferentes
animal = 'Leon' # var global

def imprimir_animal():
    # global animal # modificar la var global
    animal = 'Ballena' # vive dentro de la funcion var local
    print(animal)  # Ballena
    print(id(animal))  # 2024781122704
    tipo = 'mamifero' # solo dentro de un bloque , var local

    global varGlobal # crear var global
    varGlobal = 'animales' # asignar valor

"""
imprimir_animal()

print(animal)  # Leon
print(id(animal))  # 2024781122416
# print(tipo)  # NameError: name 'tipo' is not defined
print(varGlobal)  # animales es una var global creada en un local
"""


# def operacion():
def operacion(cantidad, balance, tipo='deposito'):  # tipo=default


    def deposito(cantidad, balance):
        return cantidad + balance


    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None

    """ print(deposito(10,20)) # 30
    # print(retiro(50, 80))  # 30
    print(retiro(50, 30))  # None """

    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)


# operacion()
""" resultado = operacion(10, 30)  # 40 # default deposito (la suma)
resultado = operacion(10, 30, 'retiro')  # 20 (la resta)
print(resultado) """

# funciones son ciudadanos de primera clase ***
def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

""" mi_funcion = centigrados_a_farhenheit
print(type(mi_funcion))  # <class 'function'>
print(mi_funcion(10)) # 50.0 """

# Lambdas
# lambda <params> : <cuerpo de la función>
funcion_grados = lambda grados : grados * 1.8 + 32 # función lambda
# print(funcion_grados(10)) # 50.0

""" sin_parametros = lambda : True
parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 + p3
asterisco = lambda *args, **kwards: len(args) + len(kwards) """

# callbacks
promedio = lambda *args : sum(args) / len(args) # var = funcion lambda : operación

aprobatorio = lambda calificacion : calificacion >= 7  # var = funcion lambda : condición

""" print(promedio(10,10,9,8,7)) # 8.8
print(aprobatorio(7)) # True """

def es_aprobatorio(calificacion):
    return calificacion >= 90

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args) # n cantidad de argumentos

    if func_aprobatorio(promedio):
        print(f'aprobaste con {promedio}')
    else:
        print('no aprobaste la materia')


# mostrar_mensaje(promedio, es_aprobatorio, 10, 10, 8, 7, 7)  # no aprobaste la materia
# mostrar_mensaje(promedio, aprobatorio, 10, 10, 8, 7, 7)  # aprobaste con 8.4

# closures *** una func genera otra func y esta puede acceder a las vars locales aunque hayan finalizado ***

e = 'e' # var global
def funcion_principal():
    a='a' # vars locales
    b='b'


    def funcion_anidada(): # bloque anidado
        c='c' # var local

        # nonlocal b # transformar en global # 2178223409200 y 2178223409200
        b= 'cambio valor'

        print(a)
        print(b)
        print(id(b))  # 2710684796976

        print(e)
    funcion_anidada()
    # print(c)  # NameError: name 'c' is not defined
    print(id(b))  # 140710201741568


# funcion_principal()
"""
a
b
e
"""

def saludar():

    def mostrar_mensaje():
        print('hi Python')

    return mostrar_mensaje

respuesta = saludar()
""" 
print(respuesta)  # <function saludar.<locals>.mostrar_mensaje at 0x000001BBDF8AE700>
print(type(respuesta))  # <class 'function'>

respuesta()  # hi Python """

# una vez que el bloque finaliza se destruyen las var
def saludar(username): # pero acá no se destruye la var local, porque la funcion crea el bloque, es closure
    mensaje = f'hola {username}' # loc var (cody) creada en Scope superior, nunca se destruye, queda en memoria

    def mostrar_mensaje(): # anidada , funcion con memoria, almacena la primera var
        print(mensaje)

    return mostrar_mensaje

username = 'cody'
respuesta = saludar(username)

username = 'edu'# aunque se modifique la var igual se mostrará cody porque queda en memoria en mostrar_mensaje

# respuesta()  # hola cody , acá recien usamos la var local


# decoradores *** funcion que toma como input una funcion

""" 
a ->  func principal (Decorador)    *shef
b ->  func a decorar                *masa
c ->  func decorada                 *pastel

a(b) -> c
"""
# estructura Decorador, una func_A que recibe una func_B como parametro y retorna otra func_C
""" def funcion_a(funcion_b):
    def funcion_c():
        # pass
        print('esta es la func_C')
    return funcion_c

@funcion_a # usar funcion_a para decorar la funcion saludar
def saludar():
    print('hi')

saludar()  # esta es la func_C """

# decorador
def funcion_a(funcion_b):
    def funcion_c():
        print('>>> antes del llamado') # tareas como conectar bd, enviar correo, leer un excel, etc
        funcion_b()
        print('>>> despues del llamado')
    return funcion_c


@funcion_a  # usar funcion_a para decorar la funcion saludar
def saludar():
    print('hi')
saludar()  # hi, ahora está decorando bien


@funcion_a  # usar funcion_a para decorar la funcion suma
def suma():
    print(10+30)
suma() # 40

""" 
>>> antes del llamado
40
>>> despues del llamado 
"""


# decorador -2
def funcion_a(funcion_b):
    # def funcion_c():
    # funcion con más acciones a realizar, ya que es la func decorada
    def funcion_c(*args, **kwargs):
        # tareas como conectar bd, enviar correo, leer un excel, etc
        print('>>> antes del llamado')
        # funcion_b()
        # funcion_b(*args, **kwargs)
        resultado = funcion_b(*args, **kwargs)
        print('>>> despues del llamado')
        return resultado
    return funcion_c


@funcion_a  # usar funcion_a para decorar la funcion saludar
def saludar():
    print('hi')


saludar()  # hi, ahora está decorando bien


@funcion_a  # usar funcion_a para decorar la funcion suma
def suma(n1, n2):
    return n1+n2


    # print(10+30)
resultado = suma(10, 30)  # 40
print(resultado)  # None

""" 
>>> antes del llamado
40
>>> despues del llamado 
"""
