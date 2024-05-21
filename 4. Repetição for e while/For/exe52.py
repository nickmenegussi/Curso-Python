n = int(input("Digite um número: "))
cont = 0

for x in range(1, n + 1):
    if n % x == 0 and n % 1 == 0:
        cont += 1
        print("\033[34m",end=' ')
    else:
        print("\033[35m", end=' ')
    print(x, end=' ')
print("\033[m\nO numero %d foi divisível %d " %(n,cont))

if cont == 2:
    print("E por isso ele é primo")
else:
    print("E por isso ele não é primo")