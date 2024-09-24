'''Fazer um algoritmo que leia diversos números e mostre quantas vezes o número 10 foi digitado. O laço de repetição deve parar quando o usuário digitar 0. '''

while True:  # Laço externo para reiniciar as tentativas caso o número 10 não seja digitado
        contador = 0  # Contador de quantas vezes o número 10 foi digitado
        tentativas = 0  # Contador de tentativas

        while tentativas < 10:  # Limite de 10 tentativas
            numero = int(input(f"Tentativa {tentativas+1}/10 - Digite um número (ou 0 para sair): "))

            if numero == 0:  # Verifica se o número é 0 para parar o laço
                break

            if numero == 10:  # Verifica se o número é 10 e incrementa o contador
                contador += 1

            tentativas += 1  # Incrementa o número de tentativas

        if contador > 0:  # Se o número 10 foi digitado ao menos uma vez, encerra o laço externo
            print(f"O número 10 foi digitado {contador} vezes.")
            break
        else:
            print("Você não digitou o número 10 nenhuma vez. Vamos tentar novamente!\n")     


