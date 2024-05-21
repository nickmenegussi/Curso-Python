def menu():
    print("="*30)
    print("Controle de terrenos".center(30))
    print("="*30)

def area(): # e tem a forma de area(largura, comprimento) , com os valores inbutido na função ja
    menu()
    try:
        largura = int(input("Largura (M): "))
        comprimento = float(input("Comprimento (M): "))
        calculo = largura * comprimento
    except (ValueError, TypeError):
        print(f"Erro encontrado nos tipos de dados inserido")
    except UnboundLocalError: # podem ter varios execpt seja especificando erro ou nao
        print("Erro , encontramos o erro no qual o valor inserido está errado.")
    else:
        print(f"A área de um terrenno {largura:.1f} é de {calculo}m². ")
    finally:
        print("Volte sempre!!")


# dessa forma = area(largura="", comprimento=" ") que voce vai pasar o parametro na area
# E tem dessa forma
area()