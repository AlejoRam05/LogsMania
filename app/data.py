import random
from datetime import datetime
from app.modelo import Logs, db

class Data:
    def generar_logs(self):
        info = ["DEBUG", "INFO", "WARNING", "ERROR"]
        logs = []
        for i in range(1, 11):
            servicio = f"Servicio {i}"
            level_severidad = random.choice(info)
            log = {
                "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "ejecucion": servicio,
                "level_severidad": level_severidad
            }
            logs.append(log)
        return logs
    
    def registrar_logs(self):
        logs = self.generar_logs()
        for log in logs:
            nuevo_log = Logs(
                fecha=datetime.strptime(log['fecha'], "%Y-%m-%d %H:%M:%S"),
                ejecucion=log['ejecucion'],
                level_severidad=log['level_severidad']
            )
            db.session.add(nuevo_log)
        db.session.commit()
