s = 0
c = 0
for x in range(1, 7):
    num = int(input("Digite o seu %d número: " % x))
    if num % 2 == 0:
        s += num
        c += 1
print("Vimos que em %d  número pares  a soma desses número são %d " % (c, s))