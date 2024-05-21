n = d = s = 0 # pois todos sao zero

n = int(input("Digite um número [999 para acabar]: "))
while n != 999:
    d += 1
    s += n
    n = int(input("Digite um número [999 para acabar]: ")) # depois que acabar tudo se o numero for 999 o flag vai sair pois 
print("Foram %d digitados e a soma deles foram %d" % (d,s))