import pygame
import random
import sys



def main():
    pygame.init()
    pygame.display.set_caption("A Day with Temoc")
    fullscreen = False
    resolution = (1920, 1080)
    screen = pygame.display.set_mode (resolution, pygame.RESIZABLE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('Orange')
        pygame.display.flip()
    pygame.quit


if __name__=="__main__":
    main()
