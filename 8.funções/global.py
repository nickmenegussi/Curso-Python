# Programa Teste
def teste(b):
    global a
    a = 10 # programa de escopo local
    b += 5
    c = 4
    print(f"Dentro o valor de a é {a}")
    print(f"Dentro o valor de b é {b}")
    print(f"Dentro o valor de b é {c}")

# Programa principal
a = 4 # global
teste(a)
print(f"O valor de fora de a é {a}")
print(f"O VALOR de fora de b é (b)") # erro pois a variavel b está no escopo local , 