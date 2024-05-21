"""Crie um programa que tenha a função leiaInt(), que vai funcionar
de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)"""

def leiaInt(numero):
    while True:
        try:
            numero = input("Digite um número: ")
            validar = False
            if numero == int(numero): # se o numero for um número inteiro , validadaro = True
                validar = True
            else: # senao
                if validar: # se o validador for False breaj
                    break
            return numero
        except (TypeError, ValueError):
            print("\033[1;31mErro, por favor digite um número inteiro válido.\033[m")

# Programa Principal
n = leiaInt("Digte um número: ")
print(f"\033[1;34mVoce digitou o número {n}\033[m!")