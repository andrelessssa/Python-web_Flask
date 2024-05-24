from flask import Flask
# pip install flask

#inicializacao
app = Flask(__name__)

# rotas
@app.route('/')
def ola_mundo():
    return 'Olá Mundo'

#execucao
app.run(debug=True)




