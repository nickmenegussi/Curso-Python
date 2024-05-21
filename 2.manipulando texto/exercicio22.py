nome = input("Digite seu nome completo: ").strip()

letras_maiuscula = nome.upper()
letras_minuscula = nome.lower()
totalnome = nome.replace(" ", "")
acharletras = nome.split()


print("Analisando seu nome...\nSeu nome em maiusculas é %s\nSeu nome em minusculas é %s\nSeu nome no total tem %d letras\nSeu primeiro nome é %s e tem %d letras" 
    %(letras_maiuscula, letras_minuscula, len(totalnome), acharletras[0], len(acharletras[0])))
