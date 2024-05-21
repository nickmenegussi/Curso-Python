from time import sleep
import random

print("Estou pensando em um número... ")
sleep(2)
print("PENSEI!!!! EM UM NUMERO ENTRE 0 E 10!")
sleep(2)
print("Será que conseguirá adivinhar? Está pronto? ")
tentativa = 0

# usuario
num = int(input("Digite novamente: "))
tentativa += 1


sorteador = random.randint(0, 10)




while num != sorteador:
    print("Quase, ", end='')
    num = int(input("Digite novamente: "))
    tentativa += 1  # é aqui pq ? because when the user tentar novamente o program vai contar + 1
    if num > sorteador:
        print("E tente um número menor")
    elif num < sorteador:
        print("tente um número maior")
    elif sorteador == num:
        print("Parabéns", end=" ")  
print("ao todo foram %d tentativas" % tentativa)