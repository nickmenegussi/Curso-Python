n = int(input("Informe um valor: "))

unidade = n // 1 % 10 # dividir e pegar o resto
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10

print("Analisando o número digitado %d Contém\n Unidade: %d\n Dezena: %d\n Centena: %d\n Milhar: %d "%(n, unidade,dezena,centena,milhar))