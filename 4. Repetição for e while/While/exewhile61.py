print("-"*20)
print("   Calculando PA")
print("-"*20)

p1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))

pt = p1

c = 1

while c <= 10:
    print("%d " % pt ,end="→ ")
    pt += r
    c += 1
print("FIM")