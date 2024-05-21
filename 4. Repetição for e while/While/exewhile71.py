print("="*27)
print("  Bem-vindo ao BANCO PNZ")
print("="*27)


total = 0



while True:
    saque = float(input("Qual é o valor do seu saque? R$ "))
    cd100 = int(saque / 100)
    resto = saque % 100 # % fornece o resto da divisão


    cd50 = resto / 50 # calcular , vai pegar o resto de 100 e do saque e vai dividir por 50
    resto %= 50


    cd10 = resto / 10
    resto %= 10

    cd1 = resto / 1
    total += saque

    print("R$100 %d\nR$50 %d\nR$10 %d \nR$1 %d" % (cd100,cd50,cd10,cd1))
    
    break
    