#4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.

soma = 0
contador = 0

temperatura = float(input('Digite uma temperatura em Celsius ou -273 para encerrar: '))

while temperatura != -273:
    soma = soma + temperatura
    contador = contador + 1

    temperatura = float(input('Digite uma temperatura em Celsius ou -273 para encerrar: '))

if contador > 0:
    media = soma / contador
    print(f'A média das temperaturas é {media:.2f}°C')
else:
    print('Nenhuma temperatura válida foi digitada.')
