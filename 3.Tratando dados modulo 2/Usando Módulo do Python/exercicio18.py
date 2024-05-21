from math import radians,sin,cos, tan



a = float(input("Digite a medida de um angulo: "))
s = sin(radians(a)) # radians converte para graus
c  = cos(radians(a))
t = tan(radians(a))

print("A medida do seu angulo foi %d com base nisso as medidas de \n Seno é %.2f \n Cosseno %.2f \n Tangente %.2f "% (a, s, c, t)) 
