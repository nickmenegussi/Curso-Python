# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def linha():
    print("\033[1;34m=\033[m"*25)

def ficha(nome= '' ,gols= 0):
    try:
        nome = str(input("Nome do jogador: "))
        gols = int(input(f"Quantos gols o {nome} fez? "))
    except (TypeError,ValueError):
        nome = '<desconhecido>'
        gols = 0
    return f'O jogador {nome} fez {gols} gols no campeonato.'

print(ficha())
