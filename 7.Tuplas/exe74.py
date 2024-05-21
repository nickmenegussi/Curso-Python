"Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."

import random

numeros = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10) , random.randint(0,10))

print(f"Foram sorteados os seguintes números: ", end="")
for aleatorios in numeros:
    print(f"{aleatorios}", end=" ")

print(f"\nO Maior valor sorteado foi: {max(numeros)}")
print(f"O Menor valor sorteado foi: {min(numeros)}")