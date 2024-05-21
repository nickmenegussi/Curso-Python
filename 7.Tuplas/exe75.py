""" Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""

n1 = int(input("Digite seu primeiro numero: "))
n2 = int(input("Digite seu segundo numero: "))
n3 = int(input("Digite seu terceiro numero: "))
n4 = int(input("Digite seu quarto numero: "))


numeros_finais = (n1, n2, n3 , n4)

if 3 in numeros_finais:
    print(f"O valor 3 apareceu na {numeros_finais.index(3) + 1} posição")
else:
    print("O valor 3 não foi encontrado ou não foi digitado.")

print(f"O valor 9 apareceu {numeros_finais.count(9)} vezes")
print(f"Os valores pares digitados foram: ", end=" ")
for par in numeros_finais:
    if par % 2 == 0:
        print(f"{par}", end=" ")
