# DESAFIO 060
# Faça um programa que leia um número qualquer e mostre seu fatorial.
# ex: 5! = 5x4x3x2x1 = 120


import math 
num = int(input('Digite um valor para ser fatorado: '))
fatorial = num
print(f'{num}! = {num} ', end = '')
while fatorial != 1:
    fatorial -= 1
    print(f'x {fatorial} ', end = '')
print(f'= {math.factorial(num)}')

'''
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end = '')
while c > 0:
    print(f'{c}', end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print(f'{f}')
'''