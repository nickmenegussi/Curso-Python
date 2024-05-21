import math

print("Digite um número para")

fatorial = int(input("Calcular o seu fatorial:"))

print("Calculando %d ! = "% fatorial, end="")
for c in range(fatorial, 0 , -1): 
   calcu = math.factorial(fatorial)
   print("%d x " % (c), end="")
print("= %d  " % (calcu))
