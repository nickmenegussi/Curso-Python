produto = float(input("Digite o preço do produto desejado:R$ "))
desconto = produto - ((produto * 5) /100)

print("O produto que custava R$%.2f, na promoção com 5porcento de desconto passa a ser R$%.2f "% (produto, desconto))