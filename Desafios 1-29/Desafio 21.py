import pygame

# Inicializar o mixer do pygame
pygame.mixer.init()

# Carregar e tocar a música
pygame.mixer.music.load('/Users/Mac_Nathan/Desktop/Phyton/Recuerdame.mp3')
pygame.mixer.music.play()

# Manter o programa rodando enquanto a música toca
input("Pressione Enter para parar...")