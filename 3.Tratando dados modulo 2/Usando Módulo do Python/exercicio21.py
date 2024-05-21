import pygame

# iniciando o pygame
pygame.init()
# caminho onde esta o arquivo
pygame.mixer.music.load("C:/Users/PC/Desktop/Meu cu sujinho/Slightly Hung Over.mp3")
pygame.mixer.music.play()
# sai somente quando acabar a música
pygame.event.wait()
