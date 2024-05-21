n = input("Digite seu nome completo: ").strip()
nome = n.split()

print("O seu primeiro nome é %s\ne seu segundo nome é %s" % (nome[0],nome[len(nome)-1]))