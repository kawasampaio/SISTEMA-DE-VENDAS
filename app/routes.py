from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Para permitir comunicação com o frontend React

# Configuração do MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['vendas_db']
vendas_collection = db['vendas']

@app.route('/add-venda', methods=['POST'])
def add_venda():
    data = request.json
    nova_venda = {
        "variacao": data["variacao"],
        "quantidade": data["quantidade"],
        "preco_unitario": data["preco_unitario"],
        "data": datetime.now()
    }
    vendas_collection.insert_one(nova_venda)
    return jsonify({"message": "Venda adicionada com sucesso!"}), 201

@app.route('/get-vendas', methods=['GET'])
def get_vendas():
    start_date = request.args.get('start')
    end_date = request.args.get('end')

    # Converter strings de datas em formato datetime
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Filtrar vendas por data
    vendas = list(vendas_collection.find({
        "data": {"$gte": start_date, "$lte": end_date}
    }))

    # Converter documentos MongoDB para JSON serializável
    for venda in vendas:
        venda["_id"] = str(venda["_id"])

    return jsonify(vendas)

