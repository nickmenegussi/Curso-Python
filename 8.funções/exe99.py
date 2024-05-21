# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def linha():
    print("="*30)

def maior(* num):
    linha()
    print("Analisando valores...")
    for c in num:
        print(f"{c}", end=" ", flush=True)
        sleep(0.5)
    print(f"Foram informados {len(num)} números ao todo.")
    print(f"O maior número foi {max(num)}")

maior(2,3,5,6,7,8,10,9,11,12)
maior(13,14,15)
maior(16,17,1)