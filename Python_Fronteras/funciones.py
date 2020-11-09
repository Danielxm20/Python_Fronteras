
def miFuncion():
    print('Mi primera función!')

# miFuncion()

def imprimeDato(*nombre):
    print('El nombre es:', nombre[1])

# imprimeDato('Chanchito', 'Feliz', 'lala', 'lele')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

# nombreCompleto(nombre='Chanchito', apellido='Feliz')

def nombreCompleto2(**kwargs): # Recibe argumentos y los maneja como diccionario kwargs es argumentos llave
    print(kwargs['nombre'], kwargs['apellido'])


# nombreCompleto2(nombre='Chanchito', apellido='Feliz')


def miFuncion2(argumento = 'Chanchito'): # la funcion tiene un argumento por defecto
    print(argumento)

# miFuncion2('Batman')
# miFuncion2() # al no pasar arguemnto la funcion utiliza el argumento por defecto

def miFuncionLista(lista):
    for el in lista:
        print(el)

# miFuncionLista(['Chanchito', 'Feliz', 'Perro', 'Berro'])


def concatenaNombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

# nombres = concatenaNombres(['Chanchito', 'Feliz', 'Gordo'])
# print(nombres)

def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)
