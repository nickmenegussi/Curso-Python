"""Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
"""

def notas(*nota_aluno, sit=False):
    """ => Função para analisar e o desempenho do aluno
    :param nota_aluno: Uma ou mais nota dos alunos.
    :param sit: imprime a situação do aluno de acordo com a média dele. e valor opcional (True ou False)
    :return: dicionário com todas as informações do aluno.
    """
    # Criar uma logica em dicionarios que faz com que imprima a maior nota, menor, a media e a situacao
    while True:
        try:
            aluno = {'Nome': str(input("Nome do aluno: ")),
                     'Nota': nota_aluno,
                     'Total': len(nota_aluno),
                     'Maior': max(nota_aluno),
                     'Menor': min(nota_aluno)}
            aluno['Média'] = sum(aluno['Nota']) / aluno['Total']

            if sit: # se a sit for verdadeira, pois a situ já é Falsa
                if aluno['Média'] >= 7:
                    aluno['Situação'] = 'Boa'
                elif 6 <= aluno['Média'] >= 5:
                    aluno['Situação'] = 'Razoavel'
                else:
                    aluno['Situação'] = 'Péssima'

            return aluno
        except (ValueError, TypeError):
            print("Digite um número válido")


# Programa principal
print(notas(5.5 ,7.5 , 10, 6.7, sit=True))


# melhorar exercicio