# rotas da cliente
# tenho que consultar a documentacao sempre pra fazer blueprint
#Rota de CLiente
# - /cliente/ (GET) listar os clientes
# - /cliente/ (POST) inserir um cliente
# - /cliente/new (GET) renderizar o formulario para criar um usuario
# - /cliente/<id> (GET) obter os dados de um cliente
# - /cliente/<id>/edit (GET) renderizar o formulario parar editar um cliente
# - /cliente/<id>/edit (PUT) atualizar os dados de um cliente
# - /cliente/<id>/delete (DELETE) deletar o registro do usuario



from flask import Blueprint, render_template, request
from data.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_cliente.html', clientes=CLIENTES)


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

       

@cliente_route.route('/new')
def form_cliente():  
    return render_template('form_cliente.html')  


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):  
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):  
       return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):  
    pass    


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):  
    pass    
