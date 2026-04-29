from PIL import Image
import pygame
import sys
import os

# function for adding/loading UI and background to screen
# function for adding temoc sprites
# function for each dialogue branching systems or pathways
#display dialogue/text function? 




directory = os.path.dirname(os.path.abspath(__file__))
temoc_path = os.path.join(directory, "assets", "temoc_content.bmp")
textbox_path = os.path.join(directory, "assets", "text_box.bmp")

def main():  
    pygame.init()
    pygame.image.get_extended()
    pygame.display.set_caption("A Day with Temoc")
    fullscreen = False
    resolution = (1920, 1080)
    screen = pygame.display.set_mode (resolution, pygame.RESIZABLE)
    textbox = pygame.image.load(textbox_path)
    image = pygame.image.load(temoc_path)
    box_width, box_height = textbox.get_size()
    new_box_width = box_width//1.7
    new_box_height = box_height //1.7
    new_box = pygame.transform.smoothscale(textbox,(new_box_width, new_box_height))
    width, height = image.get_size()
    new_width = width//2.7
    new_height = height//2.7
    new_image = pygame.transform.smoothscale(image,(new_width ,new_height))
    running = True
    while running:
        screen.fill('Black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(new_box,(230,400))
        screen.blit(new_image,(0,230))
        pygame.display.flip()
    pygame.quit
    sys.exit()



if __name__=="__main__":
    main()
