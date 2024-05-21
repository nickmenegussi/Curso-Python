sexo = input("Digite seu sexo [F/M]: ").strip()


while sexo != "M" and sexo != "F":
    sexo = input("Digite novamente [F/M]: ")
    if sexo == "M":
        print("Fim")
    elif sexo == "F":
        print("FIM!! ")