import modulos # importa todo el modulo
import modulos as xs # xs es el nombre con el que identificaremos a modulos en este program
from modulos import saludo, mascotas # imoporta de modulos solo la info requerida en lugar de todo el modulo
from camelcase import CamelCase

print(modulos.mascotas)
modulos.saludo('Daniel')

print(xs.mascotas)
xs.saludo('Nicolas')

c = CamelCase()
s = 'esta oración necesita CamelCase!'

camelcased = c.hump(s)
print(camelcased)
