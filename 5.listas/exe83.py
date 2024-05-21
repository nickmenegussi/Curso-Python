lista = []
aberto = fechado = 0
exepressão = input("Digite uma expressão qualquer: ")

for x in exepressão:
    if x == ("("):
        aberto += 1
    elif x == (")"):
        fechado +=1
if aberto > fechado or fechado > aberto:
    print("Está errada a expressão")
else:
    print("Está correta a expressão")
