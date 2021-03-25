# Importando somente o date do módulo datetime.
from datetime import date

anoNascimento = int(input("Digite que ano você nasceu: "))
"""
A função today() captura a data atual,
e o year pega somente o ano da data.
"""
anoAtual = date.today().year

idade = anoAtual - anoNascimento
print(f"Você tem {idade} anos.")
