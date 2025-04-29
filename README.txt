
Recrea el Entorno Virtual
Otros desarrolladores pueden recrear el entorno virtual ejecutando:

	1. python -m venv venv
	2. source venv/bin/activate  # En Windows: venv\Scripts\activate
	3. pip install -r requirements.txt

APLICACIONES WEB con FLASK

Pasos a tener encuenta cuando se inicia en un nuevo portatil

Ver la version de Python

-> python --version
para trabajar con django pide que sea un version minimo 3.8

se mira la version de node

-> node --version

lo mejor que sea un version por encima de la 16

si no se tiene instalado seguir esta guia

https://kinsta.com/es/blog/como-instalar-node-js/

para equipos nuevos y crear un entorno virtual de python

pip install virtualenv

una vez instalado vamos a dar - el segundo venv es el nombre de la carpeta donde se va a guardar los comandos

-> python -m venv venv

- Ahora vamos a trabajar en el archivo activate pero podemos

	f1 - "Interpreter" - aqui debio aparecer (venv) no me aparecio en la terminal si aparece un error volver aqui
	
		o
			.\venv\Scripts\activate "Activar el entorno virtual OJO"
forma de arreglar el error del entorno virtual

1-> Ejecuta el siguiente comando para permitir la ejecución de scripts solo en la sesión actual:
powershell

Copy

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

Luego, intenta activar el entorno virtual nuevamente:

powershell

Copy .\venv\Scripts\activate "Activar el entorno virtual OJO"

Cambiar la política de ejecución de forma permanente (si lo necesitas frecuentemente): Abre PowerShell como administrador.
Ejecuta:

powershell

Copy

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

instalamos django

-> pip install django
-> RESUMEN <-

Si es un equipo que ya tiene todo instalado lo que debemos de hacer

1. Creamos la carpeta con el nombre que deseamos
	2. Se abre con visual studio se puede arrastras
 	3. Se crea la carpeta virtual que el comando es:
  		python -m venv venv
4. En la terminal activamos el entorno virtual para esto hacemos el siguiente comando:
	.\venv\Scripts\activate


--> INSTALACIONES DE FLASK <--
1. En el entorno virtual
	python -m pip install flask
	
	2. Creamos el archivo app.py y colocamos informacion en este
	

