"""
    Faça um programa que leia um número inteiro e
    mostre na tela o seu sucessor e seu antecessor
"""

# Captura o número digitado pelo usuário.
numero = int(input("Digite um número: "))

# Subtraí 1 para saber qual número vem antes.
antecessor = numero - 1
# Adiciona 1 para saber qual número vem depois.
sucessor = numero + 1

# Monta uma frase para exibir o resultado.
print(f"O número {numero} tem o antecessor {antecessor} e sucessor {sucessor}")
