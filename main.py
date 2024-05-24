from flask import Flask
# pip install flask
from routes.home import home_route
from routes.cliente import cliente_route


#inicializacao
app = Flask(__name__) # inicializo o flask

app.register_blueprint(home_route)
app.register_blueprint(cliente_route, url_prefix='/clientes')


app.run(debug=True)




# rotas
# @app.route('/')
# def ola_mundo(): # da requisicao sempre tera um returno 
#    usuarios = [
#        {'nome': 'João', 'membro_ativo': False},
#        {'nome': 'André', 'membro_ativo': True},
#        {'nome': 'Guilherme', 'membro_ativo': False}
#    ]
#    return render_template ('index.html', titulo=titulo , usuarios=usuarios)
# def pagina_sobre():
#    return """"
#        <b>Programador André<b>: Assista
#        <a href="https://www.youtube.com/watch?v=tlC90zjDCwg&list=PL39zbyHjgjrbsP3xFSc-YH-6FN8WNpglh">aqui</a>
#    """



 # estamos no modo desenvolvedor entao ele fica reinicia o servicor




