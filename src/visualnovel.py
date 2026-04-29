import pygame
import random
import sys
import os

directory = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(directory, "Assets", "temoc_content.png")

print ("path", img_path)
print ("exists", os.path.exists(img_path))
print ("size", os.path.getsize(img_path))


def main():
    pygame.init()
    pygame.image.get_extended()
    pygame.display.set_caption("A Day with Temoc")
    fullscreen = False
    resolution = (1920, 1080)
    screen = pygame.display.set_mode (resolution, pygame.RESIZABLE)
    running = True
    while running:
        screen.fill('Black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit
    sys.exit()



if __name__=="__main__":
    main()
