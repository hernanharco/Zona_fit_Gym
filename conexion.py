# Importamos las bibliotecas necesarias
import pymysql
from dbutils.pooled_db import PooledDB
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Conexion:
    # Leer las variables de entorno
    DATABASE = os.getenv('DATABASE')  # Nombre de la base de datos
    USERNAME = os.getenv('DB_USERNAME')  # Usuario de MySQL
    PASSWORD = os.getenv('DB_PASSWORD')  # Contraseña del usuario
    # Puerto personalizado donde MySQL está escuchando
    DB_PORT = int(os.getenv('DB_PORT'))
    HOST = os.getenv('HOST')           # Dirección del servidor MySQL
    POOL_SIZE = int(os.getenv('POOL_SIZE'))  # Tamaño del pool de conexiones
    POOL_NAME = os.getenv('POOL_NAME')  # Nombre del pool (opcional)
    pool = None                        # Variable para almacenar el pool de conexiones

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # Si el pool no ha sido creado
            try:
                print("Intentando crear el pool...")
                # print(f"Parámetros de conexión: "
                #      f"Host={cls.HOST}, Port={cls.DB_PORT}, Database={cls.DATABASE}, User={cls.USERNAME}")

                # Creamos el pool de conexiones usando DBUtils.PooledDB
                cls.pool = PooledDB(
                    creator=pymysql,  # Usamos pymysql como creador de conexiones
                    maxconnections=cls.POOL_SIZE,  # Tamaño máximo del pool
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    database=cls.DATABASE,
                )
                print("Pool creado exitosamente.")
                return cls.pool
            except Exception as e:
                print(f'Ocurrió un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        # Obtiene una conexión del pool
        return cls.obtener_pool().connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        # Libera la conexión devolviéndola al pool
        conexion.close()
        print("Conexión liberada.")


if __name__ == '__main__':
    print("Iniciando el script...")

    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)

    # Obtenemos una conexión del pool
    conexion1 = Conexion.obtener_conexion()
    print(conexion1)

    # Liberamos la conexión
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion1')
