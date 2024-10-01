'''Faça um programa que receba dez números e usando laços de repetição calcule e mostre a quantidade de números entre 30 e 90. '''

def calculoDeQuantidade():

    numeros = []  # Lista para armazenar os números recebidos
    contador = 0  # Contador para controlar o número de entradas
    numeros3090 = 0  # Contador para números entre 30 e 90

    while contador < 10:  # Loop para receber 10 números
        num = int(input('Digite um número: '))  # Solicita um número ao usuário
        numeros.append(num)  # Adiciona o número à lista
        contador += 1  # Incrementa o contador

    # Loop para contar quantos números estão entre 30 e 90
    for i in range(len(numeros)):
        # A condição está incorreta; precisa ser separada:
        if 30 <= numeros[i] <= 90:  # Verifica se o número está entre 30 e 90
            numeros3090 += 1  # Incrementa o contador de números entre 30 e 90

    # Impressão do resultado
    print(f'A quantidade de números entre 30 e 90 é: {numeros3090} números')

# Chama a função para executar o programa
calculoDeQuantidade()
