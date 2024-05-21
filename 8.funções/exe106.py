# fazer de novo

"""Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra FIM, o programa se encerrará. Importante: use cores."""
from time import sleep

def mensagem(msg):
    tamanho_msg = len(msg) + 4
    print("\033[7;34m=\033[m"* tamanho_msg)
    print(f" {msg}")
    print("\033[7;34m=\033[m"* tamanho_msg)

def Pyhelp(manual):
    manual = help(manual)
    return manual


# Programa princial
while True:
    print("Sistema de ajuda Pyhelp!")
    opcao = input("Função ou biblioteca > ")
    if opcao in 'Fimfim':
        break
    else:
        mensagem(f"Acessando o modulo {opcao}")
        sleep(1)
        Pyhelp(opcao)
mensagem("Até logo")