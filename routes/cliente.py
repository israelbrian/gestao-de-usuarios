from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

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
@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html', clientes=CLIENTES)

# inserir os dados do cliente no servidor
@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    data = request.json

    novo_usuario = {
        'id': len(CLIENTES) + 1,
        'nome': data['nome'],
        'email': data['email'],
    }

    CLIENTES.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)

# Form para cadastro de cliente
@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

# Exibir dados de um cliente específico
@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    cliente = list(filter(lambda c: c['id'] == cliente_id, CLIENTES))[0]
    return render_template('detalhe_cliente.html', cliente=cliente)

# Formulario para editar um cliente
@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c                  

    # cliente = next((c for c in CLIENTES if c['id'] == cliente_id), None)
    # if not cliente:
    #     return "Cliente não encontrado", 404
    
    return render_template('form_cliente.html', cliente=cliente)

# Atualizar informações do cliente
@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    cliente_editado = None
    # obter dados do user pelo formulário de edicao
    data = request.json
         
    # obter usuario pelo id 
    for c in CLIENTES:
        if c['id'] == cliente_id:
            c['nome'] = data['nome']
            c['email'] = data['email']

            cliente_editado = c

    # editar usuario 
    return render_template('item_cliente.html', cliente=cliente_editado)

# Deletar um cliente específico
@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id]
    return {'delete': 'ok'}