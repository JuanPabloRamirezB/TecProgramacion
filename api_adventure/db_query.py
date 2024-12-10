# import sqlite3
# conn = sqlite3.connect("books.db")
# cur = conn.cursor()
# cur.execute("SELECT * FROM book")
# books = cur.fetchall()
# for book in books:
#     print(book)
import psycopg2
from psycopg2 import sql

# Parámetros de conexión
conexion = psycopg2.connect(
    host="localhost",
    database="adventuretime",
    port=5000,
    user="mi_usuario",
    password="mi_contraseña"
)

# Crear un cursor
cursor = conexion.cursor()

# Escribir una consulta SQL
consulta = "SELECT * FROM mi_tabla;"

# Ejecutar la consulta
cursor.execute(consulta)

# Obtener los resultados
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

