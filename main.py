from flask import Flask, url_for, render_template

# Inicialização
app = Flask(__name__)

# Rotas
@app.route('/')
def ola_mundo():
    # Lista de dicionarios
    titulo = "Gestão de Usuários"
    usuario = [
        {'nome': 'João', 'membro_ativo': True},
        {'nome': 'Maria', 'membro_ativo': False},
        {'nome': 'Pedro', 'membro_ativo': False}
    ]
    return render_template('index.html', titulo=titulo, usuario=usuario)

    # f"<a href='{ url_for('pagina_sobre') }'>Sobre</a>"

@app.route("/sobre")
def pagina_sobre():
    return """
    <h1>Sobre</h1>
    <p>Esta é uma página sobre o projeto.</p>"""


# Execução
app.run(debug=True)