# Docstring  comentarios en la funcion, atributo __doc__
# __doc__ (modulos, clases, metodos y funciones)
def suma(n1,n2):
  """
  La funcion suma 2 numeros

  Argumentos:
  n1(int)
  n2(int)

  Se retorna la suma de los parámetros

  TODO:
      *
  """
  return n1+n2


# print(suma.__doc__) # documentacion
print(help(suma))  # documentacion y valor
