matriz = [[0]*3,[0]*3,[0]*3]
pares = [] # eadicionar os valores pares na lista par e depois somar

soma = maiorv=  somacoluna = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite um número para [{l}][{c}]: "))
        pares.append(matriz[l][c])
   
print('='*30)
for l in range(3):
    somacoluna += matriz[l][2] # me confundi , estava achando que era a coluna 3 e, não , era a linha 3. 
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]",end="")

    print()
print("="*30)
for x in pares:
    if x % 2 == 0:
        soma += x
print(f"\033[35mA soma dos valores pares é {soma}\033[m")
print(f"A soma dos valores da terceira coluna é {somacoluna}")
print(f'O maior valor da segunda linha é: {max(matriz[1])}') # pois a linha sempre está fixa , dai é so pegar a linha 1 que na verdade é a linha 2 e consegui resolver
# pois a unica que muda é a coluna 