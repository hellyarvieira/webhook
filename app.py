from flask import request, jsonify

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    verify_token = 'meu_token_secreto_123'  # Este é o token que você inventa e define
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')

    if token == verify_token:
        return challenge
    return 'Token inválido', 403
