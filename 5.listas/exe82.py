lista = []
impar = []
pares = []



while True:
    n = int(input("Informe um valor: "))
    lista.append(n)
    r = str(input("Deseja continuar? [S/N]:"))
    if n % 2 == 0:
        pares.append(n)
    else:
        impar.append(n)
    if r in "Nn":
        break
print(f"\033[33mLista completa: {lista}\033[m")
print(f"\033[34mLista de números pares: {pares}\033[m")
print(f"\033[35mLista de números ímpares: {impar}\033[m")
