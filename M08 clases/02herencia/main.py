# herencia, a mayor nivel herarquico mas abstracta y amenor nivel herarquico mas concreta
""" class Animal(): # clase Abuelo mas abstracta ***
  def comer(self):
    print(f'{self.nombre} come')

  def dormir(self):
    print(f'{self.nombre} duerme')

class Mascota(Animal): # clase Padre
  pass

class Felino:
  def cazar(self):
    print(f'{self.nombre} caza')

class Perro(Mascota):  # clase hija hereda Mascota
  pass


class Gato(Mascota, Felino):  # clase hija hereda Mascota y Felino mas concreta ***
  def __init__(self, nombre) -> None:
    self.nombre = nombre


# duke = Perro()
# duke.comer()
# duke.dormir()

pat = Gato('Pat')
pat.comer() # buscar metodo comer en clases hacia arriba herarquía, Mascota, Felino, Animal
pat.dormir()
pat.cazar() """


# funcion super

class Animal():  # clase Abuelo mas abstracta ***
  def comer(self):
    print(f'el animal come')

  def dormir(self):
    print(f'{self.nombre} duerme')


class Mascota(Animal):  # clase Padre
  pass


class Felino:
  def cazar(self):
    print(f'{self.nombre} caza')


class Perro(Mascota):  # clase hija hereda Mascota
  pass


class Gato(Mascota, Felino):  # clase hija hereda Mascota y Felino mas concreta ***
  def __init__(self, nombre) -> None:
    self.nombre = nombre

  def comer(self):
    super().comer() # usar metodo de la clase padre
    print(f'{self.nombre} come')


""" duke = Perro()
duke.comer()
duke.dormir() """

pat = Gato('Pat')
pat.comer()  # buscar metodo comer en clases hacia arriba herarquía, Mascota, Felino, Animal

