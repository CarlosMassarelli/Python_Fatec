print(f'Início do programa aula_05a.py')
# comandos de repetição
# for e while
cont=1
while cont <= 10:
    print(f'Contador: {cont}')
    cont += 1
print('Contador final:', cont)
print('Fim do programa aula_05a.py')

# Verificação de par ou ímpar
print(f'Verificação de par ou ímpar')
x=1
while x != 0:
    x = int(input('Digite um número (0 para sair): '))
    if x % 2 == 0:
        print(f'{x} é par')
    else:
        print(f'{x} é ímpar')
print('Fim do programa aula_05a.py')
 
 # Usando continue
print(f'Início do programa testando o continue')
print('Digite números inteiros e descubra se são múltiplos de 4')
i=0
while i < 25:
    i += 1
    if i % 4 == 0:
        print(f'___ {i} é múltiplo de 4')
        continue
    print(i, end=' ')
print('fim do programa testando o continue')

# testando o comando break
print(f'Início do programa testando o break')
print(f'Digite números inteiros e descubra se são pares ou ímpares')
x = ''
while True:
    x = int(input('Digite um número (0 para sair): '))
    if x == 0: # se o número for 0, sai do loop
        print('Você digitou 0, saindo do loop...')
        break # sai do while True
    if x % 2 == 0: # se for múltiplo de 4
        print(f'___ {x} é par')
    else: # se não for múltiplo de 4
        print(f'___ {x} é ímpar')
        
print('Fim do programa testando o break')

# Fazendo uma tabuada
print(f'Início do programa testando a tabuada')
x = int(input('Digite um número para fazer a tabuada: '))
print(f'Tabuada do {x}')
for i in range(0, 11):
    print(f'{x} x {i} = {x*i}')
print('Fim do programa testando a tabuada')

# progressão aritmética
print(f'Início do programa testando a PA')
x = int(input('Digite o primeiro termo da PA: '))
y = int(input('Digite a razão da PA: '))
print(f'PA de: {x}')
for i in range(1, 11):
    x += y
    print(f'Termo {i} da PA é {x}')
print('Fim do programa testando a PA')

# progressão geométrica
print(f'Início do programa testando a PG')
x = int(input('Digite o primeiro termo da PG: '))
y = int(input('Digite a razão da PG: '))
print(f'PG de: {x}')
for i in range(1, 11):
    x *= y
    print(f'Termo {i} da PG é {x}')
print('Fim do programa testando a PG')


