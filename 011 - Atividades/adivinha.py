from random import randint
from time import sleep

computador = randint(0, 5)
usuario = int(input("adivinhe o número: "))

print("Hummm... verificando se você acertou...")
sleep(3)

if computador == usuario:
    print("PARABÉNS, VOCÊ GANHOU!")
else:
    print("QUE PENA, VOCÊ PERDEU!")

print(f"""
    O computador escolheu: {computador}
    E você escolheu: {usuario}
""")
