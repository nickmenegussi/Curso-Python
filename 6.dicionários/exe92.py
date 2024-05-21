""": Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO
,o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""
from datetime import date


# 1. CRIAR UM PROGRAMA QUE LEIA NOME,ANO DE NAS, CARTEIRA DE TRABALHO
dict = {}
dict["nome"] = input("Nome: ")
anonas = int(input("Ano em que nasceu: "))
dict["carteiradetab"] = int(input("Carteira de Trabalho (0 não tem): "))
dict["idade"] = date.today().year - anonas
dict["Sexo"] = input("Sexo: (M/F) ")

print("="*40)
if dict["carteiradetab"] != 0:
    dict["Ano de contratação"] = int(input("Ano de contratação: "))
    dict["Salario"] = float(input("Salário: R$ "))
    dict["Aposentadoria"] = dict["Ano de contratação"] + 40 - anonas
for k , v in dict.items():
    print(f" - {k} tem o valor {v}")
if dict["Sexo"] in "Mm" and dict["idade"] >= 65:
    print(f"Pode se aposentar! pois tem {dict['idade']} anos.")
    if dict["Sexo"] in "Ff" and dict["idade"] >= 60:
        print(f"Pode se aposentar!Pois tem {dict['idade']} anis")
else:
    if dict["idade"] <= 65:
        print(f" - Voce ainda não pode se aposentar. pois tem {dict['idade']} ano.")
