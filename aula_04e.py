""" Curso de Python Fatec
    Escreva um programa que leia dois inteiros na tela apenas o menor valor. Se ambos forem iguais, imprima "Números iguais" e mostre um deles.
"""
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a < b:
    print(f'{a} é o menor número')
elif b < a:
    print(f'{b} é o menor número')
else:
    print(f'Os números digitados são iguais e o número é: {a}')
print('Fim do programa')
