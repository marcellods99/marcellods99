def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt).replace(',', '.'))
        except ValueError:
            print("Valor inválido. Digite um número válido.")


def main():
    print("=== Coleta de Dados ===")
    nome = input("Digite seu nome: ").strip().title()
    idade = get_int("Digite sua idade: ")
    altura = get_float("Digite sua altura em metros (por exemplo: 1.75): ")

    print("\nResumo do cadastro:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Altura: {altura:.2f} m")

    if idade < 18:
        print("Status: Menor de idade")
    else:
        print("Status: Adulto")


if __name__ == "__main__":
    main()
