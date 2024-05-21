# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

# 1. Ler nomes, sexo e idade de varias pessoas, guardando em um dicionario e todos os dicionários em uma lista 
# 2.e Fazer um loop caso tenhas respostas erradas em 'sexo' , 'resposta' e 'idade'
dict = {}
pessoas = []

soma =  0

while True:
    dict["Nome"] = input("Nome: ").strip() 
    dict["Sexo"] = str(input("Sexo: (M/F) ")).strip()
    while dict["Sexo"] not in 'MmFf':
        print("\033[34mERRO! Digite um sexo valido. M Ou F \033[m")
        dict["Sexo"] = input("Sexo: (M/F) ").strip()
        if dict["Sexo"] in 'MF':
            break
    dict["Idade"] = int(input("Idade: "))
    while dict["Idade"] <= 0:
        print("\033[36mErro! Digite algum número maior que 0\033[m")
        dict["Idade"] = int(input("Idade: "))
        if dict["Idade"] >= 0:
            break
    soma += dict["Idade"]
    pessoas.append(dict.copy())
    r = input("Deseja continuar? [S/N] ")

    while r not in 'SsNn':
        print("\033[34mErro! Digite uma opção valida. [S/N]\033[m")
        r = input("Deseja continuar? [S/N] ")
    if r in "Nn":
        break
media = soma / len(pessoas)  
# 3. A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média


print("="*50)
print(f" => A) Ao todo foram cadastradas {len(pessoas)} pessoas. ")
print(f" => B) A Média de idade é de {media:.1f} anos")
print(f" => C) As mulheres cadastradas foram " , end="")
for p in pessoas:
    if p['Sexo'] in "Ff":
        print(f" {p['Nome']}") 
print(f" => D) Lista das pessoas que estão acima da média:")
for p in pessoas:
    if p['Idade'] >= media: # tem que ser aqui o verificador das pessoas acima da média pois vai iterar sobre elas
        for k,v in dict.items(): # aqui já não , pois da erro de string nao iteravel , pois so vai imprimir os valores do dicionario
            print(f" {k}; {v} " , end="")
        print()

print("Encerrando...")