frase = input("Digite uma frase: ").strip().upper()

print("A letra A aparece %d vezes na frase.\nA primeira letra A aparece na posição %d\nA última letra A aparecebeu na posição %d "%
    (frase.count("A"), frase.find("A")+1, frase.rfind("A")+1)) # adicionar o mais 1 pois esta pedindo na posiçao que agente ve normal , nao na do computador
