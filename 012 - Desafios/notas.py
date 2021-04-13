studentName = input("Nome do aluno: ")
course = input("Nome da disciplina: ")
examScore = float(input("Nota da prova: "))
jobScore = float(input("Nota do trabalho: "))
projectScore = float(input("Nota do projeto: "))

average = (examScore + jobScore + projectScore) / 3
print(f"A média do aluno é {average:.1f}")

if average < 7:
    print("REPROVADO!")
else:
    print("APROVADO!")
