valores = [[],[]] # tambem da pra criar uma lista dentro da outras com isso

for x in range(1,8):
    num = int(input(f"Digite {x} valor: "))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
print(f"Os números pares foram {valores[0]}")
print(f"Os números pares foram {valores[1]}")


# fazer amanhã, fazer agen