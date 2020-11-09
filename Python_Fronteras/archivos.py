c = open('chanchito.txt', 'a') # r= read, a=append, w=write, x=crear archivo

#c.write('\nagregaremos una nueva línea a chanchito') # agrega una linea al final del archivo

c.close()

x = open('chanchito.txt')

print(x.read()) # lee todo el archivo
# print(x.readline()) #lee solo una linea del archivo

# for l in x: # iterar por todas las lineas del archivo
#     print(l)

x.close()

import os

if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print('El archivo no existe')

#os.rmdir('micarpeta') #eliminar carpeta
