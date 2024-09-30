'''Faça um algoritmo que simule uma conta bancária:
1 - Sacar
2 - Depositar
3 - Saldo
4 - Sair

No início o algoritmo deve solicitar o saldo atual.
'''

# Inicialização da variável "opcao" com valor 0 para controlar o menu
opcao = 0

# Solicita ao usuário o saldo inicial da conta bancária
saldo = float(input('Digite seu saldo atual: '))

# Laço principal que continua enquanto o usuário não escolher a opção "Sair" (opção 4)
while opcao != 4:
    # Exibe o menu de opções para o usuário
    print('1 - Sacar')
    print('2 - Depositar')
    print('3 - Saldo')
    print('4 - Sair')
    
    # Recebe a opção escolhida pelo usuário
    opcao = int(input('Digite a opção desejada: '))

    # Se a opção escolhida for 1, o usuário deseja realizar um saque
    if opcao == 1:
        saque = float(input('Digite o valor do seu saque: '))
        
        # Verifica se o valor do saque é menor ou igual ao saldo disponível e se é positivo
        if saque <= saldo and saque > 0:
            saldo = saldo - saque  # Atualiza o saldo após o saque
            print(f'Agora seu saldo é de R${saldo:.2f}')
        else:
            # Caso o valor do saque seja maior que o saldo ou inválido, exibe uma mensagem de erro
            print('Você não pode sacar um valor maior do que seu saldo ou negativo.')
    
    # Se a opção escolhida for 2, o usuário deseja realizar um depósito
    elif opcao == 2:
        deposito = float(input('Digite o valor do depósito: '))
        
        # Atualiza o saldo somando o valor do depósito
        saldo = saldo + deposito
        print(f'Agora seu saldo total é de R${saldo:.2f}')
    
    # Se a opção escolhida for 3, o usuário deseja ver o saldo atual
    elif opcao == 3:
        # Exibe o saldo atual com duas casas decimais
        print(f'O seu saldo atual é de R${saldo:.2f}')
    
    # Se a opção escolhida for 4, o usuário deseja sair do programa
    elif opcao == 4:
        print('Você saiu da aplicação. Obrigado por usar!')
    
    # Caso o usuário digite uma opção inválida
    else:
        print('Opção inválida')
