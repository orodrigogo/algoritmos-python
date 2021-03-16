# Somando strings.
v1 = input('Digite o valor de v1: ')
v2 = input('Digite o valor de v2: ')

resultado = v1 + v2
# Ele irá colocar o valor de v1 ao lado de v2, pois são textos.
print('O resultado é: ', resultado)


# Utilizando os Operadores Aritméticos
n1 = int(input('Digite o valor de n1: '))
n2 = int(input('Digite o valor de n2: '))

print('>>> Resultados >>>')
print(f'O resultado a SOMA de {n1} + {n2} = {n1 + n2}')
print(f'O resultado a SUBTRAÇÃO de {n1} - {n2} = {n1 - n2}')
print(f'O resultado a MULTIPLICAÇÃO de {n1} * {n2} = {n1 * n2}')
print(f'O resultado a DIVISÃO de {n1} / {n2} = {n1 / n2}')


# Utilizando ordem de precedência.

nota1 = 10
nota2 = 6
nota3 = 5.5

# Sem ordem de precedência faz-se 10+6+5.5 = 21.5 / 3 = 17.83
media = nota1 + nota2 + nota3 / 3
print(f'A média final é {media:.2f}')

# Com ordem de precedência
media = (nota1 + nota2 + nota3) / 3
print(f'A média final é {media:.2f}')
