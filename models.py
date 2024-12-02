from flask_sqlalchemy import SQLAlchemy  # Importa SQLAlchemy per gestire il database in modo ORM

db = SQLAlchemy()  # Crea un'istanza dell'oggetto SQLAlchemy, che verrà utilizzata per interagire con il database

# Definizione del modello per la tabella 'ListaSpesa'
class ListaSpesa(db.Model): 
    id = db.Column(db.Integer, primary_key=True)  
    elemento = db.Column(db.String(100), nullable=False)  
