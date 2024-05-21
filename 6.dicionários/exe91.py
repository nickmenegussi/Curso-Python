""" Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep

""" `key=lambda item: item[1]' faz com o sort seja feito a partir dos valores que os jogadores obtiveram. 
Se quiser fazer com as chaves ao invés dos valores, use item[0]. Assim não precisar importar e fazer uso do itemgetter."""
# 1. sortear um numero de 1 a 6 aleatorio , para 4 jogadores e Guardar resuls em dict
dict = {"Jogador1":randint(1,6),
    "Jogador2":randint(1,6),
    "jogador3":randint(1,6),
    "jogador4":randint(1,6)}
ranking = sorted(dict.items(), key=lambda item: item[1], reverse=True)
# 3. no final colocar o dict em ordem para ver quem foi o vencer do maior numero gerado
for k, v in dict.items():
    print(f"\033[34m{k} tirou {v} no dado.\033[m")
    sleep(1)
print("-="*30)
print("  ==","RANKING DOS JOGADORES", "==")
for i , v in enumerate(ranking):
    print(f"   {i + 1}° lugar: {v[0]} com {v[1]}")
    sleep(1)
