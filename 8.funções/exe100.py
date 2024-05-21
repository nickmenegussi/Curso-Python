# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.~
from random import randint

def sorteia(lista):
    print("Sorteando 5 valores da lista: ", end="")
    c = 0
    while c < 5:
        lista.append(randint(1,15))
        c += 1
    print(f"{lista}" , end=" ")
    print("PRONTO!!")

def somapar(lista):
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f"Somando os valores pares de {lista} , temos {soma}")

# Programa principal
numeros = [] # para facilitar o programa , chamaremos a lista com nome igual a numeros fora do def
sorteia(numeros)
somapar(numeros)


# REVER