
import pygame
import sys
import os

pygame.init()
pygame.image.get_extended()
pygame.display.set_caption("A Day with Temoc")
fullscreen = False
resolution = (1920, 1080)
screen = pygame.display.set_mode (resolution, pygame.RESIZABLE)


directory = os.path.dirname(os.path.abspath(__file__))
textbox_path = os.path.join(directory, "assets", "text_box.bmp")
response_path = os.path.join(directory,"assets", "response_box.bmp")
music_path = os.path.join(directory, "assets", "game_music.mp3")
menu_music_path = os.path.join(directory, "assets", "menu_music.mp3")
menu_path = os.path.join(directory, "assets", "menu_screen.bmp")

backgrounds = {
    "intro_bg" : os.path.join(directory, "assets","background.bmp"),
    "library_bg" : os.path.join(directory, "assets","library.bmp"),
    "dininghall_bg": os.path.join(directory, "assets","dininghall.bmp"),
    "esports_bg" : os.path.join(directory, "assets","esports.bmp"),
    "gym_bg" : os.path.join(directory, "assets","pool.bmp"),
    "atec_bg" : os.path.join(directory, "assets","atec_labs.bmp"),
    "jsom_bg" : os.path.join(directory, "assets","jsom.bmp"),
    "dorms_bg" : os.path.join(directory, "assets","dorms.bmp"),
    "su_bg" : os.path.join(directory, "assets","studentunion.bmp"),
}

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

    "dorms" : [
        ("Great choice!", "happy"),
        ("Welcome to Andromeda Hall!", "content"),
        ("Sometimes I like to study in the commons!", "content"),
        ("*yawn* I'm getting sleepy!", "content"),
        ("Thank you for stopping by!", "happy"),
        ("I'm going to take a nap!", "happy")
    ],

    "su" : [
        ("Coolio!", "happy"),
        ("This is the student union!", "content"),
        ("You can get Starbucks, boba, and Panda Express!", "happy"),
        ("Thanks for checking UTD out!", "content"),
        ("I'm going to get some boba and study!", "happy")
    ]


    }

def load_fullscreen(path):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.smoothscale(img, (1920,1080))

def load_scale(path,scale):
    img = pygame.image.load(path).convert_alpha()
    w,h = img.get_size()
    return pygame.transform.smoothscale(img,(int(w/scale), int(h/scale)))

class Music:
    def __init__(self):
        pygame.mixer.init()
        self.play = False
    
    def start_music(self, path, volume = 0.3, loop = True):
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1)
        self.play = True
    
    def pause(self):
        pygame.mixer.music.pause()
        self.play = False 
    
    def resume(self):
        pygame.mixer.music.unpause()
        self.play = True

def menu():
    music = Music()
    music.start_music(menu_music_path, volume = 0.5)
    font = pygame.font.Font(None, 80)
    small_font = pygame.font.Font(None,50)
    menu_bg = load_scale(menu_path, 1)
    running = True

    while running:
        screen.fill((0,0,0))
        title = font.render("A Day with Temoc", True, (0,150,0))
        start = small_font.render("Click anywhere to Start", True, (0,150,0))

        while True:
            screen.blit(menu_bg, (0,0)) 
            screen.blit(title, (520,350))
            screen.blit(start, (570,450))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                return
            pygame.display.flip()
    return start

