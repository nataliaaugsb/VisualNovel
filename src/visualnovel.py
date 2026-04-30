from PIL import Image
import pygame
import sys
import os

# function for adding/loading UI and background to screen
# function for adding temoc sprites
# function for each dialogue branching systems or pathways
#display dialogue/text function? 



directory = os.path.dirname(os.path.abspath(__file__))
textbox_path = os.path.join(directory, "assets", "text_box.bmp")
bg_path = os.path.join(directory, "assets", "background.bmp")

directory = os.path.dirname(os.path.abspath(__file__))
expression = {"disgust": os.path.join(directory, "assets","temoc_disgust.bmp"),
        "happy": os.path.join(directory,"assets","temoc_happy.bmp"),
        "worried": os.path.join(directory, "assets","temoc_worried.bmp"),
        "content" : os.path.join(directory, "assets","temoc_content.bmp")}



def main():  
    pygame.init()
    pygame.image.get_extended()
    pygame.display.set_caption("A Day with Temoc")
    fullscreen = False
    resolution = (1920, 1080)
    screen = pygame.display.set_mode (resolution, pygame.RESIZABLE)
    font = pygame.font.Font(None,60)
    text = font.render ("Welcome to UTD!", True ,(255,255,255))
    background = pygame.image.load(bg_path)
    textbox = pygame.image.load(textbox_path)
    temoc = expression["happy"]
    img = pygame.image.load(temoc)
    bg_width, bg_height = background.get_size()
    new_bg_width = bg_width//1.5
    new_bg_height = bg_height//1.9
    new_bg = pygame.transform.smoothscale(background,(new_bg_width, new_bg_height))
    box_width, box_height = textbox.get_size()
    new_box_width = box_width//1.7
    new_box_height = box_height //1.7
    new_box = pygame.transform.smoothscale(textbox,(new_box_width, new_box_height))
    width, height = img.get_size()
    new_width = width//2.7
    new_height = height//2.7
    new_image = pygame.transform.smoothscale(img,(new_width ,new_height))
    running = True
    while running:
        screen.fill('Black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(new_bg, (0,0))
        screen.blit(new_box,(230,400))
        screen.blit(new_image,(0,230))
        screen.blit(text, (400, 650))
        pygame.display.flip()
    pygame.quit()
    sys.exit()





if __name__=="__main__":
    main()
