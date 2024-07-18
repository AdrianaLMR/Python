# Faça um programa em python que abre e reproduza áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('exercicios21.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
        continue
