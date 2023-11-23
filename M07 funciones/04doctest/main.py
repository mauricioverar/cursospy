# doctest
# >>> a probar
# resultado esperado
def suma(n1,n2):
  """
  La funcion suma 2 numeros

  Argumentos:
  n1(int)
  n2(int)

  Se retorna la suma de los parámetros

  >>> suma(10, 20)
  30

  >>> suma(100, 200)
  500
  """
  return n1+n2

# poner en consola:
# python -m doctest main.py

# si no imprime nada es que no hay errores
""" 
Expected:
    500
Got:
    300 
    **********************************************************************
1 items had failures:
  1 of   2 in main.suma
***Test Failed*** 1 failures.
"""