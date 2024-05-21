n = int(input("Digite um numero inteiro: "))

opção = int(input("""Qual é a conversão que será a escolhida da base de conversão\n[1] Converter para binário\n[2] Converter para octal\n[3] Converter para hexadecimal\nSua opção: """))

if opção == 1:
    print("%d convertido para Binário é igual a %s " %(n , bin(n)))
elif opção == 2:
    print("%d convertido para Octal é igual a %s " %(n, oct(n)))
elif opção == 3:
    print("%d convertido para Hexadecimal é igual a %s " %(n, hex(n)))
else:
    print("Número inválido, Por favor informe o numero com base na tabela.")