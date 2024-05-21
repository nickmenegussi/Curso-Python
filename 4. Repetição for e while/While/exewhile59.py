import time

v1 = int(input("Informe seu primeiro número: "))
v2 = int(input("Informe seu segundo número: "))

cores = {
    "Padrão":"\033[30m",
    "Verde":"\033[32m"
}

print("-="*12)
menu = 0
maiornum = 0

while menu != 5:
    print("""     Menu de opções     
    [ 1 ] somar 
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] new numbers
    [ 5 ] exit program """)
    menu = int(input(">>>>> Qual é a sua opção? "))
    print("-="*12)
    if menu == 1:
        soma = v1 + v2 
        print("A soma de %d com %d foi de %d " %(v1,v2,soma))
    elif menu == 2:
        vezes = v1 * v2
        print(" A multiplicação de %d com %d foi de %d  "% (v1,v2 ,vezes))
    elif menu == 3:
        if v1 > v2:
            maiornum = v1
            print("Entre os números %d e %d o maior foi %d  "% (v1,v2 ,maiornum))
        else:
            maiornum = v2
            print(" Entre os números %d e %d o maior foi %d  "% (v1,v2 ,maiornum))
    elif menu == 4:
        v1novo = int(input("Informe seu primeiro novo valor: "))
        v2novo = int(input("Informe seu segundo novo valores: "))
    elif menu == 5:
        print("Saindo...")
        time.sleep(2)
        print("Obrigado por ter jogado , volte sempre!")
    else:
        print("Ops erro, tente novamente")
print("-="*12)