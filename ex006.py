'''Faça um programa que receba a idade de dez pessoas e que calcule e mostre a quantidade de pessoas com idade maior ou igual a 18 anos.'''

# Função que realiza a contagem de pessoas com 18 anos ou mais
def pessoas():
    
    pessoas = []  # Lista para armazenar as idades das pessoas
    contador = 0  # Contador para controlar o número de entradas
    pessoas18 = 0  # Contador para pessoas com 18 anos ou mais
    
    # Loop para coletar a idade de 5 pessoas
    while contador < 5:
        pessoa = int(input('Digite quantos anos você tem: '))  # Solicita a idade e converte para inteiro
        pessoas.append(pessoa)  # Adiciona a idade à lista de pessoas
        contador += 1  # Incrementa o contador

    # Loop para contar quantas pessoas têm 18 anos ou mais
    for i in range(len(pessoas)):
        if pessoas[i] >= 18:  # Verifica se a idade é maior ou igual a 18
            pessoas18 += 1  # Incrementa o contador de pessoas com 18 anos ou mais

    # Impressão do resultado
    print(f'A quantidade de pessoas com idade maior ou igual a 18 anos é de: {pessoas18} pessoas')

# Chama a função para executar o programa
pessoas()
