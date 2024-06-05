#3. Faça um código Python que consuma a API de cotações de moeda.

import requests
import pandas
import pandas as pd
from tabulate import tabulate

api_key = "https://api.hgbrasil.com/finance?format=json-cors&key=d85a29c5"

request = requests.get(api_key)

if request.status_code == 200:
    dados = request.json()

  
else:
    print('Falhou')

#4. crie uma tabela chamada “moedas”. A tabela deverá ter as seguintes colunas “Data”,
#“Dolar” e “Euro” para armazenar a cotação das respectivas moedas (preço de compra), frente ao Real.

mydata = [
    ['Dolar', 'Bitcoin','Euro'],
      [(dados['results']['currencies']['USD']['buy']),
       (dados['results']['currencies']['BTC']['buy']),
       (dados['results']['currencies']['EUR']['buy']) ]
]
 
print(tabulate(mydata))



