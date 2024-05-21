dias = float(input("Quantos dias o carro foi alugado? "))
km = float(input("Digite quantos km voce percorreu: "))

pagar = ((60*dias) + km * 0.15)

print("O Total a pagar é R$%.2F" % pagar)