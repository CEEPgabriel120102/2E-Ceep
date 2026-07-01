def calcular_media():
    print("--- Calculadora de Médias ---")
    
    # Loop para garantir que o usuário escolha uma quantidade válida de notas
    while True:
        try:
            qtd_notas = int(input("Quantas notas deseja calcular (de 2 a 5)? "))
            if 2 <= qtd_notas <= 5:
                break
            else:
                print("Por favor, escolha um número de 2 a 5.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    notas = []
    
    # Loop para pedir as notas de acordo com a quantidade escolhida
    for i in range(qtd_notas):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1}: "))
                if 0 <= nota <= 10:  # Garante que a nota esteja em um intervalo comum (0 a 10)
                    notas.append(nota)
                    break
                else:
                    print("Por favor, digite uma nota válida entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    # Calcula e exibe a média
    media = sum(notas) / qtd_notas
    print("\n--- Resultado ---")
    print(f"Notas digitadas: {notas}")
    print(f"A média final é: {media:.2f}")

# Executa a função
calcular_media()