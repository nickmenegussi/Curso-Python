n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2: 
    print("Os segmentos acima podem FORMAR UM TRIANGULO")
    if  n1 == n2 and n1 == n3:
        print("Os segmentos acima podem formar um triangulo EQUILÁTERO")
    elif n1 == n2 or n1 == n3  or n2 == n3:
        print("Os segmentos acima podem FORMAR um triangulo ISÓSCELES")
    else:
        print("OS segmentos acima podem formar um triangulo ESCALENO")
else:
    print("Os segmentos acima nao PODEM FORMAR UM TRIANGULO")