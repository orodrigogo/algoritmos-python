km = float(input("Quantos KM você percorreu? "))
dias = int(input("Quantos DIAS você está com o carro? "))

valor = (dias * 60) + (km * 0.15)
print(f"O total a ser pago é R$ {valor:.2f}")

