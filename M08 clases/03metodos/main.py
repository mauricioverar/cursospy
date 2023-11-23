# metodos

class Circulo:
  pi = 3.141592

# cls metodo de instancia por convencion
  @classmethod # inidicar q es metodo de clase
  def area(cls, radio): #metodo de instancia, ahora es metodo de clase
    return cls.pi * (radio ** 2)

resultado = Circulo.area(14) # metodo de clase
print(resultado)  # 615.752032

# get selft diccionariovalido