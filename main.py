import pygame
from game import Game
from obstacles import *
from niveau1 import *
from niveau2 import *

pygame.init()
resize_x = 1100
resize_y = 600
# Ecran de jeu
pygame.display.set_caption("Jeux Jet-Pack")
screen = pygame.display.set_mode((resize_x, resize_y))

# Musique du menu
menu_music = pygame.mixer.Sound('assets/menu/enzo-aldasoro-phoenix-ghost-of-tsushima.mp3')

# Fond d'écran
background = pygame.image.load('assets/menu/NOIR.png').convert_alpha()
background = pygame.transform.scale(background, (resize_x, resize_y))

# Fond d'écran lvl 1
background_lvl_1 = pygame.image.load('assets/menu/Lvl 1.png').convert_alpha()
background_lvl_1 = pygame.transform.scale(background_lvl_1, (resize_x, resize_y))

# Fond d'écran lvl 2
background_lvl_2 = pygame.image.load('assets/menu/Lvl 2.png').convert_alpha()
background_lvl_2 = pygame.transform.scale(background_lvl_2, (resize_x, resize_y))

# Fond d'écran lvl 3
background_lvl_3 = pygame.image.load('assets/menu/Lvl 3.png').convert_alpha()
background_lvl_3 = pygame.transform.scale(background_lvl_3, (resize_x, resize_y))

# JETPY
Jetpy_name = pygame.image.load('assets/menu/JETPY.png').convert_alpha()
Jetpy_name = pygame.transform.scale(Jetpy_name, (680, 140))
Jetpy_name_rect = Jetpy_name.get_rect()
Jetpy_name_rect.x = 210
Jetpy_name_rect.y = 75


# Bouton Play
play_button = pygame.image.load('assets/menu/PLAY.png').convert_alpha()
play_button = pygame.transform.scale(play_button, (323, 173))
play_button_rect = play_button.get_rect()
play_button_rect.x = 388
play_button_rect.y = 325

# Bouton 1
Lvl1_button = pygame.image.load('assets/menu/LVL 1 button.png').convert_alpha()
Lvl1_button = pygame.transform.scale(Lvl1_button, (215, 115))
Lvl1_button_rect = Lvl1_button.get_rect()
Lvl1_button_rect.x = 168
Lvl1_button_rect.y = 425

# Bouton 2
Lvl2_button = pygame.image.load('assets/menu/LVL 2 button.png').convert_alpha()
Lvl2_button = pygame.transform.scale(Lvl2_button, (215, 115))
Lvl2_button_rect = Lvl2_button.get_rect()
Lvl2_button_rect.x = 443
Lvl2_button_rect.y = 425

# Bouton 3
Lvl3_button = pygame.image.load('assets/menu/LVL 3 button.png').convert_alpha()
Lvl3_button = pygame.transform.scale(Lvl3_button, (215, 115))
Lvl3_button_rect = Lvl3_button.get_rect()
Lvl3_button_rect.x = 718
Lvl3_button_rect.y = 425

# Bouton Select
Select_lvl_button = pygame.image.load('assets/menu/SELECT.png').convert_alpha()
Select_lvl_button = pygame.transform.scale(Select_lvl_button, (300, 115))
Select_lvl_button_rect = Select_lvl_button.get_rect()
Select_lvl_button_rect.x = 400
Select_lvl_button_rect.y = 275

# Bouton crédits
Credits_button = pygame.image.load('assets/menu/CREDITS.png').convert_alpha()
Credits_button = pygame.transform.scale(Credits_button, (150, 58))
Credits_button_rect = Credits_button.get_rect()
Credits_button_rect.x = 940
Credits_button_rect.y = 10

# Initialisation
running = True
Play = True
Choose_lvl = False
Menu = True
Lvl_1 = Lvl_2 = Lvl_3 = False
Start_menu = True
Credit = False

while running:

    if Start_menu:  # Si on arrive au menu
        menu_music.play(1000)
        Start_menu = False
    if Menu:  # Si on est au menu
        screen.blit(background, (0, 0))

    # Lancement des différents niveaux
    if Lvl_1:
        niveau1()
        Lvl_1=False

    if Lvl_2:
        niveau2()
        Lvl_2=False
    if Lvl_3:
        screen.blit(background_lvl_3, (0, 0))
    if Lvl_1 or Lvl_2 or Lvl_3:  # Si lancement d'un niveau
        menu_music.fadeout(1000)
        Choose_lvl = False

    if Play:  # Lancement du jeu
        screen.blit(Jetpy_name, (Jetpy_name_rect.x, Jetpy_name_rect.y))
        screen.blit(play_button, (play_button_rect.x, play_button_rect.y))

    if Choose_lvl:  # Choisir niveau
        screen.blit(Jetpy_name, (Jetpy_name_rect.x, Jetpy_name_rect.y))
        screen.blit(Select_lvl_button, (Select_lvl_button_rect.x, Select_lvl_button_rect.y))
        screen.blit(Lvl1_button, (Lvl1_button_rect.x, Lvl1_button_rect.y))
        screen.blit(Lvl2_button, (Lvl2_button_rect.x, Lvl2_button_rect.y))
        screen.blit(Lvl3_button, (Lvl3_button_rect.x, Lvl3_button_rect.y))
        screen.blit(Credits_button, (Credits_button_rect.x, Credits_button_rect.y))

    if Credit:
        print("BERGER Raphael\nDUONG Valentin\nGREINER Enzo\nJAYANTILAL Teij\nQUELLET Dylan")
        Credit = False
        #lancer les crédits
    pygame.display.flip()

    # Test touches
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not Choose_lvl and play_button_rect.collidepoint(event.pos):  # Si on clic sur "play"
                Play = False
                Choose_lvl = True

            elif Choose_lvl and Lvl1_button_rect.collidepoint(event.pos):  # Si on clic sur "1"
                Lvl_1 = True
                # Lancer lvl 1

            elif Choose_lvl and Lvl2_button_rect.collidepoint(event.pos):  # Si on clic sur "2"
                Lvl_2 = True
                # Lancer lvl 2

            elif Choose_lvl and Lvl3_button_rect.collidepoint(event.pos):  # Si on clic sur "3"
                Lvl_3 = True
                # Lancer lvl 3

            elif Choose_lvl and Credits_button_rect.collidepoint(event.pos):  # Si on clic sur "CREDITS"
                Credit = True
                # Lancer crédits



