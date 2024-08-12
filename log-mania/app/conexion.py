from flask import Flask
from app.modelo import db

def create_app():
    app = Flask(__name__)
    # Configuración de la base de datos
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///logs.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Crea todas las tablas antes de iniciar la aplicación
        
    return app
