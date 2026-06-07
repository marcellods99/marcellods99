#10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.


num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print('Qual operação você deseja realizar\n[1] - Soma\n[2] - Subtração\n[3] - Multiplicação\n[4] - Divisão ')

escolha = int(input(''))
if escolha == 1:
  r = num1 + num2
elif escolha == 2:
  r = num1 - num2
elif escolha == 3:
  r = num1 * num2
elif escolha == 4:
  r = num1/num2
else:
  print('burro')


r1 = 'par' if num1 % 2 == 0 else 'ímpar'
r2 = 'par' if num2 % 2 == 0 else 'ímpar'

r2_1 = 'positivo' if num1 > 0 else 'negativo'
r2_2 = 'positivo' if num2 > 0 else 'negativo'

r3_1 = 'inteiro' if num1 == int(num1) else 'decimal'
r3_2 = 'inteiro' if num2 == int(num2) else 'decimal'

print('-=' * 20)
print(f'O resultado da operação foi: {r}')
print(f'O primeiro número ({num1}) é {r1}, {r2_1} e {r3_1}.')
print(f'O segundo número ({num2}) é {r2}, {r2_2} e {r3_2}.')
print('-=' * 20)
