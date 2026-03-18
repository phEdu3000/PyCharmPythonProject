real=float(input('Quantos reais você quer converter ? R$'))
dolar= real/5.20
euro= real/6.00
kwanza=real/0.0057


opcao= int(input('Escolha a moeda : \n1-Dolar\n2-Euro\n3-Kwanza\n'))
match opcao:
    case 1:
    print('Sua conversão de R${:.2f} em dolar deu ${:.2f}'.format(real,dolar))

    case 2:
        print('Sua conversão de R${:.2f} em euro deu €{:.2f}'.format(real,euro))

    case 3:
        print('Sua conversão de R${:.2f} em kwanza deu {:.2f}Kz'.format(real,kwanza))


    case _:
print('opção inválida')