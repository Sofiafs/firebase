'''import requests
import json

link = "https://noble-might-399221-default-rtdb.firebaseio.com/"

dados = {'email': 'adna@gmail.com', 'senha': 5678}
requisicao = requests.post(f'{link}/login/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)


cred = credentials.Certificate('C:/Users/sofia/Downloads/noble-might-399221-firebase-adminsdk-blpau-93e21293d0.json') 
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://noble-might-399221-default-rtdb.firebaseio.com/'  
})'''
