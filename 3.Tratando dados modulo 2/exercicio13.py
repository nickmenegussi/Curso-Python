salário_funcionário = float(input("Digite seu salário como funcionário: R$ "))
aumento = salário_funcionário + ((salário_funcionário * 15) / 100)

print("Seu salário antes do aumento era R$%.2f, com o aumento passou a ficar %.2f" % (salário_funcionário, aumento))