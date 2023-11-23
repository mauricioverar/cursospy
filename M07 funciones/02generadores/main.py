# generador
def pares(): # Lazy iterator iteración perezosa
  for numero in range(0,10,2): # de 0 a 10 en pares
    # print(numero) # 0 a 98
    """ return numero # 0
    print('aca no se ejecutará porque la func termina en return') """
    # yield suspende de forma momentanea
    yield numero  # <generator object pares at 0x000002DBCBB3DFF0>
    print('se reanuda')

# print(pares())

""" for par in pares():
  print(par) # numero y texto """

generador = pares()

""" print(next(generador))#0
print(next(generador))#2
print(next(generador))#4
print('ejecutamos codigo entre un llamado y otro')
print(next(generador))#6
print(next(generador))  # 8
print(next(generador))  # 10 err StopIteration """

while True:
  try: # tipo try-catch
    par = next(generador)
    print(par)
  except StopIteration: # evitar err
    print('el generador finalizó')
    break