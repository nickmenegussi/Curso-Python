"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Coritiba."""

tabela_brasileira = ('botafogo', "palmeiras","fluminense","gremio","fortaleza","flamengo","atletico Paranaense","atletico-MG","São Paulo","cruzeiro","internacional","bragantino"
                    ,"santos","bahia","corinthians","cuiaba","goias","america mineiro","Vasco","coritiba")


print("Os 5 primeiros da tabela do brasileirão:")
for contador in range(0, len(tabela_brasileira)):
    if 0 <= contador <= 4:
        print(f"{tabela_brasileira[contador]}", end=" ")

print("\nOs 4 ultimos colocados da tabela são: ")
print(tabela_brasileira[-4:])

print("Os times em ordem alfabetica são: ")
print(sorted(tabela_brasileira))

print("Posicao do coritiba: ")
print(tabela_brasileira.index('São Paulo') + 1)