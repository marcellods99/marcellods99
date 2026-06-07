def main():
    print("=== Texto Utils ===")
    phrase = input("Digite uma frase: ")

    print("\nEscolha uma opção:")
    print("[1] Converter para maiúsculas")
    print("[2] Converter para minúsculas")
    print("[3] Remover espaços extras")
    print("[4] Substituir um caractere")
    print("[5] Mascarar letra 's' como '$'")

    option = input("Opção: ")

    if option == "1":
        print(phrase.upper())
    elif option == "2":
        print(phrase.lower())
    elif option == "3":
        print(' '.join(phrase.split()))
    elif option == "4":
        old = input("Digite o caractere a ser substituído: ")
        new = input("Digite o novo caractere: ")
        print(phrase.replace(old, new))
    elif option == "5":
        print(phrase.replace('s', '$').replace('S', '$'))
    else:
        print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
