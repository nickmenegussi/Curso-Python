"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta."""

# importar biblioteca
from random import sample
from time import sleep
# quantos jogos serão gerados
print("="*30)
print(F"{'JOGO DA MEGA SENA':^30}")
print("="*30)

jogada = int(input("Quantos jogos voce quer que eu sorteie?"))
# sortear 6 número em uma lista composta entre números de 1, a 60 para cara jogo

print("\033[35m-="*3,f"Sorteando {jogada} jogos" ,"-="*3,"\033[m")
for x in range(1, jogada + 1):
    sleep(1)
    print(f"\033[34mJogo {x}: {sorted(sample(range(1,61),6))}\033[m")

print("\033[36m-="*5, "< BOA SORTE! >", "-="*5,"\033[m")