def main():  
    pygame.event.clear()
    response = load_scale(response_path,4)
    textbox = load_scale(textbox_path, 1.7)
    temoc_imgs = {key: load_scale (path, 2.7)
                  for key, path in expression.items()}
    bg_imgs = {key: load_fullscreen(path)
               for key, path in backgrounds.items()}
    load_scale(expression["happy"], 2.7)
    music = Music()
    music.start_music(music_path, volume = 0.3)
    font = pygame.font.Font(None,60)
    dialogues = load_dialogues()
    current_bg = "intro_bg"
    dialogue = dialogues["intro"]
    index = 0
    current_expression = dialogue[index][1]
    quit_game = False
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

                    if paused:
                        music.pause()
                    if not paused:
                        music.resume()
                        
            if event.type == pygame.MOUSEBUTTONDOWN and not paused:
                if not show_choices:
                    if index < len(dialogue) -1:
                        index += 1
                        current_expression = dialogue[index][1]
                    else:
                        if dialogue == dialogues["intro"]:
                            choice_state = "intro"
                            show_choices = True
                        elif dialogue == dialogues["library"]:
                            choice_state = "library"
                            show_choices = True
                        elif dialogue == dialogues["dininghall"]:
                            choice_state = "dininghall"
                            show_choices = True
                        elif dialogue == dialogues["esports"]:
                            choice_state = "esports"
                            show_choices = True
                        elif dialogue == dialogues["gym"]:
                            choice_state = "gym"
                            show_choices = True
                        elif dialogue == dialogues["atec"]:
                            choice_state = "atec"
                            show_choices = True
                        elif dialogue == dialogues["jsom"]:
                            choice_state = "jsom"
                            show_choices = True
                        else:
                            show_choices = False

                else: 
                    mouse_pos = pygame.mouse.get_pos()

                    if choice_state == "intro":
                        if top_rect.collidepoint(mouse_pos):
                            current_bg = "library_bg"
                            dialogue = dialogues["library"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                        elif bottom_rect.collidepoint(mouse_pos):
                            current_bg = "dininghall_bg"
                            dialogue = dialogues["dininghall"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                    elif choice_state == "library":
                        if bottom_rect.collidepoint(mouse_pos):
                            current_bg = "esports_bg"
                            dialogue = dialogues["esports"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                        elif top_rect.collidepoint(mouse_pos):
                            current_bg = "gym_bg"
                            dialogue = dialogues["gym"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False
                    
                    elif choice_state == "dininghall":
                        if top_rect.collidepoint(mouse_pos):
                            current_bg = "atec_bg"
                            dialogue = dialogues["atec"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                        elif bottom_rect.collidepoint(mouse_pos):
                            current_bg = "jsom_bg"
                            dialogue = dialogues["jsom"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False

                    elif choice_state == "atec":
                        if top_rect.collidepoint(mouse_pos):
                            current_bg = "dorms_bg"
                            dialogue = dialogues["dorms"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False 
                            quit_game = True
                        
                        elif bottom_rect.collidepoint(mouse_pos):
                            current_bg = "su_bg"
                            dialogue = dialogues["su"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False
                            quit_game = True
                    
                    elif choice_state == "jsom":
                        if top_rect.collidepoint(mouse_pos):
                            current_bg = "dorms_bg"
                            dialogue = dialogues["dorms"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False
                            quit_game = True
                        
                        elif bottom_rect.collidepoint(mouse_pos):
                            current_bg = "su_bg"
                            dialogue = dialogues["su"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False
                            quit_game = True
                    
                    elif choice_state == "esports":
                        if top_rect.collidepoint(mouse_pos):
                            current_bg = "dorms_bg"
                            dialogue = dialogues["dorms"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False
                            quit_game = True
                        
                        elif bottom_rect.collidepoint(mouse_pos):
                            current_bg = "su_bg"
                            dialogue = dialogues["su"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False
                            quit_game = True

                    elif choice_state == "gym":
                        if top_rect.collidepoint(mouse_pos):
                            current_bg = "dorms_bg"
                            dialogue = dialogues["dorms"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False
                            quit_game = True
                        
                        elif bottom_rect.collidepoint(mouse_pos):
                            current_bg = "su_bg"
                            dialogue = dialogues["su"]
                            index = 0
                            current_expression = dialogue[index][1]
                            show_choices = False
                            quit_game = True

                

                    

        screen.blit(bg_imgs[current_bg], (0,0))
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
            elif choice_state == "gym":
                top_text = "Dorms"
                bottom_text = "SU"
            elif choice_state == "esports":
                top_text = "Dorms"
                bottom_text = "SU"
            elif choice_state == "atec":
                top_text = "Dorms"
                bottom_text = "SU"
            elif choice_state == "jsom":
                top_text = "Dorms"
                bottom_text = "SU"
            option1_text = font.render(top_text, True, (255,255,255))
            option2_text = font.render(bottom_text, True, (255,255,255))
            screen.blit(option1_text, (1180,460))
            screen.blit(option2_text, (1180,540))

        pygame.display.flip()
        if quit_game and index == len(dialogue)-1:
            pygame.time.delay(5000)
            return menu

    pygame.quit()
    sys.exit()


if __name__=="__main__":
    while True:
        menu()
        main()

