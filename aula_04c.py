# Curso Python Fatec

risco=input('Digite BX (Baixo) ou AL (Alto) para grau de risco: ').upper()
valor=float(input('Digite um valor: '))

if risco != 'BX' and risco != 'AL':
    print('Risco Inválido')
elif valor < 0 or valor == 0:
    print('Valor inválido')
else:
    if risco == 'BX':
        if valor < 1000:
            tipo = 'Poupança'
        else:
            tipo = 'Renda Fixa'
    else:
        if valor < 1000:
            tipo = 'Bitcoin'
        else:
            tipo = 'Ações'
    print(f'Você poderia invertir em {tipo}')
    

"""
risco = input("Qual o risco? (A, B, C, D ou E): ").upper()
if risco == 'A':
    print('Risco Alto')
elif risco == 'B':
    print('Risco Médio')
elif risco == 'C':
    print('Risco Baixo')
elif risco == 'D':
    print('Risco Irrelevante')
elif risco == 'E':
    print('Risco Inexistente')
else:
    print('Risco Inválido')
valor=float(input('Digite um valor: '))
if valor < 0:
    print('Valor negativo')
elif valor == 0:
    print('Valor nulo')
else:
    print('Valor positivo')
if risco == 'A' and valor > 1000:
    print('Risco Alto e Valor Alto')
"""