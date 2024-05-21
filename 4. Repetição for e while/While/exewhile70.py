print("-"*28)
print("    Loja SUPER BARATAO")
print("-"*28)


Opcao = " "

t = custa100 = barato = menor = cont = 0

while Opcao not in "N":
    nomep = input("Nome do Produto: ")
    preco = float(input("Preço do Produto: "))
    cont += 1 # REVISAR
    t += preco

    Opcao = input("Quer continuar? [S/N]").upper()
    if Opcao == "N":
        break
    if preco > 1000:
        custa100 += 1
    if cont == 1: # vai checar se so tem uma fez o programa repedito  , REVISAR
        menor = preco
    else:
        if preco < menor:
            menor = preco
    
print("Ao total de sua compra voce deverá pagar R$%.2f\nTemos %d produtos custando mais de R$1000.00\nO produto mais barato foi %.2f" % (t,custa100,menor))