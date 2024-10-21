while True:
    # Solicitar operação
    Operacao = input("Digite a operação (1 - Soma, 2 - Subtração, 3 - Divisão, 4 - Multiplicação) ou 'q' para sair: ")

    # Verifica se é para sair
    if Operacao == 'a' or Operacao == 'A':
        break

    # Tenta converter os números para float
    try:
        N1 = float(input("Digite o primeiro número: "))
        N2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada inválida! Por favor, insira números válidos.")
        continue

    # Verifica qual operação foi solicitada
    if Operacao == '1':
        total = N1 + N2
    elif Operacao == '2':
        total = N1 - N2
    elif Operacao == '3':
        total = N1 / N2
    elif Operacao == '4':
        total = N1 * N2
    else:
        print("Operação inválida! Por favor, tente novamente.")

    print(f"O resultado da operação é: {total}")
