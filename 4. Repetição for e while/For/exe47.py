cor = {
    'Limpa':'\033[30m',
    'azul':'\033[34m',
    'Amarelo':'\033[33m'
}

final = "Acabou, parabéns voce acertou quais eram os numeros pares!!"



print("======== Menu de Opções PAR E ÍMPAR ========\n[ P ] Para saber os de pares \n[ I ] Para saber os de ímpares")

opção = input("Informe sua opcao: ").strip().capitalize()

for x in range(0, 52):
    if opção == "P":
        if  x % 2 == 0:
            print(cor['azul'],x,cor['Limpa'])
    if opção == "I":
        if x % 2 == 1:
            print(cor['Amarelo'],x,cor['Limpa'])
print("Acabou")
