import requests
import json

link = "https://noble-might-399221-default-rtdb.firebaseio.com/"

dados = {'email': 'adna@gmail.com', 'senha': 5678}
requisicao = requests.post(f'{link}/login/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)