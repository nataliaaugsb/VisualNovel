import pygame
import sys
import os


pygame.init()


pygame.display.set_caption("A Day with Temoc")
fullscreen = False
resolution = (500, 500)
screen = pygame.display.set_mode (resolution)
font = pygame.font.Font(None,30)
text = font.render ("hello", True ,(255,255,255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    screen.blit(text,(100,100))
    pygame.display.flip()

pygame.quit()