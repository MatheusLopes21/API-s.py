#Modifique o primeiro código de tal forma que o endereço " https://viacep.com.br/abc/" tente ser acessado. Exiba o código de retorno e o texto.

import requests

url = 'https://viacep.com.br/abc/'
r = requests.get(url)

print('Código de retorno:', r.status_code)
print('Texto:', r.text)