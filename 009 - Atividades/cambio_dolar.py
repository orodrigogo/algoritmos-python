# import math
from math import floor

reais = float(input("Informe quantos reais você tem para trocar: "))
dolares = reais / 5.51

print(f"Você pode trocar por $ {floor(dolares):.2f} doláres")
