from flask import Flask
from routes.home import home_rout
from routes.cliente import cliente_rout


# Inicialização
app = Flask(__name__)

app.register_blueprint(home_rout)
app.register_blueprint(cliente_rout, url_prefix='/clientes')

# Execução
app.run(debug=True)