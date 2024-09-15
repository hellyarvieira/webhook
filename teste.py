import requests

url = 'https://web-production-64a7.up.railway.app/webhook'
data = {"chave": "valor"}

response = requests.post(url, json=data)

print(f'Status Code: {response.status_code}')
print(f'Response: {response.json()}')
