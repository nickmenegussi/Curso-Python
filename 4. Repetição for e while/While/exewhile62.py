# revisar exercicio

#import pygame

#def tocar():
#    pygame.init()
#    pygame.mixer.music.load("C:/Users/PC/Desktop/Meu cu sujinho/Slightly Hung Over.mp3")
#    pygame.mixer.music.play()
#    input()
#   pygame.event.wait(10)

print("-"*20)
print("   Gerador de PA")
print("-"*20)

primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

termo = primeiro
c = 1
pf = 0
total = 0
mais = 10

while mais != 0:
    total = total + mais # apartir de 10 ele vai contar os proximos termos
    while c <= total:
        print("%d → " % termo, end="")
        termo += razao
        c += 1
    print("Pause")
    novonum = int(input("Digite outro termo que quer saber: "))
print("AO todo foram %d termos mencionados " %total )

   

#       primeiro = int(input("Deseja ver quantos novos termos: "))
 #       if primeiro != 0:
 #           termo += razao
 #           c += 1
  #          print("%d → " % termo, end="")
  #      else:
  #          pf += 1
  #          print("Ao todo a sua progressão de PA contou com %d termos mostrados." % pf)