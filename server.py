from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# Garantir que existe arquivo de dados
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({"convocacoes": [], "pads": [], "ipms": []}, f)


def salvar_dados(dados):
    with open(DATA_FILE, "w") as f:
        json.dump(dados, f, indent=4)


def carregar_dados():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


@app.route("/update", methods=["POST"])
def update():
    dados = carregar_dados()
    body = request.json

    tipo = body.get("tipo")

    if tipo == "convocacao":
        dados["convocacoes"].append(body)

    elif tipo == "pad":
        dados["pads"].append(body)

    elif tipo == "ipm":
        dados["ipms"].append(body)

    salvar_dados(dados)
    return jsonify({"status": "ok"}), 200


@app.route("/dados", methods=["GET"])
def dados():
    return jsonify(carregar_dados())


@app.route("/")
def home():
    return "API da Corregedoria funcionando!"


if __name__ == "__main__":
    app.run()
