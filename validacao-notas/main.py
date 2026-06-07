#3) Escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserida uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

for c in range(1, 16):
    nota = int(input('Digite uma nota de 0 a 5:\n'))

    while nota < 0 or nota > 5:
        print('Valor Incorreto, digite novamente!')
        nota = int(input('Digite uma nota de 0 a 5:\n'))

    print('Valor Correto')
