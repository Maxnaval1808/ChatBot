from requests import get

requisicao = get('https://economia.awesomeapi.com.br/json/last/USD-BRL')

cotacao = requisicao.json()

nome = cotacao['USDBRL']['name']
data = cotacao['USDBRL']['create_date']
valor = cotacao['USDBRL']['bid']

mensagem = f"Cotação do {nome} em {data} é R$ {valor}"
print(mensagem)