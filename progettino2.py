from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ListaSpesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)  
    elemento = db.Column(db.String(100), nullable=False) 

with app.app_context():
    db.create_all()  

@app.route('/')
def home():
    elementi = ListaSpesa.query.all()  
    return render_template('index.html', elementi=elementi)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    nuovo_elemento = request.form['elemento'] 
    elemento = ListaSpesa(elemento=nuovo_elemento)
    db.session.add(elemento)  
    db.session.commit() 
    return redirect('/')

@app.route('/rimuovi/<int:id>', methods=['POST'])
def rimuovi(id):
    elemento = ListaSpesa.query.get_or_404(id)  
    db.session.delete(elemento)  
    db.session.commit()  
    return redirect('/')

@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete() 
    db.session.commit() 
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
