from flask import Flask, render_template, request, redirect, url_for
from etl import extraer_datos_api
from db import guardar_datos_postgres, obtener_ultimo_registro, obtener_todos_los_registros 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        datos = extraer_datos_api()
        guardar_datos_postgres(datos)
        return redirect(url_for("index"))

    registro = obtener_ultimo_registro()
    return render_template("index.html", registro=registro)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/historial")
def historial():
    registros = obtener_todos_los_registros()
    return render_template("historial.html", registros=registros)

