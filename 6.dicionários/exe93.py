#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas(len) partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# 1. ler o nome do jogador e quantas prtidas ele jogou. ALT + 62
futebol = {}

futebol["Nome"] = input("Nome do jogador: ").capitalize().strip()
futebol["Partidas"] = int(input(F"Quantas partidas {futebol['Nome']} jogou: "))
lista_gols = []

# 2. Ler a quantidade de gols feito em cada partida e vai guardar tudo isso em um dicionario incluindo o total de gols feito durante o campeonato
for x in range(1, futebol["Partidas"] + 1):
    golpartida = int(input(f"Quantos gols na partida {x}? "))
    lista_gols.append(golpartida)
    futebol["Gols por partida"] = lista_gols
    futebol["Total Gols"] = sum(lista_gols)
print("="*100)
print(futebol)
print('='*100)
for k , v in futebol.items():
    print(f" - o campo {k} tem o valor {v}")
print("="*100)
print(f"O jogador {futebol['Nome']} jogou {futebol['Partidas']} partidas.")

for i , j in enumerate(lista_gols):
    print(f"  -> Na partida {i + 1}, fez {j} gols.")

print(futebol)
print(lista_gols)