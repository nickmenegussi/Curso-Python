print("""======== 10 Termos de uma PA ========
=====================================""")

pt = int(input("Informe o seu Primeiro Termo : "))
razao = int(input("Informe a sua razão: ")) 
decimo = pt + (10 - 1) * razao


for n in range(pt, decimo + 1,razao):
    print("%d" %n, end=' → ')
print("ACABOU")