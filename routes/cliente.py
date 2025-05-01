from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

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
    return render_template('lista_clientes.html', clientes=CLIENTES)

# inserir os dados do cliente no servidor
@cliente_rout.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json

    novo_usuario = {
        'id': len(CLIENTES) + 1,
        'nome': data['nome'],
        'email': data['email']
    }

    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)

# Form para cadastro de cliente
@cliente_rout.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

# Exibir dados de um cliente específico
@cliente_rout.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html')

# Formulario para editar um cliente
@cliente_rout.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html')

# Atualizar informações do cliente
@cliente_rout.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    pass

# Deletar um cliente específico
@cliente_rout.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    pass