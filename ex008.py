'''Em um prédio com 10 moradores há três elevadores denominados A, B e C. Para otimizar o sistema de controle dos elevadores, desenvolva um programa em que cada morador informa qual o elevador que utiliza com mais frequência (A, B ou C). 
O algoritmo deve contabilizar o total de pessoas que usa cada um dos elevadores e mostrar estes totais e suas respectivas porcentagens no final.  
'''

def controleElevadores():
    # Inicializa contadores para cada elevador
    contagemA = 0  # Contador para o elevador A
    contagemB = 0  # Contador para o elevador B
    contagemC = 0  # Contador para o elevador C
    totalMoradores = 10  # Número total de moradores

    # Coleta de dados dos moradores
    for i in range(totalMoradores):  # Loop para 10 moradores
        # Solicita ao morador qual elevador utiliza com mais frequência
        elevador = input(f'Morador {i + 1}, qual elevador você utiliza com mais frequência (A, B ou C)? ').strip().upper()

        # Contabiliza a escolha do elevador
        if elevador == 'A':  # Se o elevador escolhido for A
            contagemA += 1  # Incrementa o contador do elevador A
        elif elevador == 'B':  # Se o elevador escolhido for B
            contagemB += 1  # Incrementa o contador do elevador B
        elif elevador == 'C':  # Se o elevador escolhido for C
            contagemC += 1  # Incrementa o contador do elevador C
        else:  # Se a entrada for inválida
            print('Elevador inválido. Por favor, escolha A, B ou C.')  # Informa ao usuário sobre a entrada inválida
            # Decrementa o contador se a entrada for inválida para não contar como um morador
            totalMoradores -= 1  # Reduz o total de moradores válidos

    # Cálculo das porcentagens (sem divisão por zero)
    if totalMoradores > 0:  # Verifica se há moradores válidos
        porcentagemA = (contagemA / totalMoradores) * 100  # Porcentagem do elevador A
        porcentagemB = (contagemB / totalMoradores) * 100  # Porcentagem do elevador B
        porcentagemC = (contagemC / totalMoradores) * 100  # Porcentagem do elevador C
    else:
        porcentagemA = 0  # Define como 0 se não houver moradores válidos
        porcentagemB = 0
        porcentagemC = 0

    # Impressão dos resultados
    print(f'\nTotal de pessoas que utilizam o elevador A: {contagemA} ({porcentagemA:.2f}%)')  # Mostra total e porcentagem do elevador A
    print(f'Total de pessoas que utilizam o elevador B: {contagemB} ({porcentagemB:.2f}%)')  # Mostra total e porcentagem do elevador B
    print(f'Total de pessoas que utilizam o elevador C: {contagemC} ({porcentagemC:.2f}%)')  # Mostra total e porcentagem do elevador C

# Chama a função para executar o programa
controleElevadores()

