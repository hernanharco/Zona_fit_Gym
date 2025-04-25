# Importamos la biblioteca `pymysql`.
# Esta es una biblioteca de Python para conectarse a bases de datos MySQL.
import pymysql
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

print("Todas las variables de entorno:")
for key, value in os.environ.items():
    print(f"{key}={value}")

print(f"--------------------------- \n")   

try:
    # Imprimimos un mensaje para indicar que estamos intentando conectar.
    print("Intentando conectar directamente...")

    # Intentamos establecer una conexión con la base de datos MySQL.
    connection = pymysql.connect(
        host=os.getenv('HOST'),           # Dirección del servidor MySQL
        port=int(os.getenv('DB_PORT')),   # Puerto del servidor MySQL
        user=os.getenv('DB_USERNAME'),       # Usuario de MySQL
        password=os.getenv('DB_PASSWORD'),   # Contraseña del usuario
        database=os.getenv('DATABASE')    # Nombre de la base de datos
    )

    # Si la conexión es exitosa, imprimimos un mensaje confirmando la conexión.
    print("Conexión exitosa:", connection)

except Exception as e:
    # Si ocurre algún error durante la conexión, capturamos la excepción y la imprimimos.
    print(f'Error al conectar: {e}')