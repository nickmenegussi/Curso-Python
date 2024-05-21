s = 0
c = 0

cores = {
    "Limpa":"\033[m",
    "Azul":"\033[34m"
}

for n in range(1, 501):
    if n % 2 == 1:
        if n % 3 == 0:
            c += 1
            s += n
print("A soma  de todos os %d valores solicitado é  resultado é %d " % (c,s))
    