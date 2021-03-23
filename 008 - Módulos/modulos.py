# Importando o módulo completo, ou seja, todas as funções mesmo sem usá-las.
# import math

# Importando as funções específicas do módulo.
from math import ceil, floor, factorial


numero = float(input("Digite um número quebrado: "))
print(f"PARA CIMA: {ceil(numero)}")
print(f"PARA BAIXO: {floor(numero)}")
print(f"Fatorial: !{factorial(int(numero))}")
