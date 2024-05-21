lista = []



while True:
    num = int(input("Digite um número: "))
    if num in lista: # se numero ja estiver na lista nao adicione
        print("Valor duplicado! Portanto não será adicionado")
    else:
        lista.append(num)
        print("\033[36mValor adicionado com sucesso\033[m")
    
    op = str(input("Deseja continuar? ")).strip()

    while op not in "SsNn":
        op = str(input("Deseja continuar? ")).strip()
    if op in "Nn":
        break

print(sorted(lista))
