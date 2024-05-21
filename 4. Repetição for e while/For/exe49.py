print("""======== Menu de Tabuada ========
[ 1 ] Tabuada do 1
[ 2 ] Tabuada do 2
[ 3 ] Tabuada do 3
[ 4 ] Tabuada do 4
[ 5 ] Tabuada do 5
[ 6 ] Tabuada do 6
[ 7 ] Tabuada do 7
[ 8 ] Tabuada do 8
[ 8 ] Tabuada do 9
[ 10 ] Tabuada do 10""")


opcao = int(input("Informe qual tabuada que está no menu vai querer: "))

print("-"*12)

while opcao > 10:
    print("ERROR, Digite novamente ")
    opcao = int(input("Por favor digite novamente um número que está no Menu: "))
for x in range(1,11):
    if opcao == 1:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " %(opcao, cont, resul))
    elif opcao == 2:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " % (opcao, cont, resul))
    elif opcao == 3:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " % (opcao, cont, resul))
    elif opcao == 4:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " % (opcao, cont, resul))
    elif opcao == 5:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " % (opcao, cont, resul))
    elif opcao == 6:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " % (opcao, cont, resul))
    elif opcao == 7:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " % (opcao, cont, resul))
    elif opcao == 8:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " % (opcao, cont, resul))
    elif opcao == 9:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " % (opcao, cont, resul))
    elif opcao == 10:
        cont = x * 1
        resul = x * opcao
        print("%d x %d = %d " % (opcao, cont, resul))

    
print("-"*12)