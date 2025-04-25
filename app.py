
from flask import Flask, render_template

from cliente_dao import ClienteDAO #importamos la libreria Flask

titulo_app = "Zona Fit (GYM)"

app = Flask(__name__)

@app.route('/') #url: http://localhost:5000/
@app.route('/index.html') #url: http://localhost:5000/index.html

def inicio():
    app.logger.debug('Entramos al path de inicio /')
    # Recuperamos los clientes de la bd
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db) #renderizamos el template index.html

if __name__ == '__main__':
    app.run(debug=True, port=5000) #debug=True para que se reinicie el servidor al hacer cambios en el código
