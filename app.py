import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint para verificação do webhook (GET)
@app.route('/webhook', methods=['GET'])
def verify_webhook():
    verify_token = 'meu_token_secreto_123'  # Token definido por você
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if token == verify_token:
        return challenge
    return 'Token inválido', 403

# Endpoint para receber dados do webhook (POST)
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Recebido: {data}")
    return jsonify({"status": "received"}), 200

# Iniciar o servidor Flask na porta definida pelo Railway
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usa a porta atribuída pelo Railway
    app.run(host='0.0.0.0', port=port)
