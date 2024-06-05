#Modifique o código para que a consulta seja feita com um endereço (nome de rua), ao invés do CEP.

import requests

estado = 'MG'
cidade = 'Belo Horizonte'
logradouro = 'Rua dos Aimores'
formato = '/json/'


url = f'https://viacep.com.br/ws/{estado}/{cidade}/{logradouro}{formato}'


r = requests.get(url)
if r.status_code == 200:
    enderecos = r.json()
    print()
    print(f'Endereços encontrados para {logradouro} em {cidade}/{estado}:')
    for endereco in enderecos:
        print(endereco)
        print()
else:
    print('Não houve sucesso na requisição.')


