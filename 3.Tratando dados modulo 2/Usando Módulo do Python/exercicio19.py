from random import choice


aluno_1 = input("Primeiro aluno: ")
aluno_2 = input("Segundo aluno: ")
aluno_3 = input("Terceiro aluno: ")
aluno_4 = input("Quarto aluno: ")

lista = [aluno_1, aluno_2, aluno_3 , aluno_4]

sorteio = choice(lista) #choice escolher algum coisa da lista

print("O aluno selecionado foi %s "% sorteio)