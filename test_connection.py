# Importamos la biblioteca `pymysql`.
# Esta es una biblioteca de Python para conectarse a bases de datos MySQL.
import pymysql

try:
    # Imprimimos un mensaje para indicar que estamos intentando conectar.
    # Esto es útil para depurar y verificar que el script llega a este punto.
    print("Intentando conectar directamente...")
    
    # Intentamos establecer una conexión con la base de datos MySQL.
    # Usamos el método `pymysql.connect()` para crear la conexión.
    connection = pymysql.connect(
        host='localhost',  # Dirección del servidor MySQL. 'localhost' significa que el servidor está en la misma máquina.
        port=3329,         # Puerto personalizado donde MySQL está escuchando. En este caso, usas el puerto 3329.
        database='zona_fit_db',   # Nombre de la base de datos a la que quieres conectarte. Aquí, es 'test'.
        user='root',       # Usuario de MySQL. 'root' es el usuario administrador predeterminado.
        password='admin',  # Contraseña del usuario 'root'. Aquí, la contraseña es 'admin'.
        cursorclass=pymysql.cursors.DictCursor  # Especificamos el tipo de cursor que queremos usar.
                                                # `DictCursor` devuelve los resultados de las consultas como diccionarios,
                                                # lo que facilita trabajar con los datos en Python.
    )
    
    # Si la conexión es exitosa, imprimimos un mensaje confirmando la conexión.
    # También mostramos el objeto de conexión (`connection`) para verificar que se creó correctamente.
    print("Conexión exitosa:", connection)
    
except Exception as e:
    # Si ocurre algún error durante la conexión, capturamos la excepción y la imprimimos.
    # Esto nos ayuda a identificar problemas como errores de autenticación, puertos incorrectos, etc.
    print(f'Error al conectar: {e}')