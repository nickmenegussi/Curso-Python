from datetime import date

ano = int(input("Informe seu ano de nascimento: "))
validadordeano = date.today().year
idade = validadordeano - ano
validadoranos = date.today()


print("Quem nasceu no %d tem %d em %d" %(ano,idade, validadordeano))
if idade < 18:
    validador = 18 - idade
    validador2 = validadordeano + validador
    print("Ainda faltam %d anos para o alistamento. " %validador)
    print("Seu alistamento será em %d. " %validador2)
elif idade > 18:
    validador = idade - 18
    ano = validadordeano -  validador
    print("Voce ja deveria ter se alistado há %d anos." %validador)
    print("Seu alistamento foi em %d. " %ano)
elif idade == 18:
    print("ALISTAMENTO IMEDIATAMENTE")

