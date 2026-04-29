from PIL import Image
import pygame
import sys
import os



def main():  
    pygame.init()
    pygame.image.get_extended()
    pygame.display.set_caption("A Day with Temoc")
    fullscreen = False
    resolution = (1920, 1080)
    screen = pygame.display.set_mode (resolution, pygame.RESIZABLE)
    filename = "temoc_happy.bmp"
    image = pygame.image.load(filename)
    width, height = image.get_size()
    new_width = width//3.5
    new_height = height//3.5
    new_image = pygame.transform.smoothscale(image,(new_width ,new_height))
    running = True
    while running:
        screen.fill('Black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(new_image, (0,-5))
        pygame.display.flip()
    pygame.quit
    sys.exit()



if __name__=="__main__":
    main()
