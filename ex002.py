'''Faça um algoritmo que simule uma conta bancária:
1 - Sacar
2 - Depositar
3 - Saldo
4 - Sair

No início o algoritmo deve solicitar o saldo atual.
'''

opcao = 0

saldo = float(input('Digite seu salto atual: '))

while opcao != 4:
    print('1 - Sacar')
    print('2 - Depositar')
    print('3 - Saldo')
    print('4 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        saldo = saldo
        saque = float(input('Digite o valor do seu saque: '))
        if saque <= saldo and saque > 0:
            saldoTotal = saque - saldo
            print(f'Agora teu saldo é de {saldoTotal}')
        else:
            print('Voce nao pode sacar um valor maior do que seu saldo')
    elif opcao == 2:
        deposito = float(input('Digite o valor do desposito: '))
        saldo = saldo + deposito
        print(f'Agora seu saldo total é de R${saldo}')
    elif opcao == 3:
        print(f'O seu saldo atual é de {saldo}')
    elif opcao == 4:
        print('Voce saiu da aplicação. Obrigado por usar!')
    else:
        print('Opção invalida')