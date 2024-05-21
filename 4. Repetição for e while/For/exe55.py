"""from time import sleep

obesidade = 0
sobrepeso = 0
pesoideal = 0
pesoabaixo = 0
obesidademorbita = 0

print("==================== Tabela para saber seu peso e da sua familia ====================")
print("Para saber isso precisaremos tambem que coloque a altura da pessoa.")


familia = int(input("Quantos membros da familia voce quer saber o peso? "))

for X in range(1, familia + 1):
    peso = float(input("Qual é o peso da %d° pessoa?  " % X))
    altura = float(input("Qual é a altura da %d° pessoa? " % X))
    calculo = peso / (altura * altura)

    if calculo < 18.5:
        pesoabaixo += 1
    elif calculo >= 18.5 and calculo <= 25:
        pesoideal += 1
    elif calculo >= 25 and calculo <=30:
        sobrepeso += 1
    elif calculo >= 30 and calculo <= 40:
        obesidade += 1
    else: 
        obesidademorbita += 1

print("analisando.... conforme os dados informados, faremos uma média de qnts pessoas estao em alto peso , baixo peso, sobrepeso , peso ideal e obesidade mórbita")
sleep(2)

print("%d com baixo peso , %d pessoas com peso ideal , %d pessoas com sobrepeso , %d pessoas com obesidade e %d pessoas com obesidade mórbita" 
    % (pesoabaixo, pesoideal, sobrepeso, obesidade, obesidademorbita))"""

