def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Valor inválido. Por favor, digite um número.")


def main():
    print("=== Calculadora Python ===")
    n1 = get_number("Digite o primeiro número: ")
    n2 = get_number("Digite o segundo número: ")

    print("\nEscolha a operação:")
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Média ponderada (5, 12, 20, 15)")

    choice = input("Operação: ")

    if choice == "1":
        result = n1 + n2
        print(f"Resultado: {n1} + {n2} = {result}")
    elif choice == "2":
        result = n1 - n2
        print(f"Resultado: {n1} - {n2} = {result}")
    elif choice == "3":
        result = n1 * n2
        print(f"Resultado: {n1} * {n2} = {result}")
    elif choice == "4":
        if n2 == 0:
            print("Erro: divisão por zero não permitida.")
        else:
            result = n1 / n2
            print(f"Resultado: {n1} / {n2} = {result}")
    elif choice == "5":
        weights = [1, 2, 3, 4]
        values = [5, 12, 20, 15]
        weighted_sum = sum(v * w for v, w in zip(values, weights))
        average = weighted_sum / sum(weights)
        print(f"Média ponderada dos valores {values} com pesos {weights}: {average}")
    else:
        print("Operação inválida. Tente novamente.")


if __name__ == "__main__":
    main()
