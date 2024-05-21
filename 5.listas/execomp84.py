teste = []
verdadeiro = []
p = []

while True:
    teste.append(str(input("Nome: ")))
    peso = float(input("Peso: "))
    teste.append(peso)
    p.append(peso)

    pesomax = max(p)
    pesomin = min(p)

    verdadeiro.append(teste.copy())
    teste.clear() # apagar a lista temporária
    r = input("Deseja continuar? [S/N]")
    if r in "Nn":
        break
 
print(f"O Maior peso foi de {pesomax} Peso de ", end="")
for pessoa in verdadeiro:
    if pessoa[1] == pesomax:
        print(f"[{pessoa[0]}] ",end="")

print(f"\nO Menor peso foi de {pesomin}. Peso de ", end="")
for pessoa in verdadeiro:
    if pessoa[1] == pesomin:
        print(F"[{pessoa[0]}] " ,end="")
