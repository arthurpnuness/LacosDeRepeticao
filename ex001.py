'''Uma empresa de pesquisa deseja saber a média de altura e idade das pessoas, para isso, crie um algoritmo que apresente o seguinte menu:
1. Cadastrar pessoa
Neste item, deve-se ler a altura e idade da pessoa.
2. Mostrar média parcial de altura e idade
3. Sair

Após o usuário digitar 3, deve-se mostrar a média de altura
e idade oficial.'''

# Inicialização de variáveis
contador = 0         # Contador para controlar o número de pessoas cadastradas
somaAltura = 0       # Variável para armazenar a soma de todas as alturas
somaIdade = 0        # Variável para armazenar a soma de todas as idades
opcao = 0            # Variável para armazenar a opção do menu escolhida pelo usuário

# Laço principal que continua executando enquanto a opção escolhida for diferente de 3 (sair)
while opcao != 3:
    # Exibe o menu com as opções para o usuário
    print('1 - Cadastrar Pessoa')
    print('2 - Mostrar média parcial de altura e idade')
    print('3 - Sair')
    
    # Lê a opção digitada pelo usuário
    opcao = int(input('Digite a opção desejada: '))

    # Opção 1: Cadastrar uma nova pessoa
    if opcao == 1:
        # Coleta o nome, altura e idade da pessoa
        nome = input('Digite o nome do cadastrado(a): ')
        altura = float(input('Digite a altura: '))
        idade = int(input('Digite a idade: '))
        
        # Atualiza a soma total de altura e idade com os valores da pessoa cadastrada
        somaAltura = somaAltura + altura
        somaIdade = somaIdade + idade
        
        # Incrementa o contador de pessoas cadastradas
        contador += 1
    
    # Opção 2: Mostrar a média parcial de altura e idade
    elif opcao == 2:
        # Verifica se há pessoas cadastradas para evitar divisão por zero
        if contador > 0:
            # Calcula a média de altura e idade dividindo pela quantidade de pessoas cadastradas
            mediaAltura = somaAltura / contador
            mediaIdade = somaIdade / contador
            
            # Exibe as médias parciais
            print(f'A média de altura da empresa é de {mediaAltura:.2f} e a média de idade é de {mediaIdade:.2f}')
        else:
            print('Nenhuma pessoa cadastrada ainda.')
    
    # Opção 3: Sair e mostrar a média final
    elif opcao == 3:
        # Verifica se há pessoas cadastradas antes de calcular a média final
        if contador > 0:
            # Calcula a média de altura e idade final
            mediaAltura = somaAltura / contador
            mediaIdade = somaIdade / contador
            
            # Exibe as médias finais
            print(f'A média de altura da empresa é de {mediaAltura:.2f} e a média de idade é de {mediaIdade:.2f}')
        else:
            print('Nenhuma pessoa cadastrada.')
    
    # Caso o usuário digite uma opção inválida
    else:
        print('Opção inválida')


    
        

    



