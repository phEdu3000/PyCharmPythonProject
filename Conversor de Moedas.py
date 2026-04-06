import requests

try:
    real = float(input('Quantos reais você quer converter? R$ '))
except ValueError:
    print("❌ Digite um número válido!")
    exit()

# Buscamos USD-BRL (Dólar/Real), EUR-BRL (Euro/Real) e USD-AOA (Dólar/Kwanza)
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,USD-AOA'

try:
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()


        dolar_real = float(dados['USDBRL']['bid'])
        euro_real = float(dados['EURBRL']['bid'])
        dolar_kwanza = float(dados['USDAOA']['bid'])
        kwanza_por_real = dolar_kwanza / dolar_real

        print('\nEscolha a moeda:')
        print('1 - Dólar')
        print('2 - Euro')
        print('3 - Kwanza')

        opcao = input('Opção: ')

        match opcao:
            case '1':
                convertido = real / dolar_real
                print(f'R$ {real:.2f} -> US$ {convertido:.2f}')
            case '2':
                convertido = real / euro_real
                print(f'R$ {real:.2f} -> € {convertido:.2f}')
            case '3':
                convertido = real * kwanza_por_real
                print(f'R$ {real:.2f} -> Kz {convertido:.2f}')
            case _:
                print('❌ Opção inválida')
    else:
        print(f"❌ Erro na API: {resposta.status_code}")

except Exception as e:
    print(f"❌ Erro inesperado: {e}")