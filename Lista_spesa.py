from flask import Flask, render_template, request, redirect  # Importa Flask e strumenti utili per gestire richieste e template
from flask_sqlalchemy import SQLAlchemy  # Importa SQLAlchemy per gestire il database
from models import db, ListaSpesa  # Importa la configurazione del database e il modello 'ListaSpesa' dal file models.py

app = Flask(__name__)  # Crea un'applicazione Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'  # Configura il database come SQLite, salvato in 'lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disattiva il monitoraggio delle modifiche per evitare overhead

db.init_app(app)  # Inizializza l'oggetto 'db' con l'app Flask

# Creazione del database e delle tabelle, se non esistono, durante l'avvio dell'app
with app.app_context():
    db.create_all()

# Route principale: mostra tutti gli elementi nella lista della spesa
@app.route('/')
def home():
    elementi = ListaSpesa.query.all()
    return render_template('index.html', elementi=elementi)  

# Route per aggiungere un nuovo elemento alla lista
@app.route('/aggiungi', methods=['POST'])  
def aggiungi():
    nuovo_elemento = request.form['elemento']  
    elemento = ListaSpesa(elemento=nuovo_elemento)  
    db.session.add(elemento)  
    db.session.commit() 
    return redirect('/')  

# Route per rimuovere un elemento specifico dalla lista, identificato dall'ID
@app.route('/rimuovi/<int:id>', methods=['POST'])  
def rimuovi(id):
    elemento = ListaSpesa.query.get_or_404(id)  
    db.session.delete(elemento)  
    db.session.commit()  
    return redirect('/') 

# Route per svuotare completamente la lista
@app.route('/svuota', methods=['POST'])  
def svuota():
    ListaSpesa.query.delete()  
    db.session.commit()  
    return redirect('/') 

# Avvio dell'applicazione in modalità di debug
if __name__ == '__main__':
    app.run(debug=True)  
