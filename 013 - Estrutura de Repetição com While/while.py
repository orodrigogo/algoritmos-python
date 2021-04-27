"""
Exemplo sem Laço de Repetição
print('Bloco 0')
print('Bloco 1')
print('Bloco 2')
print('Bloco 3')
print('Bloco 4')
print('Bloco 5')
print('Pular')
"""
import time
block = 5

# ENQUANTO os BLOCOS for MENOR ou IGUAL a 5 FAÇA
while block > 0:
    print(f"Andar para o bloco {block}")
    # incremento long sintaxe
    # block = block + 1

    # incremento short sintaxe
    # block += 1

    # decremento
    block -= 1
    time.sleep(1)

print("Pular!")

