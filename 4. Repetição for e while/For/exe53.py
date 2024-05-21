frase = input("Digite uma frase: ").upper().strip()

# class Verificador_de_palíndromos:
    # def palindromio_verdadeiro

# tirar os espaços inúteis
substituir = frase.replace(" ", "")

# manipulacao de strings , fazendo uma reversao
fatiar = substituir[::-1]



# verificando se a ultima palavra é igual com a primeira
terminacao_da_frase = substituir.endswith(fatiar)

while terminacao_da_frase == False:

    print("ERRO...frase não captada")

    frase = input("Digite uma de novo frase: ").upper().strip()

    # class Verificador_de_palíndromos:
     # def palindromio_verdadeiro

    # tirar os espaços inúteis
    substituir = frase.replace(" ", "")

    # manipulacao de strings , fazendo uma reversao
    fatiar = substituir[::-1]



    # verificando se a ultima palavra é igual com a primeira
    terminacao_da_frase = substituir.endswith(fatiar)

if terminacao_da_frase == True:
    print("sao iguais pois %s é %s É UM PALINDROMO" % (substituir, fatiar))
else:
    print("o inverso de  %s e %s por isso nao sao iguais" % (substituir, fatiar))

