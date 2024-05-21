"""Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quize','dezesseis','dezessete','dezoito','dezenove','vinte')

n = int(input("Digite um numero entre 0 e 20: "))

while n > 20:
    n = int(input("Tente Novamente. Digite um numero entre 0 e 20: "))
    if n == 20 or n <= 20:
        break

print(numeros[n])