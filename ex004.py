'''Faça um programa que receba a idade e o peso de 7 pessoas, calcule e mostre:
A média das idades das 7 pessoas;
Quantidade de pessoas maiores de idade.
Porcentagem de pessoas com idade entre 10 e 30 anos
'''

def calculoPessoas():
    # Lista para armazenar as idades das 7 pessoas
    pessoas = []
    
    # Contador para rastrear quantas pessoas já foram cadastradas
    contador = 0
    
    # Lista para armazenar as idades das pessoas maiores de idade (18 anos ou mais)
    maiores = []
    
    # Lista para armazenar as idades das pessoas com idade entre 10 e 30 anos
    pessoas1030 = []

    # Laço que continua até que 7 idades tenham sido coletadas
    while contador < 7:
        # Solicita a idade de uma pessoa e a armazena como um número inteiro
        pessoa = int(input('Digita a idade de uma pessoa: '))
        
        # Adiciona a idade da pessoa à lista de pessoas
        pessoas.append(pessoa)
        
        # Incrementa o contador
        contador += 1

    # Calcula a média das idades dividindo a soma das idades pelo número total de pessoas (7)
    mediaIdade = sum(pessoas) / 7

    # Laço que verifica quantas pessoas são maiores de idade
    for i in pessoas:
        if i >= 18:  # Se a idade for 18 ou mais
            maiores.append(i)  # Adiciona a idade à lista de maiores de idade

    # Laço que verifica quantas pessoas estão na faixa etária de 10 a 30 anos
    for i in pessoas:
        if 10 <= i <= 30:  # Se a idade estiver entre 10 e 30 anos
            pessoas1030.append(i)  # Adiciona a idade à lista de pessoas entre 10 e 30 anos

    # Calcula a quantidade de pessoas maiores de idade
    qtdMaiores = len(maiores)
    
    # Calcula a quantidade de pessoas com idade entre 10 e 30 anos
    qtdPessoasIntervalo = len(pessoas1030)
    
    # Calcula a porcentagem de pessoas entre 10 e 30 anos em relação ao total (7)
    porcentagem = (qtdPessoasIntervalo / 7) * 100

    # Exibe os resultados: média das idades, quantidade de maiores de idade e porcentagem na faixa etária
    print(f'A média de idade das pessoas é {mediaIdade:.0f} anos \nA quantidade de pessoas maiores de idade é de {qtdMaiores} \nA porcentagem de pessoas com idade entre 10 a 30 anos é de {porcentagem:.2f} %')

# Chama a função para executar o cálculo
calculoPessoas()
