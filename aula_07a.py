# Trabalhando com listas
# Listas são mutáveis, ou seja, podem ser alteradas
# Listas são representadas por colchetes []
# Listas podem conter diferentes tipos de dados
# Listas podem conter listas dentro delas
# Listas podem ser indexadas, ou seja, podemos acessar os elementos da lista pelo índice
# Listas podem ser fatiadas, ou seja, podemos acessar uma parte da lista
# Listas podem ser ordenadas, ou seja, podemos ordenar os elementos da lista
# Listas podem ser invertidas, ou seja, podemos inverter a ordem dos elementos da lista
# Listas podem ser concatenadas, ou seja, podemos juntar duas listas
# Listas podem ser repetidas, ou seja, podemos repetir os elementos da lista
# Listas podem ser copiadas, ou seja, podemos copiar os elementos da lista
# Listas podem ser somadas, ou seja, podemos somar os elementos da lista
# Listas podem ser multiplicadas, ou seja, podemos multiplicar os elementos da lista
# Listas podem ser divididas, ou seja, podemos dividir os elementos da lista
# Listas podem ser subtraídas, ou seja, podemos subtrair os elementos da lista
# Listas podem ser comparadas, ou seja, podemos comparar os elementos da lista
# Listas podem ser filtradas, ou seja, podemos filtrar os elementos da lista
# Listas podem ser mapeadas, ou seja, podemos mapear os elementos da lista
# Listas podem ser reduzidas, ou seja, podemos reduzir os elementos da lista
l= [1, 2, 3, 4, 5, 10, 13, 15, 20, 25, 30, 35, 40, 45, 50]
print('Exibindo a lista l')
print(l)
print('Exibindo o primeiro elemento da lista l')
print(l[0])
print('Exibindo todos os elementos da lista l')
print(l[:])
print('Exibindo os elementos individuais da lista l')
print('Esta lista possui', len(l), 'elementos')
i = 0
while i < len(l):
    print(l[i])
    i += 1
# removendo a virgula da lista
print('Exibindo lista sem virgula')
for i in l:
    print(i, end=' ')
print ('\nFim do programa')
# inserindo elementos na lista
l.append(100)
l.insert(0, 200)
print('Exibindo lista com o elemento 100 adicionado')
print(l)
# excluindo elementos na lista
print('Removendo o elemento 200 da lista')
l.remove(200)
print('O item 5 da lista é', l[5])
print('vamos remover o item 5 da lista')
del l[5]
print('Exibindo lista com o elemento 200 removido')
print(l)
# ordenando a lista
l.sort()
print('Exibindo lista ordenada')
print(l)
# invertendo a lista
l.reverse()
print('Exibindo lista invertida')
print(l)
l.sort(reverse=False)
print('Exibindo lista ordenada de forma crescente')
print(l)
print('Cuidado com cópias de listas')
# l2 = l
l2 = l
l3 = l[:]
print('ID da lista l', id(l), 'lista l', l)
print('ID da lista l2', id(l2), 'lista l2', l2)
print('ID da lista l3', id(l3), 'lista l3', l3)
# usando for para percorrer a lista
print('Exibindo lista l com for')
for i in l:
    print(i, end=' ')
# iterando a lista com for e mostrando o índice
print('Exibindo lista l com for e índice')
for i in range(len(l)):
    print('O elemento', l[i], 'está na posição', i)
# iterando a lista com for e mostrando o índice e o valor
print('Exibindo lista l com for e índice e valor')
for i, v in enumerate(l):
    print('O elemento', v, 'está na posição', i)
# Trabalhando com list comprehension
[print('O elemento', l[i], 'está na posição', i) for i in range(len(l))]
[print('O elemento', v, 'está na posição', i) for i, v in enumerate(l)]
  
print ('\nFim do programa')

# construindo uma lista de termos de uma PA e inserir em uma lista
# PA = Progressão Aritmética
p=int(input('Digite o primeiro termo da PA: '))
r=int(input('Digite a razão da PA: '))
n=int(input('Digite o número de termos da PA: '))
termos = []
[termos.append(p + (i * r)) for i in range(n)]
print('Os termos da PA são:', termos)

# sem append... mais pythonic
termos = [p + (i * r) for i in range(n)]
print('Os termos da PA são:', termos)

# criando uma lista a partir de uma quantidade de termos digitada pelo usuário
n = int(input('Digite a quantidade de termos da lista: '))
lista = []
lista = [float(input(f'Digite o elemento {i} da lista: ')) for i in range(n)]
[print(f'O elemento {i} da lista é: {v:.2f}')for i, v in enumerate(lista)]

# criando uma lista de números aleatórios
from random import randint
qtde = int(input('Digite a quantidade de números aleatórios: '))
lista = [randint(1, 20) for i in range(qtde)]
print('Os números aleatórios são:', lista)
# pesquisando um valor x != 0 digitado pelo usuário e verifique a quantidade de vezes que o número aparece na lista e a posição em que ele aparece
x = int(input('Digite um número diferente de 0: '))
while x == 0:
    x = int(input('Digite um número diferente de 0: '))
qtde = lista.count(x)
if qtde == 0:
    print(f'O número {x} não aparece na lista')
else:
    print(f'O número {x} aparece {qtde} vezes na lista')
    print(f'O número {x} aparece nas posições:', end=' ')
    for i in range(len(lista)):
        if lista[i] == x:
            print(i, end=' ')
print(f'Fim do programa')
    




