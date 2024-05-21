valorcasa = float(input("Infome o valor da casa: R$ "))
salariocomprador = float(input("Informe seu salário: "))
financiamento = int(input("Quantos anos deseja financiar? "))
prestacao = valorcasa / (financiamento * 12) # descobrir o financiamento em quantos anos ele pagará
minimo = salariocomprador * 30 / 100



if prestacao >= minimo:
    print("Empréstimo negado!")
else:
    print("Empréstimo pode ser Concedido!!")

print("Para pagar uma casa de %.2f em %d anos a será de prestação de %.2f " %(valorcasa,financiamento, prestacao))