print("============== LOJAS NICOLAS ==============")

preço = float(input("Preço das compras R$: "))

print("Escolha umas das FORMAS DE PAGAMENTOS a seguir\n[ 1 ] á vista dinheiro / cheque\n[ 2 ] á vista no cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão ")

opção = int(input("Qual é a sua opção: "))

if opção == 1:
    desconto = preço - (preço * 10 / 100)
    print("O valor a se pagar é %.2f mas com desconto foi para %.2f " %(preço,desconto))
elif opção == 2:
    desconto = preço - (preço* 5 /100)
    print("O valor a se pagar é %.2f mas com desconto foi para %.2f " %(preço,desconto))
elif opção == 3:
    parcelamento = preço / 2
    print("Sua compra será parcela em até 2x no cartão, então será %dR$ por mes\nNo final de tudo isso o valor a se pagar será %.2f" %(parcelamento,preço))
else:
    parcela = int(input("Em quantas parcela quer fazer? "))
    parcelamento = preço + (preço * 20 / 100) 
    total = parcelamento / parcela
    print("Sua compra será parcela em até %dx no cartão de %dR$ COM JUROS\nSua compra de %.2f vai custa %.2f no final." %(parcela,total,preço,parcelamento))