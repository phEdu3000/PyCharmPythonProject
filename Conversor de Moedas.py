import requests

real=float(input('Quantos reais você quer converter ? R$'))

url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,AOA-BR'
dados = requests.get(url).json()



dolar = float(dados['USDBRL']['bid'])
euro = float(dados['EURBRL']['bid'])
kwanza = float(dados['AOABRL']['bid'])

print('\nEscolha a moeda:')
print('1 - Dólar')
print('2 - Euro')
print('3 - Kwanza')
opcao = int(input('Opção:'))

match opcao:
    case 1:
        convertido = real / dolar
        print(f'Sua conversão de R${real:.2f} em dólar deu ${convertido:.2f}')
    case 2:
        convertido = real / euro
        print(f'Sua conversão de R${real:.2f} em euro deu €{convertido:.2f}')

    case 3:
        convertido = real / kwanza
        print(f'Sua conversão de R${real:.2f} em kwanza deu {convertido:.2f} Kz')

    case _:
        print('opção inválida')

