
from flask import Flask, redirect, render_template, url_for

from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_forma import ClienteForma  # importamos la libreria Flask

titulo_app = "Zona Fit (GYM)"

app = Flask(__name__)

# Necesario para proteger el formulario con CSRF
app.config['SECRET_KEY'] = 'una_clave_secreta_muy_segura'


@app.route('/')  # url: http://localhost:5000/
@app.route('/index.html')  # url: http://localhost:5000/index.html
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    # Recuperamos los clientes de la bd
    clientes_db = ClienteDAO.seleccionar()
    # Creamos un objeto de cliente form vacio
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db,
                           forma=cliente_forma)  # renderizamos el template index.html


@app.route('/guardar', methods=['POST'])  # url: http://localhost:5000/guardar
def guardar():
    # Creamos los objetos de cliente inicialmente objetos vacios
    cliente = Cliente()
    cliente_forma = ClienteForma(obj=cliente)
    # Validamos el formulario
    if cliente_forma.validate_on_submit():
        # Llenamos el objeto cliente con los valores del formulario
        # Tambien se recupera el id oculto del formulario
        cliente_forma.populate_obj(cliente)
        if not cliente.id:
            # Guardamos el cliente en la base de datos
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)
    # Redirigimos al usuario a la pagina de inicio
    return redirect(url_for('inicio'))


@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))


@app.route('/editar/<int:id>')  # localhost:5000/editar/1
def editar(id):
    cliente = ClienteDAO.selecciona_por_id(id)
    cliente_forma = ClienteForma(obj=cliente)
    # Recuperar el listado de clientes para volver a mostrarlo
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app,
                           clientes=clientes_db,
                           forma=cliente_forma)


@app.route('/eliminar/<int:id>')  # localhost:5000/eliminar/1
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    # debug=True para que se reinicie el servidor al hacer cambios en el código
    app.run(debug=True, port=5000)
