print("-"*25)
print("Cadastro de Pessoas")
print("-"*25)

opcao = "S"

maior18 = homens = mulheresmenos20 = 0


while opcao != "N" and opcao != "n":
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ")
    opcao = input("Deseja continuar [S/N]: ")
    if idade > 18:
        maior18 += 1
    if sexo == "M":
        homens += 1
    if sexo == "F":
        if idade < 20:
            mulheresmenos20 += 1
print("Total de pessoas com mais de 18 anos: %d\nAo todo temos %d homem cadastrado\nE temos %d mulheres com menos de 20" %(maior18,homens,mulheresmenos20))
