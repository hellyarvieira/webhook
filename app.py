from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    verify_token = 'meu_token_secreto_123'  # Token que você define
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if token == verify_token:
        return challenge
    return 'Token inválido', 403

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Recebido: {data}")
    return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
