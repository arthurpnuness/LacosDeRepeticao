'''Foi feita uma pesquisa entre os 10 habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um algoritmo que informe:  

1 - A média de salário do grupo;
2 - Maior e menor idade do grupo;
3 - Quantidade de mulheres com salário até R$10000,00.
'''

def pesquisa():  
    generos = []
    idades = []
    salarios = []
    contador = 0
    mulheres10000 = 0  # Alterado para um contador simples

    # Coleta de dados de 10 habitantes
    while contador < 10:
        idade = int(input('Quantos anos você tem? '))
        idades.append(idade)
        genero = input('Qual gênero você se identifica (M / F): ').strip().upper()  # Para garantir a comparação
        generos.append(genero)
        salario = float(input('Qual o seu salário? '))
        salarios.append(salario)
        contador += 1

    # Cálculo da média de salários
    mediaSalarios = sum(salarios) / 10  # Usando o comprimento da lista de salários
    maiorIdade = max(idades)
    menorIdade = min(idades)

    # Contagem de mulheres com salário até R$10.000,00
    for i in range(len(generos)):
        if generos[i] == 'F' and salarios[i] <= 10000:  # Corrigido para <= e uso do índice
            mulheres10000 += 1  # Incrementa o contador

    # Impressão dos resultados
    print(f'A média salarial do grupo de habitantes é de R${mediaSalarios:.2f} \nA maior idade do grupo é {maiorIdade} \nA menor idade do grupo é {menorIdade} \nA quantidade de mulheres com salário até R$10.000,00 é de {mulheres10000}')

# Chama a função para executar a pesquisa
pesquisa()
