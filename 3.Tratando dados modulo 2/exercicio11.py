Largura = float(input("Digite a largura da parede: "))
Altura = float(input("Digite a altura da parede:  "))

area = Largura * Altura
tinta = area / 2

print("Sua parede tem a dimensão de %.2f x %.2f e sua area é de %.2fm². \n Para pintar a parede, voce precisará de %.2f l tinta"%(Largura, Altura, area, tinta))