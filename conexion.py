# Importamos las bibliotecas necesarias
import pymysql
from dbutils.pooled_db import PooledDB

class Conexion:
    DATABASE = 'zona_fit_db'  # Nombre de la base de datos
    USERNAME = 'root'         # Usuario de MySQL
    PASSWORD = 'admin'        # Contraseña del usuario
    DB_PORT = 3329            # Puerto personalizado donde MySQL está escuchando
    HOST = 'localhost'        # Dirección del servidor MySQL
    POOL_SIZE = 5             # Tamaño del pool de conexiones
    POOL_NAME = 'zona_fit_pool'  # Nombre del pool (opcional)
    pool = None               # Variable para almacenar el pool de conexiones

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # Si el pool no ha sido creado
            try:
                print("Intentando crear el pool...")
                #print(f"Parámetros de conexión: "
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