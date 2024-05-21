peso = float(input("Informe seu peso (Kg): "))
altura = float(input("Informe sua altura (m): "))
calculo = peso / (altura * altura)

print("O (IMC) dessa pesoa é %.1f " % calculo)

if calculo < 18.5:
    print("Essa pessoa está abaixo do PESO")
elif calculo >= 18.5 and calculo <= 25:
    print("Essa pessoa está com peso IDEAL")
elif calculo >= 25 and calculo <=30:
    print("Essa pessoas está com SOBREPESO")
elif calculo >= 30 and calculo <=40:
    print("Essa pessoa está com OBESIDADE!")
else:
    print("Essa pessoa está com OBESIDADE MÓRBITA,CUIDADO!!")