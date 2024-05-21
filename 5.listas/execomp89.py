""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

# 1. Ler 1 nome e duas notas de vários alunos com loop, tambem a opção do usuario se quer continuar
from time import sleep

desempenho = []
lista = []

while True:
    nome = input("Nome do usuário: ").capitalize().strip()
    nota1 = float(input("Nota1: "))
    nota2 = float(input("Nota2: "))
    média = (nota1 + nota2) / 2
    res = input("Quer continuar? (S/N)").strip()

    lista += [nome,[nota1,nota2,],média]
    desempenho.append(lista.copy())
    lista.clear()
    # 3.. Final do programa , receber um boletim com a média de cada um , e permita que o usuario possa mostrar as notas de cada aluno
    if res in "Nn":
        print("-="*20)
        break
print("     NOME      MÉDIA")
print("-"*35)
for indice , l in enumerate(desempenho):
    print(f"{indice:<4}   {l[0]:<10} {l[2]:>8.1f}")
while True:
    try:
        aluno = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
        if aluno <= len(desempenho):  # ler quantos tem de caracteristica em desempenho. e vai ler esses valores , nao vai contar numeros que nao existem
            print(f"\033[36mNotas de {desempenho[aluno][0]} são {desempenho[aluno][1]}\033[m") # rever
        else:
            print(f"Número do aluno {aluno} nao existe")
    except (TypeError, ValueError, IndexError):
        print('Erro de tipo de valor.')
    else:
        if aluno == 999:
            print("\033[35mFINALIZANDO...\033[m")
            sleep(1)
            print("\033[35mVOLTE SEMPRE!\033[m")
            break 