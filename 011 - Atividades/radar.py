from random import randrange

# simulando o radar.
velocidade = randrange(60, 120, 10)

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("MULTADO!")
    print(f"O carro passou a {velocidade}Km/h")
    print(f"O valor da multa é R${multa}")
else:
    print("Velocidade OK")
