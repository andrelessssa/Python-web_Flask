from flask import Flask, url_for, render_template
# pip install flask

# caminho
# ROtas / Metodos / Requisição / Respostas
# status code web - 200 bem sucedida 404 rota nao encontrada 405 rota existe mas nao suporta 500 erro no backend


#inicializacao
app = Flask(__name__) # inicializo o flask

# rotas
@app.route('/')
def ola_mundo(): # da requisicao sempre tera um returno 

    titulo = "Gestão de Usuários"
    usuarios = [
        {'nome': 'João', 'membro_ativo': False},
        {'nome': 'André', 'membro_ativo': True},
        {'nome': 'Guilherme', 'membro_ativo': False}
    ]
    return render_template ('index.html', titulo=titulo , usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return """"
        <b>Programador André<b>: Assista
        <a href="https://www.youtube.com/watch?v=tlC90zjDCwg&list=PL39zbyHjgjrbsP3xFSc-YH-6FN8WNpglh">aqui</a>
    """



#execucao
app.run(debug=True) # estamos no modo desenvolvedor entao ele fica reinicia o servicor




