""" Curso de Python Fatec
    Escreva um programa para exibir o nome e a categoria de um lutador de boxe, a partir do peso informado pelo usuário.
    A categoria é determinada conforme a tabela abaixo:
    Categoria Peso
    abaixo de 40 kg não luta
    Mosca até 47 Kg
    Pena até 57 Kg
    Leve até 61 Kg
    Médio até 73 Kg
    Pesado acima de 73 Kg
"""

nome = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
if peso < 40:
    categoria = 'não pertence a nenhuma categoria'
elif peso <= 47:
    categoria = 'Mosca'
elif peso <= 57:
    categoria = 'Pena'
elif peso <= 61:
    categoria = 'Leve'
elif peso <= 73:
    categoria = 'Médio'
else:
    categoria = 'Pesado'
print(f'{nome} é da categoria {categoria} por pesar {peso} Kg')
print('Fim do programa')
    