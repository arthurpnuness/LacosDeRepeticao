'''Uma empresa de pesquisa deseja saber a média de altura e idade das pessoas, para isso, crie um algoritmo que apresente o seguinte menu:
1. Cadastrar pessoa
Neste item, deve-se ler a altura e idade da pessoa.
2. Mostrar média parcial de altura e idade
3. Sair

Após o usuário digitar 3, deve-se mostrar a média de altura
e idade oficial.'''

contador = 0
somaAltura = 0
somaIdade = 0
opcao = 0

while opcao != 3:
    print('1 - Cadastrar Pessoa')
    print('2 - Mostrar média parcial de altura e idade')
    print('3 - Sair')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        nome = input('Digite o nome do cadastrado(a): ')
        altura = float(input('Digite a altura: '))
        idade = int(input('Digite a idade: '))
        somaAltura = somaAltura + altura
        somaIdade = somaIdade + idade
        contador += 1
    elif opcao == 2:
        mediaAltura = somaAltura / contador
        mediaIdade = somaIdade / contador
        print(f'A media de altura da empresa é de {mediaAltura} e a media de idade é de {mediaIdade}')
    elif opcao == 3:    
        mediaAltura = somaAltura / contador
        mediaIdade = somaIdade / contador
        print(f'A media de altura da empresa é de {mediaAltura} e a media de idade é de {mediaIdade}')
    else:
        print('Opção Invalida')
    
        

    



