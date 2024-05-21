from math import hypot
# from math import sqrt

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adajcente = float(input("Digite o valor do cateto adjacente: "))
hi = hypot(cateto_oposto,cateto_adajcente)
# h2 = sqrt(cateto_oposto * cateto_oposto + cateto_adajcente * cateto_adajcente) # formula e automaticament calcula raiz quadrada

print("A hipotenusa vai medir %.2f"% h1)