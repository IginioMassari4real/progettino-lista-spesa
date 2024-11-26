from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app = Flask(__name__)

lista_spesa = []

@app.route('/')
def index():

    return render_template('index.html', lista=lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():

    elemento = request.form.get('elemento')
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('index'))

@app.route('/rimuovi/<int:indice>')
def rimuovi(indice):

    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('index'))

@app.route('/svuota')
def svuota():

    lista_spesa.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)