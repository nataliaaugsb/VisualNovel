from PIL import Image
import pygame
import sys
import os

# function for adding/loading UI and background to screen
# function for adding temoc sprites
# function for each dialogue branching systems or pathways
#display dialogue/text function? 

pygame.init()
pygame.image.get_extended()
pygame.display.set_caption("A Day with Temoc")
fullscreen = False
resolution = (1920, 1080)
screen = pygame.display.set_mode (resolution, pygame.RESIZABLE)


directory = os.path.dirname(os.path.abspath(__file__))
textbox_path = os.path.join(directory, "assets", "text_box.bmp")
bg_path = os.path.join(directory, "assets", "background.bmp")
response_path = os.path.join(directory,"assets", "response_box.bmp")

directory = os.path.dirname(os.path.abspath(__file__))
expression = {"disgust": os.path.join(directory, "assets","temoc_disgust.bmp"),
        "happy": os.path.join(directory,"assets","temoc_happy.bmp"),
        "worried": os.path.join(directory, "assets","temoc_worried.bmp"),
        "content" : os.path.join(directory, "assets","temoc_content.bmp")}


def load_scale(path,scale):
    img = pygame.image.load(path).convert_alpha()
    w,h = img.get_size()
    return pygame.transform.smoothscale(img,(int(w/scale), int(h/scale)))

def main():  
    background = load_scale(bg_path,1.5)
    response = load_scale(response_path,4)
    textbox = load_scale(textbox_path, 1.7)
    temoc_imgs = {key: load_scale (path, 2.7)
                  for key, path in expression.items()}
    load_scale(expression["happy"], 2.7)
    font = pygame.font.Font(None,60)
    dialogue = [
        ("Welcome to UTD!", "happy"),
        ("My name is Temoc! Let me show you around!", "content"),
        ("Where would you like to go first?", "content")
    ]

    library_dialogue = [
        ("Awesome! Let's check out the library!", "happy"),
        ("It's the perfect place to study and take a nap!", "content"),
        ("I hope I can pass my chemistry exam this Friday!", "worried")
    ]

    cafeteria_dialogue = [
        ("Great choice! Let's head over to the dining hall!", "happy"),
        ("I love the pizza here!", "content"),
        ("My friend Enarc likes pineapple pizza, gross!", "disgust")
    ]

    index = 0
    current_expression = dialogue[index][1]

    show_choices = False

    library_rect = pygame.Rect(1150, 450, 300, 60)
    dining_rect = pygame.Rect(1150, 530, 300, 60)

    running = True
    while running:
        screen.fill('Black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not show_choices:
                    if index < len(dialogue) -1:
                        index += 1
                        current_expression = dialogue[index][1]
                    else:
                        show_choices = True

                else: 
                    mouse_pos = pygame.mouse.get_pos()

                    if library_rect.collidepoint(mouse_pos):
                        dialogue = library_dialogue
                        index = 0
                        current_expression = dialogue[index][1]
                        show_choices = False
                    elif dining_rect.collidepoint(mouse_pos):
                        dialogue = cafeteria_dialogue
                        index = 0
                        current_expression = dialogue[index][1]
                        show_choices = False

        screen.blit(background, (0,0))
        screen.blit(textbox,(230,400))
        screen.blit(temoc_imgs[current_expression],(0,230))
        text = font.render (dialogue[index][0], True ,(255,255,255))
        screen.blit(text, (400, 650))

        if show_choices:
            screen.blit(response, (1100,400))
            library_text = font.render("Library", True, (255,255,255))
            cafeteria_text = font.render("Dining Hall", True, (255,255,255))
            screen.blit(library_text, (1180,460))
            screen.blit(cafeteria_text, (1180,540))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__=="__main__":
    main()

