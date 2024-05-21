# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
#from colorama import Fore
#from pyfiglet import Figlet as fg
# 1. Menu
jogadores = {}
time = []
gols = []

#palavra =  fg(font="slant")

#print(Fore.BLUE + palavra.renderText('Bem vindo!') ,end="")
print("\033[32m -> Ao programa de aproveitamento de um jogador <- \033[m ")
# 2. ler o nome do jogador e quantas prtidas ele jogou e fazer um loop perguntando se ele quer continuar.
# Ler a quantidade de gols feito em cada partida e vai guardar tudo isso em um dicionario incluindo o total de gols feito durante o campeonato
while True:
    gols.clear()
    jogadores["Nome"] = str(input("\033[32m Nome do jogador: \033[m"))
    partida = int(input(f"Quantas partidas {jogadores['Nome']} jogou? "))
    for x in range(partida):
        gols.append(int(input(f" -> Quantos gols {jogadores['Nome']} marcou na partida {x + 1}? ".center(5))))
        jogadores["Gols"] = gols.copy()
        jogadores["Total"] = sum(gols)
    time.append(jogadores.copy())
    r = str(input("Quer continuar? "))

    while r not in "SsNn":
        r = str(input("Quer continuar? "))
    if r in "Nn":
        break
print("="*56)
print("  Nome", "            Gols", "             Total")
print("-"*56)
# 3. Fazer um loop para contar os nomes e para o usuario conseguir ver o aproveitamento do jogador escolhido
for k , v in enumerate(time):
    print( k , end=" ")
    for d in v.values():
        print(f"{str(d):<18}", end="") # str(d) para poode fazer o centralizamento de 15 linhas
    print() # para quebrar a linha e deixar ela em branco
print("-"*56)
while True:
    dados = int(input("Mostrar dados de qual jogador? (999 PARA ACABAR) "))
    if dados == 999:
        break
    if dados >= len(time): # se o dado que o usuario colocou for maior do que o os indices do time imprimir erro
        print(f"ERRO, numero nao existe do jogar {dados}")
    else:
        print(f" == Levantamentos do JOGADOR {time[dados]['Nome']} == ")
        for i, j in enumerate(time[dados]['Gols']): # vai pegar na lista time onde esta armazenada as info e depois que o usuario digitar o dado vai pegar os gols
            print(f"  => No jogo {i + 1} fez {j} gols.")
    print("-"*40)
print(" >>> Volte sempre <<< ")