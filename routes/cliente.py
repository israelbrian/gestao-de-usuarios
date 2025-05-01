from flask import Blueprint

cliente_rout = Blueprint('cliente', __name__)

"""
    Rotas do cliente

    - /clientes/ (GET) - Listar todos os clientes
    - /clientes/ (POST) - Inserir o cliente no servidor
    - /clientes/new (GET - Renderizar o formulário de criação de um cliente
    - /clientes/<id> (GET) - Obter os dados de um cliente específico
    - /clientes/<id>/edit (GET) - Renderizar o formulário de edição de um cliente
    - /clientes/<id>/update (PUT) - Atualizar os dados do cliente
    - /clientes/<id>/delete (DELETE) - Deletar um cliente específico
"""

# listar todos os clientes
@cliente_rout.route('/')
def lista_clientes():
    return {'pagina': "lista_clientes"}

# inserir os dados do cliente no servidor
@cliente_rout.route('/', methods=['POST'])
def inserir_cliente():
    pass

# Form para cadastro de cliente
@cliente_rout.route('/new')
def form_cliente():
    return {'pagina': "formulario clientes"}

# Exibir um cliente específico
@cliente_rout.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    pass

# Formulario para editar um cliente
@cliente_rout.route('/<int:cliente_id/edit>')
def form_edit_cliente(cliente_id):
    pass

# Atualizar informações do cliente
@cliente_rout.route('/<int:cliente_id/update>', methods=['PUT'])
def update_cliente(cliente_id):
    pass

# Deletar um cliente específico
@cliente_rout.route('/<int:cliente_id/delete>', methods=['DELETE'])
def deletar_cliente(cliente_id):
    pass