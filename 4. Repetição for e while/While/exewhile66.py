n = d = s = 0


while n != 999:
    n = int(input("Digite um numero (999 para parar): "))
    if n == 999:
        break
    d += 1
    s += n # vai somar so quando  o programa acabar
print("Foram %d digitados e a soma deles foram %d" % (d,s))