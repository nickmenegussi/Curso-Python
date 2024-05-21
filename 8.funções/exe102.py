# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

fat = 1 # fatorial

def fatorial(n, show=False):
    from math import factorial
    """
    ==> Calcula o fatorial de um n:
    :param n: O número a ser calculado
    :param show: Parametro(OPCIONAL) onde o usuario vai escolher se mostra a conta ou nao
    :retrun: O valor do fatorial do numero pedido
    """
    fat = n # o fatorial vai ser igual ao n
    print("="*25)
    print(f"O calculo do fatorial do número {n}: ", end="")
    while fat > 0:
        if show == True:
            print(fat, end="")
            if fat > 1: # se o fatorial for maior que 1 imprimir x e depois quando chegar em 1 imprimir =
                print(" x ", end="")
            else:
                print(" = " , end="")
        fat -= 1 
        cal = factorial(n)
    return cal

print(fatorial(8))

""" ------ Outra opcao tambem -----
n = int(input("Digite um numero para calcular o seu fatorial: "))

fato = 1

for x in range(n,0 ,- 1):
    print(x, end=" ")
    if x > 1:
        print(">" , end=" ")
    else:
        print("=", end=" ")
    fato *= x
print(fato)
"""