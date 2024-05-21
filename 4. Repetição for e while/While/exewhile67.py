print("-"*21)
print("Programa de Tabuada")
print("-"*21)



while True:
    tabuada = int(input("Voce quer a tabuada de qual valor? "))
    if tabuada  < 0:
        break
    for x in range(1, 11):
        c = tabuada * 1
        result = x * tabuada
        print("%d x %d = %d " % (tabuada,x,result))
    print("-"*21)
print("Fim de programa da tabuada , Volte sempre!")