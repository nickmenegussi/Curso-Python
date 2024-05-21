from datetime import date

nascimento = int(input("Infome seu ano de nascimento: "))
ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print("O Atleta tem %d\nClassificação: MIRIM" % idade)
elif idade <= 14:
    print("O Atleta tem %d.\nClassificação: INFANTIL" % idade)
elif idade <= 19:
    print("O Atleta tem %d anos.\nClassificação: JÚNIOR" % idade)
elif idade <= 25:
    print("O Atleta tem %d anos.\nClassificação: SENIOR" % idade)
else:
    print("O Atleta tem %d anos.\nClassificação: MASTER" % idade)