print("-"*12)
print("Sequencia Fibonacci")
print("-"*12)

c = 3 # por que  ja mostre o 1 e o 2 termo entao vou começar no 3
termo = int(input("Quantos termos voce quer mostrar? "))

num1 = 0
num2 = 1

print("%d → %d" %(num1, num2), end="")

while c <= termo:
    soma = num1 + num2
    print(" → %d" % (soma), end="")
    num1 = num2
    num2 = soma
    c += 1
print(" → FIM")


# fazer de