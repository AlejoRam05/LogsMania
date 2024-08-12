from flask import render_template, jsonify
from app.conexion import create_app
from app.data import Data
from app.modelo import Logs

app = create_app()
data_service = Data()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logs", methods=["POST", "GET"])
def logs():
    logs = data_service.generar_logs()
    return jsonify(logs)  # Devolver JSON de forma correcta

@app.route("/registrarlogs", methods=["POST", "GET"])
def registrar():
    with app.app_context():  # Aseguramos que estamos en el contexto de la aplicación
        data_service.registrar_logs()
        registros = Logs.query.all()
    return render_template("index.html", logs=registros)


if __name__ == "__main__":
    app.run(debug=True)
