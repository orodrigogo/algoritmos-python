n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

small = n1
if n2 < n1 and n2 < n3:
    small = n2

if n3 < n1 and n3 < n2:
    small = n3

biger = n1
if n2 > n1 and n2 > n3:
    biger = n2

if n3 > n1 and n3 > n2:
    biger = n3

print('o menor número é', small)
print('o maior número é', biger)