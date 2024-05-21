números = []


for c in range(0, 5):
    números.append(int(input(f'Digite um valor para a posicao {c}: ')))
print("-=-"*20)
print(f"voce digitou os valores {números}")
print(f"O maior valor digitado foi {max(números)} nas posições " , end="")
for pos,contador in enumerate(números):
    if contador == max(números):
        print(f"{pos}... ", end="")
print(f"\nO menor valor digitado foi {min(números)} nas posições " , end="")
for pos,contador in enumerate(números):
    if contador == min(números):
        print(f"...{pos} ", end="")

