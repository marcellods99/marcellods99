"""
Questão 9
Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
"""

nota1 = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a segunda nota:\n'))
nota3 = float(input('Digite a terceira nota:\n'))

nota = (nota1 + nota2 + nota3) /3
print(f'A média de notas é: {nota}')
