"""
Questão 3
Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
"""

nome = str(input('Digite o seu nome:\n'))
idade = int(input('Digite sua idade:\n'))
altura = float(input('Digite sua altura:\n'))
print(f'Olá {nome}, você tem {idade} e mede {altura} metros!')
