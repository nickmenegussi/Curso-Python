import random
from time import sleep

class Game_jokenpo:
    def __init__(x):
        print("Suas opções:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura")

        jogada = int(input("Qual é a sua jogada? "))
        while jogada >= 3:
            itens = ["Pedra", "Papel", "Tesoura"]
            cores = {
                'Limpa':'\033[m',
                'Azul':'\033[0;34m',
                'Ciano':'\033[36m',
                'Red':'\033[31m',
                'Verde':'\033[32m',
                'Amarelo':'\033[33m',
                'Cinza':'\033[37m'
            }       
            sorteador = random.randint(0,2)
            frase = "O número digitado não está na base de opções,porfavor digitar novamente..."
            print(cores["Amarelo"] , frase , cores["Limpa"])

            jogada = int(input("Digite Novamente um número que tem nas opções do game: "))

            print("JO")
            sleep(2)
            print("KEN")
            sleep(2)
            print("PO!!")

            print("="*24)

#   jogarnovamente = input("Ops , deu empate, se quiser seguir digite [Y] para Sim or [N]para Não: ")
            print(" O computador jogou %s " % cores["Verde"],itens[sorteador],cores["Limpa"])
            if jogada == 0:
                print(" O jogador jogou %s " % cores["Red"],itens[jogada], cores["Limpa"])
            elif jogada == 1:
                print(" O jogador joogu %s" % cores['Azul'],itens[jogada],cores['Limpa'])
            elif jogada == 2:
                print(" O Jogador jogou %s " % cores["Ciano"],itens[jogada],cores["Limpa"])
            print("="*24)
        
#while itens[sorteador] == itens[jogada]:
#    jogarnovamente = input("Ops , deu empate, se quiser seguir digite [Y] para Sim or [N]para Não: ")
# Condição de vitória ou empate e 
            if sorteador == 0: # o computador escolheu Pedra
                if jogada == 1:
                    print("Jogador VENCEU")
                elif jogada == 2:
                    print("O Computador VENCEU")
            if sorteador == 1:
                if jogada == 0:
                    print("Computador VENCEU")
                elif jogada == 2:
                    print("Computador VENCEU")
            if sorteador == 2:
                if jogada == 0:
                    print("Jogador VENCEU")
                elif jogada == 1:
                    print("Computador VENCEU")
            frase = "WOW, Temos um EMPATE" 
            if sorteador == 1  and jogada == 1:
                print(cores["Cinza"], frase , cores["Limpa"])
            elif sorteador == 0 and jogada == 0:
                print(cores["Cinza"], frase , cores["Limpa"])
            elif sorteador == 2 and jogada == 2:
                print(cores["Cinza"], frase , cores["Limpa"])
            exit()

        itens = ["Pedra", "Papel", "Tesoura"]
        cores = {
            'Limpa':'\033[m',
            'Azul':'\033[0;34m',
            'Ciano':'\033[36m',
            'Red':'\033[31m',
            'Verde':'\033[32m',
            'Amarelo':'\033[33m',
            'Cinza':'\033[37m'
            }       
        sorteador = random.randint(0,2)
        # frase = "O número digitado não está na base de opções,porfavor digitar novamente..."
        # print(cores["Amarelo"] , frase , cores["Limpa"])

        # jogada = int(input("Digite Novamente um número que tem nas opções do game: "))

        print("JO")
        sleep(2)
        print("KEN")
        sleep(2)
        print("PO!!")

        print("="*24)

#   jogarnovamente = input("Ops , deu empate, se quiser seguir digite [Y] para Sim or [N]para Não: ")
        print(" O computador jogou %s " % cores["Verde"],itens[sorteador],cores["Limpa"])
        if jogada == 0:
             print(" O jogador jogou %s " % cores["Red"],itens[jogada], cores["Limpa"])
        elif jogada == 1:
            print(" O jogador joogu %s" % cores['Azul'],itens[jogada],cores['Limpa'])
        elif jogada == 2:
            print(" O Jogador jogou %s " % cores["Ciano"],itens[jogada],cores["Limpa"])
        print("="*24)
        
#while itens[sorteador] == itens[jogada]:
#    jogarnovamente = input("Ops , deu empate, se quiser seguir digite [Y] para Sim or [N]para Não: ")
# Condição de vitória ou empate e 
        if sorteador == 0: # o computador escolheu Pedra
            if jogada == 1:
                print("Jogador VENCEU")
            elif jogada == 2:
                print("O Computador VENCEU")
        if sorteador == 1:
            if jogada == 0:
                print("Computador VENCEU")
            elif jogada == 2:
                print("Computador VENCEU")
        if sorteador == 2:
            if jogada == 0:
                print("Jogador VENCEU")
            elif jogada == 1:
                print("Computador VENCEU")
        frase = "WOW, Temos um EMPATE" 
        if sorteador == 1  and jogada == 1:
            print(cores["Cinza"], frase , cores["Limpa"])
        elif sorteador == 0 and jogada == 0:
            print(cores["Cinza"], frase , cores["Limpa"])
        elif sorteador == 2 and jogada == 2:
            print(cores["Cinza"], frase , cores["Limpa"])

Game_jokenpo()