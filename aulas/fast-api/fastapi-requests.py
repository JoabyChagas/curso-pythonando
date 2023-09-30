import requests

# O request com get e solicitado através das url
responseGet = requests.get('http://127.0.0.1:8000/usuario/1')

# o request com post você tem que passar um 'params=' para receber a response
responsePost = requests.post('http://127.0.0.1:8000/usuario/', params={'id': 1})

print(responsePost.json())