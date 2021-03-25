import datetime

data = datetime.date.today()
ano = datetime.date.today().year
dia = datetime.date.today().day
mes = datetime.date.today().month

print(f"Data atual: {data}")
print(f"Você está no dia {dia}")
print(f"Você está no mês {mes}")
print(f"Você está no ano {ano}")

"""
Desenvolva uma aplicação que pergunte o ano de nascimento da 
pessoa e utilizando o módulo datetime mostre quantos anos a pessoa têm. 
"""