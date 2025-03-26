""" Curso de Fatec
    Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
    Lembrando que para saber se um número é par ou ímpar, basta dividir o número por 2 e verificar o resto da divisão.
"""
x = int(input("Digite um número inteiro: ")) # Recebe um número inteiro
resto = x % 2 # Calcula o resto da divisão por 2
# forma clean de fazer o if
# print("O número", x, "é", "par" if resto == 0 else "ímpar")
if resto == 0: # Se o resto for zero, então o número é par
    print("O número", x, "é par.")
else: # Se o resto for diferente de zero, então o número é ímpar
    print("O número", x, "é ímpar.")
print("Fim do programa") # Fim do programa
