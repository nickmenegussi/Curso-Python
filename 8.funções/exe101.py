# Crie um programa que tenha uma função chamada voto() 
# que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(anonascimento):
    from datetime import date

    idadeatual = date.today().year - anonascimento

    if idadeatual < 16:
        return f'Com {idadeatual} anos e é NEGADO.'
    elif 16 <= idadeatual  < 18 or  idadeatual > 65:
        return f'Com {idadeatual} anos a situação do voto é OPCIONAL'
    else:
        return f"Com {idadeatual} anos O VOTO É OBRIGATORIO."
    
print("="*21)
nascimento = int(input("Ano de nascimento: "))
print(voto(nascimento))
# refazer