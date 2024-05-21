n = 999
c = 0

menor = maior = d = c = s = 0
while c != n:
    n = int(input("Digite um número: "))
    opcao = input("Quer continuar? (S/N) ").strip().upper()
    d += 1
    s += n
    if d == 1: # se tiver so 1 numero digitado ele vai ser = = = ao número
        maior = menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    if opcao == "N":
        break
media = s / d
print("Voce digitou %d numeros e a media foi %.2f " % (d,media))
print("O maior valor foi %d e o menor foi %d" %(maior, menor))
    