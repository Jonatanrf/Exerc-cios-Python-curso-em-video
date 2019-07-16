import pygame
print('REPRODUÇÃO DE AUDIO')
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()


