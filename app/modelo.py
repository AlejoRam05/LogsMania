from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy() #db se comvierte en un objeto que nos permite interactuar con la base de datos

class Logs(db.Model): #db.Model indica que 'Usuario' es un modelo de daros gestionado por SQLAlchemy
    
    '''Los atributos de clases definen (que)'''
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable = True)
    ejecucion = db.Column(db.String(255), nullable = False)
    level_severidad = db.Column(db.String(50), nullable = False)
    '''Los atributos de instancia contienen los datos expecificos que almacenan'''
    def __init__(self, fecha: datetime, ejecucion: str, level_severidad: str):
        self.fecha = fecha
        self.ejecucion = ejecucion
        self.level_severidad = level_severidad
