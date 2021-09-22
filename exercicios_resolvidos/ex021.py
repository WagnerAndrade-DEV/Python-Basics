import pygame

pygame.init()
pygame.mixer.music.load('caminho_do_arquivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()
