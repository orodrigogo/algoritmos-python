largura = float(input("Digite a LARGURA da parede em metros: "))
altura = float(input("Digite a ALTURA da parede em metros: "))

area = largura * altura
print(f"Sua parede tem area de {area:.2f}")

tinta = area / 2
print(f"Para pintar a sua parede, você irá precisar de {tinta} litros de tinta!")

