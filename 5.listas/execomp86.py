matriz = [[0]*3,[0]*3,[0]*3]

# Primeiro for para colocar elementos dentro da lista
for l in range(3): # imprimir a  3 linha
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um número para [{l}] [{c}]: ")) # pegou a linha e a coluna e jogou os valores dentro

# Segundo for para botar as colunas em ordem
for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^6}]", end="") # imprimir a matriz em ordem
    print() # quebrar a linha