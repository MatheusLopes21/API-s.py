#Modifique o código anterior para que, usando uma estrutura de repetição, consulte 5 CEPs sequenciais.
#Suponha que o CEP da sua casa seja 30140-071, o código Python deverá enviar 5 requisições com os seguintes CEPs:
#30140071, 30140072, 30140073, 30140074 e 30140075

import requests

url = 'https://viacep.com.br/ws/'
base_cep = 30140071 
formato = '/json/' 

for i in range(5):
    cep = str(base_cep + i)  # Converte o número do CEP para string
    r = requests.get(url + cep + formato)
    if r.status_code == 200:
        print()
        print('JSON para o CEP {cep}:')
        print(r.json())
        print()
    else:
        print(f'Não houve sucesso na requisição para o CEP {cep}.')







