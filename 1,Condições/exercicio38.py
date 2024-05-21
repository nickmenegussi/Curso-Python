num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

if num1 > num2:
    maior = num1
    print("O Primeiro valor é maior")
elif num2 > num1:
    maior = num2
    print("O Segundo valor é maior")
else:
    print("Os dois valores são iguais")