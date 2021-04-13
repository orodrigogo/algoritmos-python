housePrice = float(input("Valor da casa R$ "))
salary = float(input("Salário R$"))
years = int(input("Quantos você desejar pagar: "))

salaryLimit = salary * 30 / 100
installment = housePrice / (years * 12)

print(f"Para pagar uma casa de R${housePrice:.2f} em {years} anos a prestação será de R${installment:.2f}")

if installment > salaryLimit:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo AUTORIZADO!")
