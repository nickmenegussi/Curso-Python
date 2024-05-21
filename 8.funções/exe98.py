from time import sleep

# 1. criar função contador e com ela fazer a logica de contagem
def contdor():
    print("\033[36m="*45)
    print("Contado de 1 até 10, de 1 em 1: ")

    for x in range(1, 11):
        print(x , end=" ", flush=True) # vai ligar o buffer de tela
        sleep(0.5)
    print("FIM!!")
    print("\033[36m=\033[m"*45)
    print("\033[34mContagem de 10 até 0 de 2 em 2!")

    for x in range(10, -2 , -2):
        print(x, end=" ", flush=True)
        sleep(0.5)
    print("FIM!!\033[m")
    print("\033[34m=\033[m"*45)

    print("Agora é sua vez de personalizar a contagem! ")
    inicio = int(input("Inicio: "))
    fim = int(input("Fim: "))
    Passo = int(input("Passo: "))
    # se o passo for negativo eu executo para deixar ele positivo.
    if Passo == 0: # passo zero nao existe pois dai a gente adiciona o 1
        Passo = 1
    if Passo < 0: # se o passo for menor que zero ou seja o numero negativo iremos colocar ele para positivo
        Passo *= -1
    print("="*45)
    print(f"Contagem de  {inicio} até {fim} de {Passo} em {Passo}")
    # PAREI AQUI,  VOLTAR AMANHA ,voltei e ENTENDI UM POUCO
    if inicio < fim: # se o inicio for menor do que o fim 
        for x in range(inicio, fim + 1, Passo):
            print(x,  end=" " , flush=True)
            sleep(0.5)
        print("FIM!!!")
    elif inicio > fim:# se nao se inicio for maior do que o fim
        if Passo > 0: # por que com zero nao há contagem 
            for x in range(inicio, fim - 1,  - Passo):
                print(x, end=" " , flush=True)
                sleep(0.5)
            print("FIM!!")
                  
                
    """if inicio < fim: # parei aqui
        for x in range(inicio, fim + 1, Passo):
            print(x , end=" " , flush=True)
            sleep(0.5)
        print("FIM!!!")
    if inicio > fim:
        for p in range(inicio,  - fim,  - Passo):
            print(p , end=" ", flush=True)
            sleep(0.5)
        print("FIM!!")"""
    
contdor()