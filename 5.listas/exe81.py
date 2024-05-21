lista = []

while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    r = str(input("Deseja continuar? [S/N]: ")).strip()
    while r not in "SsNn":
        r = str(input("Deseja continuar? [S/N]: ")).strip()
    if r in "Nn":
        break
if 5 not in lista:
    print("O valor 5 nao foi encontrado na lista!")
else:
    print("O VALOR 5 foi encontrado")
print(f"Voce digitou um total de {len(lista)} elementos.")
lista.sort(reverse=True)
print(f"OS valores da lista em ordem decescente são {lista}")
print(lista)