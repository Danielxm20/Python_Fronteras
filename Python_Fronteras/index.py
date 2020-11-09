# Acá va a un comentario
if 3 > 5: # Acá va a un comentario
    print('Esto no se va a imprimir')

# if 5 > 3: # Acá va otro comentario
    # print('5 es mayor a 3')


x = 5
y = 'chanchito feliz'

print(x, y)

correo = 'chanchito@feliz.com'

print(correo)

_mi_var = 'chanchito'
MIVAR = 'chanchito'
a, b, c = 'Lala', 'Lele', 'Lili'

# print(a, b, c)

valor1 = valor2 = valor3 = 'Chanchito Feliz'

# print(valor1, valor2, valor3)

inicio = 'Hola'
final = 'mundo'

# print(inicio + final)

palabra = 'hola mundo' # string
oracion = "hola mundo comilla doble" # string
entero = 20 # integer
conDecimales = 20.2 # float
complejo = 1j

#print(palabra, oracion, entero, conDecimales, complejo)

lista = ['Hola', 'Mundo', 'Chanchito feliz']
lista2 = lista.copy() # copia la lista 
lista.append('Chanchito triste')
# lista.clear()
print("aqui",lista, lista2.count('Mundo')) # contador de elementos en este caso el 3
# print(len(lista), len(lista2))
largoLista = len(lista)
largoLista2 = len(lista2)

#print(largoLista, largoLista2)

# print(lista[2])

# lista.pop() # este elimina el último elemento de la lista
# lista.remove('Hola') # este elimina un elemento por su valor

#print(lista)
lista.reverse() # cambia el orden de los elementos en la lista del ultimo pasa a ser el primero
lista.sort() # ordena los valores alfabeticamente para strings 
print(lista)

tupla = ('hola', 'mundo', 'somos', 'tupla')
print(tupla)
print(tupla.count('hola')) # devuelve el numero de veces que 'hola' aparece en la tupla
print(tupla.index('mundo')) # devuelve el indice en que se encuentra el calor 'mundo'
listaDeTupla = list(tupla) # convierte la tupla en una lista
listaDeTupla.append('chanchito')
print(listaDeTupla)

rango = range(6)
print(rango)

diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}

print(diccionario)
print(diccionario['nombre']) # forma 1 de obtener el atributo nombre
print(diccionario['raza'])
print(diccionario.get('nombre')) # obtener el elemento nombre forma 2
diccionario['nombre'] = 'Fluffy' # reasignar un nombre

print(len(diccionario))

diccionario['ronronea'] = 'Si' # agregar una propiedad al diccionario

print(diccionario)
#diccionario.pop('ronronea') # elimina el valor 'ronronea'
#diccionario.popitem() # elimina el ultimo valor del diccionario
del diccionario['ronronea'] # otra forma de eliminar un valor del diccionario
#print(diccionario)
copiaGatito = diccionario.copy() #  copia el diccionario especificado
copiaGatito = dict(diccionario) # otra forma de copiar un diccionario
# del diccionario['ronronea']
diccionario.clear()
#print(diccionario, copiaGatito)

print("\nDICCIONARIOS COMO VARIABLES")
fluffy = { # diccionario usado como variable
    "nombre": "Fluffy",
    "edad": 4
}

mamba = { # diccionario usado como variable
    "nombre": "Black Mamba",
    "edad": 12
}

gatitos = { # diccionario anidado
    "Fluffy": fluffy, # al llamar a este diccionario imprime los valores en las variables definidas
    "Mamba": mamba # llama al diccionario mamba
}

print(gatitos)

perritos = dict(nombre="Chanchito Feliz", edad=6) # otra forma de crear diccionarios
print(perritos)

verdadero = True
falso = False

print(verdadero, falso)
