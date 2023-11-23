lenguajes = 'Python Ruby Java Rust C++ C'
listado_lenguajes = lenguajes.split() # divide elementos por espacio y agrega ,
print(listado_lenguajes)

lenguajes = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes = lenguajes.split('-')  # divide elementos por guión y agrega ,
listado_lenguajes = lenguajes.split('-')  # divide elementos por guión y agrega ,
# listado_lenguajes = lenguajes.split('-', 2)  # divide elementos por guión y agrega , solo a 2
print(listado_lenguajes)  # ['Python', 'Ruby', 'Java', 'Rust', 'C++', 'C']

lenguajes = ['Python', 'Ruby', 'Java', 'Rust']
# string_lenguajes = ' '.join(lenguajes)  # crear string uniendo con espacio
string_lenguajes = '|'.join(lenguajes)  # crear string uniendo con | u otro caracter
print(string_lenguajes)  # Python Ruby Java Rust
print(type(string_lenguajes)) # str

# los Strings son inmutables
nombre = 'Eduardo Ismael'
apellido = 'García'
# nombre_completo = nombre + ' ' + apellido  # concatenar  # Eduardo Ismael García
nombre_completo = '%s %s.' %(nombre, apellido)  # los %s se reemplazan por %()  # Eduardo Ismael García
nombre_completo = '%s %s.' %(nombre, apellido)  # los %s se reemplazan por %()  # Eduardo Ismael García
nombre_completo = 'Mr. %s %s %s.' % (nombre, apellido, 'Perez')
print(nombre_completo)

# nombre_completo = 'Mr. {} {} {}.'.format(nombre, apellido, 'Perez') # placeholders
# ó
""" nombre_completo = 'Mr. {nom} {ap1} {ap2}.'.format(
    nom=nombre, 
    ap1=apellido, 
    ap2='Perez'
) """

# Fstring
nombre_completo = f'Mr. {nombre} {apellido} {"Perez"} {10*20}' # interpolación
print(nombre_completo)

titulo_curso = 'Curso profesional de Python'
contador = titulo_curso.count('Python')  # contar coincidencias
# contador = titulo_curso.count('o')  # 4
# contador = titulo_curso.count('x')  # 0
print(contador) # 1

print('python' in titulo_curso.lower()) # existe python, cambiando todo a minusculas # True

# metodos
print(titulo_curso.startswith('Curso'))  # existe al comienzo? # True
print(titulo_curso.endswith('Curso'))  # existe al final? # False

msj = 'hi'
# msj = msj.ljust(20)  # justificar a la izquierda
# msj = msj.rjust(20)  # justificar a la derecha
msj = msj.center(20)  # justificar al centro 10 a cada lado
print(msj)
