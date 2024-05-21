from math import floor

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

média =  (n1 + n2 ) / 2
arredondamento = floor(média)

if média < 5:
    print("REPROVADO")
elif média >= 5 and média < 7:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
    
print("O aluno que tirou %.1f e %.1f tem a média %.1f" %(n1, n2, média))

# > maior < menor