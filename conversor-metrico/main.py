#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

num = float(input('Digite um número: '))
cm = num * 100
mm = num * 1000
print(f'O número {num} convertido para centimetros é {cm}cm e para milímetros é {mm}mm')
