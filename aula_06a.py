# trabalhando com exceções


try:
    a = int(input('Digite um número inteiro: '))
    b = int(input('Digite outro número inteiro: '))
    res = a/b
    print(f'O resultado da divisão é: {res}')
except ValueError:
    print('Erro: Você não digitou um número inteiro.')
except ZeroDivisionError:
    print('Não é possível a divisão por zero.')
except Exception as e:
    print(f'Erro inesperado: {e}')
print('Fim do programa aula_06a.py')



