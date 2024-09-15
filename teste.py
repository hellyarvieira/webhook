import requests

# URL do seu webhook
url = 'https://web-production-64a7.up.railway.app/webhook'

# Parâmetros para testar o token de validação
params = {
    'hub.verify_token': 'meu_token_secreto_123',  # Token que você definiu
    'hub.challenge': '12345',  # Valor de teste para o desafio
    'hub.mode': 'subscribe'
}

# Enviando a requisição GET
response = requests.get(url, params=params)

# Exibindo a resposta
print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
