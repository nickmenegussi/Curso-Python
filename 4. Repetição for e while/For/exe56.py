somaidade = 0
nomevelho = " "
idadevelho = 0
mulher = 0

analisadordeidentidades = int(input("Digite quantas pessoas deseja analisar a identidad: "))

for x in range(1, analisadordeidentidades + 1):
    print("--------- %d° Pessoa ---------" % x)
    nome = input("Nome: ").strip().capitalize()

    # Pedindo a idade do usuário
    idade = int(input("Idade: "))
    somaidade += idade
    media = somaidade / 4

    # Pedindo o sexo do usuário
    sexo = input("[F/H]: ").upper().strip ()

    if "H" in sexo:
       if idade > 50:
            idadevelho = idade
            nomevelho = nome
    if "F" in sexo:
        if idade < 20:
            mulher += 1

print("A média de idade do gp é %.1f\no homem mais velho tem %d e o nome dele é %s\nAo todo são %d mulheres com menos de 20 anos "% (media,idadevelho, nomevelho,mulher))