2. Creando contenidos HTML para esto
	2.1 para esto creamos una carpeta templates
		2.1.1 creamos el archivo index.html
		
		3.1.2 Instalacion de Bootstrap - 295 - Respuesta y contenido FLASK nos dirigimos a la siguiente pagina
			https://getbootstrap.com/docs/5.3/getting-started/introduction/
			copiamos el contenido 2. include bootstrap y lo poenmos en nuestro proyecto en el archivo index.html
			
			a. en el html index cambiamos el title el lang="es" lo colocamos en español y agregamos el 
				modo oscuro ingresando data-bs-theme="dark"
		
		3.1.3 Envio de Parametros dinamicos
			a. en el archivo app.py creamos la variable titulo_app y en la parte de return agregamos titulo=titulo_app 			
				con esto podemos pasar las variables
				
			b. en el archivo de index.html para agregar este parametro lo que hacemos en trabajar con {{}}
		
		3.2 Se va a trabajar con darle estilo al titulo
			agregamos el icono al titulo y esterilizamos colocando estilos de bootstrap
		
		3.3 Manejo de Grid -> vamos a trabajar el panel lateral y el el contenido central este es un diseño que utiliza
		en muchos proyectos
			3.3.1 seguimos trabajando en el archivo index.html video 298. Manejo de Grid con Bootstrap
				a. en la clase se maneja el container-fluid que este permite que se haga el contenedor de manera horizontal
				y este se expanda
					- pb-3 -> padding en para manejar el espacio en la parte inferior
					- class="d-grid gap-3" style="grid-template-columns: 1f 2fr;" -> esto es para dibujar los espacios que 
					van a utilizar en pantalla el gap-3 -> es el espacio que va a manejar entre cada contenedor
				
				b. Vamos a crear la tabla para los datos en este caso estamos en index.html
					en la parte de <!-- aca va el listado de clientes -->
			
			3.4 Conexion a MySql video 300. Tabla de Clientes Estática con Bootstrap
				a. pip install mysql-connector-python
					pip show mysql-connector-python -> para ver que la instalacion fue correcta
				b. trabajamos en app.py y agregamos desde el comentario que dice #Recuperamos los clientes de la bd
					- vamos a la plantilla de index.html en donde vamos a tomar los datos que se encuentran en la bd ya
					para esto hemos pasado los datos necesarios
						- agregamos el ciclo for utilizando jinja
						
				-> Error <- Por mas que tenia todo los pasos este no se conectaba correctamente a la base de datos
				1. Verifica si MySQL está instalado
					Primero, asegúrate de que MySQL está instalado en tu sistema. Si usas XAMPP, MySQL debería estar incluido, pero necesitas acceder a él correctamente.

					Pasos:
						1. Ve a la carpeta de instalación de XAMPP (por ejemplo, C:\xampp).
						2. Navega hasta la carpeta mysql\bin. Por ejemplo:

							1 C:\xampp\mysql\bin
							
						3. Busca el archivo ejecutable mysql.exe. Si existe, entonces MySQL está instalado.
						
				2. Agrega MySQL al PATH del sistema
					Para poder usar el comando mysql desde cualquier terminal, necesitas agregar la ruta de la carpeta mysql\bin a la variable de entorno PATH.

					-->  Pasos para Windows: <--
						1. Abre el Panel de Control y ve a Sistema > Configuración avanzada del sistema .
						2. Haz clic en el botón Variables de entorno .
						3. En la sección Variables del sistema , busca la variable Path y haz clic en Editar .
						4. Haz clic en Nuevo y agrega la ruta completa a la carpeta mysql\bin. Por ejemplo:

							1	C:\xampp\mysql\bin
							
						5. Haz clic en Aceptar para guardar los cambios.
						
					-->  Pasos para Linux/macOS: <--
					
						1. Abre un terminal y edita el archivo de configuración de tu shell. Por ejemplo, para bash, edita .bashrc o .zshrc:
						bash

							1	nano ~/.bashrc
						
						2. Agrega la siguiente línea al final del archivo:
						bash


							1	export PATH=$PATH:/ruta/a/mysql/bin
							Reemplaza /ruta/a/mysql/bin con la ubicación real de la carpeta mysql\bin.
							
						3. Guarda el archivo y actualiza la configuración:
						bash


							1	source ~/.bashrc
							
				3. Prueba el comando mysql nuevamente
					Después de agregar MySQL al PATH, abre una nueva terminal y prueba el comando nuevamente:

						bash

						1 mysql -u root -padmin -h localhost -P 3306
					
					Si todo está configurado correctamente, deberías poder conectarte a MySQL sin problemas.

				4. Alternativa: Usa la ruta completa al ejecutable
					
				Si no quieres modificar la variable PATH, puedes usar la ruta completa al ejecutable mysql.exe cada vez que necesites ejecutarlo. Por ejemplo:

					bash

					1 C:\xampp\mysql\bin\mysql.exe -u root -padmin -h localhost -P 3306
					
					Esto es menos conveniente, pero funciona si solo necesitas ejecutar el comando ocasionalmente.

				5. Verifica que MySQL esté iniciado
					Asegúrate de que el servicio de MySQL esté iniciado en XAMPP:

					1. Abre el XAMPP Control Panel .
					2. Verifica que el servicio MySQL esté iniciado. Si no lo está, haz clic en el botón Start junto a MySQL.
					
				6. Solución alternativa: Usa phpMyAdmin
					
					Si no puedes resolver el problema con el comando mysql, puedes verificar la conexión a la base de datos usando phpMyAdmin :

						1.	Abre un navegador y ve a:

							1	 http://localhost/phpmyadmin
						2. Inicia sesión con el usuario root y la contraseña admin.
						3. Verifica que la base de datos zona_fit_db exista y que los permisos estén configurados correctamente.
						
				Resumen de pasos
				
					1. Verifica si MySQL está instalado.
					2. Agrega la carpeta mysql\bin al PATH del sistema.
					3. Prueba el comando mysql nuevamente.
					4. Asegúrate de que el servicio MySQL esté iniciado en XAMPP.
					5. Usa la ruta completa al ejecutable si no quieres modificar el PATH.
					6. Como alternativa, verifica la conexión usando phpMyAdmin.
					7. Para la parte de actulizacion de contraseña podemos ingresar a 
						D:\xampp\phpMyAdmin\config.inc.php y en la parte de $cfg['Servers'][$i]['password'] se cambia
					8. Para cambiar el puerto de conexion
						D:\xampp\mysql\bin\my.ini
					9. Hice varias pruebas y con mysql.connector no me dejo conectar lo que encontre fue utilizar pymysql
						pip install pymysql
					10. Para poder hacer funcionar la conexion a partir de Pool debi utilizar otra biblioteca
						pip install dbutils
						
					DATABASE=zona_fit_db
					DB_USERNAME=
					DB_PASSWORD=
					DB_PORT=
					HOST=localhost
					POOL_SIZE=5
					POOL_NAME=zona_fit_pool
						
			3.5 Manejo de Formulario la parte de izquierda
			
			3.6 Instalacion de WTForm y FLASK -> esto se utiliza para relacionar el form con una clase
				pip install flask-wtf
				3.6.1 Creamos la clase cliente_forma.py
				
				3.6.2 En app.py 
					Creamos un objeto del cliente form vacio
				
				3.6.3 Esta generando el siguiente error
					RuntimeError: A secret key is required to use CSRF.
					para solucionar este error en la clase app.py
						debemos agregar el siguiente codigo 
							app.config['SECRET_KEY'] = 'una_clave_secreta_muy_segura'  # Necesario para proteger el formulario con CSRF
						
						b. Despues debemos de ir a index.html
							agregamos esta linea de codigo y con esto solucionamos {{ forma.csrf_token }}
						
						c. hay dos campos que se agregaron y como se esta trabajando el formulario desde una clase entonces los datos a mostra puede ser de forma dinamica
							{{forma.nombre(class="form-control", placeholder="Nombre")}}
							{{forma.nombre.label(class="form-label")}}
			
	2.2 Guardar la Informacion del Formulario
		
		3.7.1 vamos a la clase app.py y agregamos codigo despues del @app.route('/guardar', methods=['POST'])
		
		3.8 Limpiar el Formulario
			en la clase de app.py se agrega la linea de codigo	
				@app.route('/limpiar')
				
	2.3 Cargar Cliente Seleccionado
		2.3.1 en la clase de app.py agregamos @app.route('/editar/<int:id>')
		2.3.2 en la clase cliente_dao.py debemos de utilizar SELECCIONAR_ID = y creamos el metodo def selecciona_por_id(cls):
	
	2.4 Campo de id oculto esto es para poder modificar una informacion
		En index.html agregamos lo campos <!-- Valor de Id -->
		2.4.1 en ClienteForma se trabaja con el id = HiddenField('id')
		2.4.2 en index.html agregamos {{forma.id}}
		
	2.5 Actualizar un Registro Existente
		en def guardar() agregamos el if en donde se puede actualizar la informacion
	
	2.6 Para eliminar agregamos la linea @app.route('/eliminar/<int:id>')  # localhost:5000/eliminar/1

