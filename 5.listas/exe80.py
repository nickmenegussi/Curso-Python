# nao consegui fazer, tive dificuladade
lista = []

for x in range(1, 6):
    n = int(input(f"Digite o seu {x} número: "))
    if x == 1 or n > max(lista):
        lista.append(n)
        print("Adicionado ao final da lista")
    else:
        for p, c in enumerate(lista):
            if n < c: # verificar se o numero que eu quero inserir é menor que a ultima posição 
                lista.insert(p,n) # vou inserir na posicao p o valor n
                print(f"Adicionado na posição {p} da lista")
                break


print(f"Os valores digitados em ordem foram {lista}")