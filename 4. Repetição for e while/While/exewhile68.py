import random 

print("-"*26)
print("Vamos jogar Par OU ÍMPAR")
print("-"*26)

c = 0

while True:
    v = int(input("Informe um valor: "))
    opcao = input("Par ou ímpar? [P/I] ").upper().strip()
    sorteador = random.randint(1, 100)
    t = v + sorteador
    if opcao == "I":
        if t % 2 == 1:
            print("Voce jogou %d e o computador %d. Total de %d Deu Ímpar" % (v, sorteador, t))
            print("Voce ganhou!")
            c += 1
        else:
            print("Voce jogou %d e o computador %d. Total de %d Deu Ímpar" % (v, sorteador, t))
            print("Voce perdeu!")
            break
    elif opcao == "P":
        if t % 2 == 0:
            print("Voce jogou %d e o computador %d. Total de %d Deu Par" % (v, sorteador, t))
            print("Voce ganhou")
            c += 1
        else:
            print("Voce jogou %d e o computador %d. Total de %d Deu Par" % (v, sorteador, t))
            print("Voce perdeu")
            break
    print("Vamos jogar novamente...")
print("Game Over !! Voce venceu %d vezes" %c)