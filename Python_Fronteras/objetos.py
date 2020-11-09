class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)


class Admin(Usuario): # Se crea la clase Admin que hereda de Usuario
    def superSaludo(self):
        print('Hola!, me llamo,', self.nombre, ' y soy administrador')

usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('Ximena', 'CO')

usuario.saludo()
usuario.nombre = 'Chanchito' # cambia la propiedad nombre del objeto
usuario.saludo()
usuario2.saludo()
# # del usuario.nombre # elimina la propiedad nombre
# # del usuario # elimina el objeto usuario
# # print(usuario)

admin = Admin('Super', 'Feliz')
admin.saludo()
admin.superSaludo()

#usuario.superSaludo() # la instacia de la clase padre no puede acceder a los metodos de la clase hijo
print("\nEJERCICIO DE HERENCIA\n")

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print('Hola, soy un', self.tipo, 'y mi sonido es el', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya): # constructor de la clase gato
        Animal.__init__(self, nombre, onomatopeya) # Se utiliza para ejecutar el metodo init de la clase padre de lo contrario no se ejecutaria
        print('Hola, soy un gato extendido!')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya): # init de la clase Perro
        super().__init__(nombre, onomatopeya) # inir de la clase padre de esta forma no es necesario el self
        print('instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()
