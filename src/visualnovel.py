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

def load_dialogues():
    return{
        "intro" : [
        ("Welcome to UTD!", "happy"),
        ("My name is Temoc! Let me show you around!", "content"),
        ("Where would you like to go first?", "content")
    ],
    
    "library" : [
        ("Awesome! Let's check out the library!", "happy"),
        ("It's the perfect place to study and take a nap!", "content"),
        ("I hope I can pass my chemistry exam this Friday!", "worried"),
        ("Where would you like to go next?", "content")
    ],

    "dininghall" : [
        ("Great choice! Let's head over to the dining hall!", "happy"),
        ("I love the pizza here!", "content"),
        ("My friend, Enarc likes pineapple pizza, gross!", "disgust"),
        ("Where would you like to go next?", "content")
    ],

    "esports" : [
        ("Cool! Follow my lead!", "happy"),
        ("This is the Esports Center!", "content"),
        ("This is where our esports teams compete!", "content"),
        ("You can also play games in between classes!", "happy"),
        ("I usually like to play Valorant!", "happy"),
        ("But...I'm not the best at the game...", "disgust"),
    ],

    "gym" : [
        ("Sweet! I can't wait!", "happy"),
        ("Welcome to the Rec center!", "content"),
        ("We have a workout room, gym, and a pool!", "content"),
        ("When using the pool make sure...", "content"),
        ("there is a lifeguard on duty!", "content"),
        ("We wouldn't want you to drown!", "worried"),
        ("We have some cool sports clubs!", "happy"),
        ("Taekwondo, Swordfighting, Fencing... ", "content"),
        ("You should check it out!", "happy")
    ],

    "atec" : [
        ("Great! Let's go to the Bass bulding!", "happy"), 
        ("This is where ATEC students have class!", "content"),
        ("They can work in the open lab!", "content"),
        ("Hopefully Maya doesn't crash again!", "worried"),
        ("Their most recent film is Kraken's Tooth", "content"),
        ("You should check it out!", "happy")
    ],

    "jsom" : [
        ("So exciting!", "happy"),
        ("This is JSOM!", "content"),
        ("This is where students can study...", "content"),
        ("Business administration, Marketing...","content"),
        ("Supply chain management, Finance...", "content"),
        ("and more!", "happy")
    ],

    }

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
   
    dialogues = load_dialogues()
    dialogue = dialogues["intro"]
    index = 0
    current_expression = dialogue[index][1]

    show_choices = False
    choice_state = None
    paused = False

    top_rect = pygame.Rect(1150, 450, 300, 60)
    bottom_rect = pygame.Rect(1150, 530, 300, 60)
    

    running = True
    while running:
        screen.fill('Black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused 
            if event.type == pygame.MOUSEBUTTONDOWN and not paused:
                if not show_choices:
                    if index < len(dialogue) -1:
                        index += 1
                        current_expression = dialogue[index][1]
                    else:
                        if dialogue == dialogues["intro"]:
                            choice_state = "intro"
                        elif dialogue == dialogues["library"]:
                            choice_state = "library"
                        elif dialogue == dialogues["dininghall"]:
                            choice_state = "dininghall"
                        show_choices = True

                else: 
                    mouse_pos = pygame.mouse.get_pos()

                    if choice_state == "intro":
                        if top_rect.collidepoint(mouse_pos):
                            dialogue = dialogues["library"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                        elif bottom_rect.collidepoint(mouse_pos):
                            dialogue = dialogues["dininghall"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                    elif choice_state == "library":
                        if top_rect.collidepoint(mouse_pos):
                            dialogue = dialogues["esports"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                        elif bottom_rect.collidepoint(mouse_pos):
                            dialogue = dialogues["gym"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False
                    
                    elif choice_state == "dininghall":
                        if top_rect.collidepoint(mouse_pos):
                            dialogue = dialogues["atec"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                        elif bottom_rect.collidepoint(mouse_pos):
                            dialogue = dialogues["jsom"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                    

        screen.blit(background, (0,0))
        screen.blit(textbox,(230,400))
        screen.blit(temoc_imgs[current_expression],(0,230))
        text = font.render (dialogue[index][0], True ,(255,255,255))
        screen.blit(text, (400, 650))

        if paused:
            pause_overlay = pygame.Surface((1920,1080))
            pause_overlay.set_alpha(180)
            pause_overlay.fill((0,0,0))

            screen.blit(pause_overlay, (0,0))

            pause_text = font.render("PAUSED", True, (255,255,255))
            continue_text = font.render("Press P to Resume", True, (255,255,255))
            screen.blit(pause_text, (700,300))
            screen.blit(continue_text, (600,400))

        if show_choices:
            screen.blit(response, (1100,400))
            if choice_state == "intro":
                top_text = "Library"
                bottom_text = "Dining Hall"
            elif choice_state == "library":
                top_text = "Rec Center"
                bottom_text = "Esports"
            elif choice_state == "dininghall":
                top_text = "ATEC"
                bottom_text = "JSOM"
            library_text = font.render(top_text, True, (255,255,255))
            cafeteria_text = font.render(bottom_text, True, (255,255,255))
            screen.blit(library_text, (1180,460))
            screen.blit(cafeteria_text, (1180,540))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__=="__main__":
    main()

