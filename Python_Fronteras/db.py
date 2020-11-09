import mysql.connector

midb = mysql.connector.connect(host='localhost', user='dany', password='redamerica10', database='prueba')

cursor = midb.cursor()

# ********************CONSULTAR DATOS**********************
cursor.execute('select * from usuario')
resultado = cursor.fetchall() # devuelve todos los resultados de la consulta
#resultado = cursor.fetchone() # devuelve solo el primer resultado
print(resultado)

# LIMITAR LA CONSULTA DE DATOS CON LIMIT**********
cursor.execute('select * from usuario limit 1')
resultado = cursor.fetchall() # devuelve todos los resultados de la consulta
#resultado = cursor.fetchone() # devuelve solo el primer resultado
print(resultado)

# ****************INSERTAR DATOS*************************************
# sql = 'insert into usuario (id, username, email) values(%s, %s, %s)'
# values = (2, 'americo', 'hola@yahoo.com')
# cursor.execute(sql, values) # ejecuta la sentencia
# midb.commit() # envia los datos a la base de datos
#print(cursor.rowcount)

# ********VER DEFINICIONES DE TABLAS**************
# cursor.execute('show create table usuario')
# re=cursor.fetchone()
# print(re)

# ************* ACTUALIZAR DATOS************
# sql = 'update usuario set email = %s where id = %s'
# values = ('micorreo@correo.com', 2)
# cursor.execute(sql, values)
# midb.commit() 

# ***********ELIMINAR DATOS*********************
# sql = 'delete from usuario where id = %s'
# values = (2,) # auque sea un solo valor se tiene que poner la coma
# cursor.execute(sql, values)
# midb.commit() 