import requests

# URL do seu webhook
url = 'https://web-production-64a7.up.railway.app/webhook'

# Parâmetros de validação
params = {
    'hub.verify_token': 'meu_token_secreto_123',  # Token definido por você
    'hub.challenge': '12345',  # Um desafio fictício para o teste
    'hub.mode': 'subscribe'
}

# Enviando a requisição GET
response = requests.get(url, params=params)

# Exibindo a resposta
print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
