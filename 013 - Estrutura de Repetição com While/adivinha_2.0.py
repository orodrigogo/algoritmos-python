from random import randint

computer = randint(0, 5)
playing = True
tries = 0

# Enquanto playing for True
while playing:
    tries += 1
    player = int(input("Qual é seu palpite (0 à 5): "))

    if player == computer:
        playing = False
    else:
        print('Que pena. Você errou!')

print(f"""
    PARABÉNS, VOCÊ GANHOU!
    Você precisou de {tries} tentativas para ganhar.
""")
