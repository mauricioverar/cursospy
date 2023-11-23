# clases
""" class Usuario:
  pass

cody = Usuario()
print(cody)  """ # <__main__.usuario object at 0x000001641C537F80>


# atributos de clases , le pertenecen a una clase
""" class Usuario:
  username = 'username predeterminado' # atributos que pertenecen a la clase Usuario
  email = ''

Usuario.username = 'User1'
Usuario.email = 'a@web.cl'

print(Usuario.username)
print(Usuario.email) """


# atributos de instancia , le pertenecen a un objeto
""" class Usuario:
  username = 'username predeterminado' # atributos que pertenecen a la clase Usuario
  email = ''

# __dict__ # meta atributo

user1 = Usuario()

print(user1.username)  # username predeterminado
print(user1.__dict__) # {}

print(id(user1.username)) # 2348913443376
print(id(Usuario.username))  # 2348913443376

# si no encuentra el att dentro de un objeto, buscará dentro de la clase, sino tira err

user1.username = 'cody'  # agrega nuevo atributo al objeto con valor inicial
user1.password = '1234'  # agrega nuevo atributo al objeto

print(user1.__dict__)  # {'username': 'cody'}
print(user1.username) # atributo de instancia

print(id(user1.username))  # 2592687981312
print(id(Usuario.username)) """  # 2592687964720 # son diferentes


""" class Usuario:
  # metodo inicializar
  def inicializar(self, username, password): # self hace referencia a si mismo, mas 2 params
    self.username = username
    self.password = password

user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

user1.inicializar('User1', 'password1') # para q el objeto posea los dos att username y password
user2.inicializar('User2', 'password2')
user3.inicializar('cody', 'password3')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__) """


# __init__  para definir e inicializar atributos para los objetos de la clase
class Usuario:
  def __init__(self, username='', password=''): # 2 atributos
    # pass
    self.username = username
    self.password = password

user1 = Usuario('User1', 'password1')
user2 = Usuario('User2', 'password2')
user3 = Usuario('cody', 'password3')
user4 = Usuario() # adquiere los defaults values

print(user1.__dict__)  # {'username': '', 'password': ''}
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)
