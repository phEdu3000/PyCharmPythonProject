m=float (input('Digite seu valor em metros para obter os calculos'));
cm = m*100
mm = m*1000
print('a medida de {}m corresponde a {:.2f}cm e {:.2f}mm' .format(m,cm,mm));
#*////////////////////////////////////////////////////////////////////////////////////*
km= m/1000
hec= m/100
dec= m/10
unidade=""
resultado=0

while True:
        opcao = input('Escolha a conversão de metros para: '
             '\n[1]KM'
             '\n[2]Hec'
             '\n[3]Dec');

        if opcao == '1':
                resultado = km;
                unidade ="km"
                print('{:.2f}km' .format(resultado));
        elif opcao == '2' :
                 resultado = hec;
                 unidade = "hec";
                 print('{:.2f}hec'.format(hec));
        elif opcao == '3' :
                  resultado = dec;
                  unidade ="dec";
                  print('{:.2f}dec'.format(dec));
        else :print ('Opção inválida');
        break
print('voce escolheu opção {} '.format(opcao));
print('Sua conversao foi de {}{}'.format(resultado,unidade));