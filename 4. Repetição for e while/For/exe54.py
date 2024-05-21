from datetime import date

anoatual = date.today().year

#totalmaior = 0
#totalmenor = 0

for x in range(1, 8):
    anopessoa = int(input("Em qual ano a %d ° pessoaa nasceu? " % x))
    validadorano = anoatual - anopessoa
    if validadorano <= 18:
        print("Temos ao todo  pessoas menores de idade ")
    else:
        print("Temos ao todo  pessoas maiores de idade ")

# maneira melhor de executar , usando lógica , criando um contador
# if validadorano <= 18:
#       totalmenor += 1
#    else:
#       totalmaior += 1 

#print("Temos ao total %d pessoas menores de idade e %d pessoas maiores de idade " %(totalmenor, totalmaior))