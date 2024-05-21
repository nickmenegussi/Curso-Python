def escreva():
    while True:
        msg = input("Mensagem: ")

        tamanho = len(msg) + 4
        print("="*tamanho)
        print(f"{msg.center(tamanho)}")
        print("="*tamanho)

        r = input("Deseja continuar? [S/N]: ")
        while r not in "SsNn":
            r = input("Deseja continuar? [S/N]: ")
        if r in "Nn":
            break

escreva()