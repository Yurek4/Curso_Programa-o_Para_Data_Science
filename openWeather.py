##OpenWeather

import os
import requests 
import pandas as pd 

API_KEY = "c1d9c0352f82661b7500d316c06c28ae"
cidade = "campinas"
link = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&lang=pt_br"
link_2 = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_KEY}"


resposta = requests.get(link)

print(link)
print(link_2)
print(resposta)

if resposta.status_code == 200:
  total_registros = resposta.json()
  print(total_registros)
  #total_de_paginas = int(total_registros['total']/total_registros["per_page"])
  #registros_por_pagina = total_registros["per_page"]
  #print(f"Total de registropor pagina{registros_por_pagina} e total de paginas {total_de_paginas}")
#else:
  #print("deu ruim")
