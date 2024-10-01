'''Foi feita uma pesquisa entre os 10 habitantes de uma região. Foram coletados os dados de idade, sexo (M/F) e salário. Faça um algoritmo que informe:  

1 - A média de salário do grupo;
2 - Maior e menor idade do grupo;
3 - Quantidade de mulheres com salário até R$10000,00.
'''

# Função que realiza a pesquisa com 10 habitantes
def pesquisa():  
    # Inicializa listas para armazenar os dados coletados
    generos = []   # Lista para armazenar os gêneros
    idades = []    # Lista para armazenar as idades
    salarios = []  # Lista para armazenar os salários
    contador = 0   # Contador para controlar o número de habitantes
    mulheres10000 = 0  # Contador para mulheres com salário até R$10.000,00

    # Coleta de dados de 10 habitantes
    while contador < 10:
        idade = int(input('Quantos anos você tem? '))  # Solicita a idade e converte para inteiro
        idades.append(idade)  # Adiciona a idade à lista de idades
        genero = input('Qual gênero você se identifica (M / F): ').strip().upper()  # Solicita o gênero e normaliza
        generos.append(genero)  # Adiciona o gênero à lista de gêneros
        salario = float(input('Qual o seu salário? '))  # Solicita o salário e converte para float
        salarios.append(salario)  # Adiciona o salário à lista de salários
        contador += 1  # Incrementa o contador

    # Cálculo da média de salários
    mediaSalarios = sum(salarios) / 10  # Calcula a média de salários dividindo a soma pelo número de habitantes
    maiorIdade = max(idades)  # Encontra a maior idade
    menorIdade = min(idades)  # Encontra a menor idade

    # Contagem de mulheres com salário até R$10.000,00
    for i in range(len(generos)):  # Itera sobre os índices das listas
        if generos[i] == 'F' and salarios[i] <= 10000:  # Verifica se o gênero é feminino e se o salário é <= 10.000
            mulheres10000 += 1  # Incrementa o contador de mulheres com salário até 10.000

    # Impressão dos resultados
    print(f'A média salarial do grupo de habitantes é de R${mediaSalarios:.2f} \nA maior idade do grupo é {maiorIdade} \nA menor idade do grupo é {menorIdade} \nA quantidade de mulheres com salário até R$10.000,00 é de {mulheres10000}')

# Chama a função para executar a pesquisa
pesquisa()
