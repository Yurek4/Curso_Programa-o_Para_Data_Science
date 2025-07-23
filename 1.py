import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
#GET buscar dados
#POST Criar dados 
#PUT/PATCH Atualizar dados
#DELETE remover dados
resposta = requests.get(url) #Ele vai bater la na API 

print(resposta) #Vamos visualizar a resposta

if resposta.status_code == 200:
    dados = resposta.json() # Transformando os dados da API em formato JSON
    #print(json.dumps(dados[10], indent = 4))
    print(type(dados))
    print(json.dumps(dados[0], indent = 4)) #Estou usando os comando json.dumps para deixar uma visualização tipo json
else:
    print(f"Erro:{resposta.status_code}")


primeiro_post = dados[10]
usuario_id = primeiro_post["userId"]
post_id = primeiro_post["id"]
title = primeiro_post["title"]

print(usuario_id)
print(post_id)
print(title)
print("--------------------------------")
print("---------------Estou fazendo um loop para exibir todos os ids (do indice 0 ao 5)-----------------")


lista_ids = [] # CRIEI UMA LISTA VAZIA PARA ARMAZENAR OS MEUS IDS
lista_titulos = []
for post in dados[:5]:
    #print(post)
    user_ids = post["id"]
    titulos = post["title"]
    print(f"userId: {user_ids}")
    lista_ids.append(user_ids)
    lista_titulos.append(titulos)

print("----------------------------------------")
print(user_ids)
print("-------------Print da minha lista de ids-------------------")
print(lista_ids)
print(lista_titulos)
