import pygame
from game import Game

pygame.init()



#générer la fenetre de notre jeu
pygame.display.set_caption("Jetpy")
screen=pygame.display.set_mode((1100, 600))

resize_x=1333
resize_y=1140
#importer l'image du fond
background=pygame.image.load('assets/bg6.jpg').convert_alpha()
background=pygame.transform.scale(background,(resize_x,resize_y))

brouillard1=pygame.image.load('assets/background/brouillard1.png').convert_alpha()
brouillard1=pygame.transform.scale(brouillard1,(resize_x,resize_y))

brouillard2=pygame.image.load('assets/background/brouillard2.png').convert_alpha()
brouillard2=pygame.transform.scale(brouillard2,(resize_x,resize_y))

feuillages=pygame.image.load('assets/background/feuillages.png').convert_alpha()
feuillages=pygame.transform.scale(feuillages,(resize_x,resize_y))

fond=pygame.image.load('assets/background/fond.png').convert_alpha()
fond=pygame.transform.scale(fond,(resize_x,resize_y))

herbe=pygame.image.load('assets/background/herbe.png').convert_alpha()
herbe=pygame.transform.scale(herbe,(resize_x,resize_y))

lumiere1=pygame.image.load('assets/background/lumiere1.png').convert_alpha()
lumiere1=pygame.transform.scale(lumiere1,(resize_x,resize_y))

lumiere2=pygame.image.load('assets/background/lumiere2.png').convert_alpha()
lumiere2=pygame.transform.scale(lumiere2,(resize_x,resize_y))

ombres1=pygame.image.load('assets/background/ombres1.png').convert_alpha()
ombres1=pygame.transform.scale(ombres1,(resize_x,resize_y))

ombres2=pygame.image.load('assets/background/ombres2.png').convert_alpha()
ombres2=pygame.transform.scale(ombres2,(resize_x,resize_y))

ombres3=pygame.image.load('assets/background/ombres3.png').convert_alpha()
ombres3=pygame.transform.scale(ombres3,(resize_x,resize_y))

terre=pygame.image.load('assets/background/terre.png').convert_alpha()
terre=pygame.transform.scale(terre,(resize_x,resize_y))

tronc=pygame.image.load('assets/background/tronc.png').convert_alpha()
tronc=pygame.transform.scale(tronc,(resize_x,resize_y))

#charger le jeu
game=Game()

running=True

#horloge
clock = pygame.time.Clock()
fps=120

#coordonnées du background
bg_y=-485
bg_seventh_plan_x=0
bg_sixth_plan_x=0
bg_fifth_plan_x=0
bg_fourth_plan_x=0
bg_third_plan_x=0
bg_second_plan_x=0
bg_firstplan_x=0
bg_light_x=0


#boucle tant que le jeu est lancé
while running:

    #appliquer arriere plan en le répétant à l'infini avec des vitesses différentes en fonction du premier plan, deuxième,...

    #vitesses de chaque plan:
    bg_seventh_plan_x -= 0.25
    bg_sixth_plan_x -= 0.5
    bg_fifth_plan_x -= 1
    bg_fourth_plan_x-=1.3
    bg_light_x-=1.5
    bg_third_plan_x-=1.8
    bg_second_plan_x-=2
    bg_firstplan_x -= 2.2

    #Pour tous les éléments du septième plan:
    if bg_seventh_plan_x>-1333:
        screen.blit(fond, (bg_seventh_plan_x, bg_y))
        screen.blit(fond, (bg_seventh_plan_x + 1333, bg_y))

        screen.blit(brouillard2, (bg_seventh_plan_x, bg_y))
        screen.blit(brouillard2, (bg_seventh_plan_x + 1333, bg_y))

        screen.blit(brouillard1, (bg_seventh_plan_x, bg_y))
        screen.blit(brouillard1, (bg_seventh_plan_x + 1333, bg_y))
    else:
        bg_seventh_plan_x=0
        screen.blit(fond, (bg_seventh_plan_x, bg_y))
        screen.blit(brouillard2, (bg_seventh_plan_x, bg_y))
        screen.blit(brouillard1, (bg_seventh_plan_x, bg_y))

    #Pour tous les éléments du sixième plan:
    if bg_sixth_plan_x>-1333:
        screen.blit(ombres3, (bg_sixth_plan_x, bg_y))
        screen.blit(ombres3, (bg_sixth_plan_x + 1333, bg_y))
        screen.blit(lumiere2, (bg_sixth_plan_x, bg_y))
        screen.blit(lumiere2, (bg_sixth_plan_x + 1333, bg_y))
    else:
        bg_sixth_plan_x=0
        screen.blit(ombres3, (bg_sixth_plan_x, bg_y))
        screen.blit(lumiere2, (bg_sixth_plan_x, bg_y))


    # Pour tous les éléments du cinquième plan:
    if bg_fifth_plan_x>-1333:
        screen.blit(ombres2, (bg_fifth_plan_x, bg_y))
        screen.blit(ombres2, (bg_fifth_plan_x + 1333, bg_y))
    else:
        bg_fifth_plan_x=0
        screen.blit(ombres2, (bg_fifth_plan_x, bg_y))


    #Pour tous les éléments du quatrième plan:
    if bg_fourth_plan_x>-1333:
        screen.blit(ombres1, (bg_fourth_plan_x, bg_y))
        screen.blit(ombres1, (bg_fourth_plan_x + 1333, bg_y))
    else:
        bg_fourth_plan_x=0
        screen.blit(ombres1, (bg_fourth_plan_x, bg_y))

    #Plan avec lumière:
    if bg_light_x>-1333:
        screen.blit(lumiere1, (bg_light_x, bg_y))
        screen.blit(lumiere1, (bg_light_x + 1333, bg_y))

    else:
        bg_light_x=0
        screen.blit(lumiere1, (bg_light_x, bg_y))

    #Pour tous les éléments du troisième plan:
    if bg_third_plan_x>-1333:
        screen.blit(tronc, (bg_third_plan_x, bg_y))
        screen.blit(tronc, (bg_third_plan_x + 1333, bg_y))
    else:
        bg_third_plan_x=0
        screen.blit(tronc, (bg_third_plan_x, bg_y))

    #Pour tous les éléments du second plan:
    if bg_second_plan_x>-1333:
        screen.blit(herbe, (bg_second_plan_x, bg_y))
        screen.blit(herbe, (bg_second_plan_x + 1333, bg_y))
        screen.blit(feuillages, (bg_second_plan_x, bg_y))
        screen.blit(feuillages, (bg_second_plan_x + 1333, bg_y))
    else:
        bg_second_plan_x=0
        screen.blit(herbe, (bg_second_plan_x, bg_y))
        screen.blit(feuillages, (bg_second_plan_x, bg_y))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)


    #Pour tous les éléments du premier plan:
    if bg_firstplan_x>-1333:
        screen.blit(terre, (bg_firstplan_x, bg_y))
        screen.blit(terre, (bg_firstplan_x+1333, bg_y))
    else:
        bg_firstplan_x=0
        screen.blit(herbe, (bg_firstplan_x, bg_y))
        screen.blit(terre, (bg_firstplan_x, bg_y))




    if game.pressed.get(pygame.K_SPACE) and game.player.rect.y>2:
        game.player.move_up()
    elif game.pressed.get(pygame.K_s) and game.player.rect.y<509:
        game.player.move_down()

    #mise à jour de l'ecran
    pygame.display.flip()


    clock.tick(fps)

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #si le joueur appuie sur la croix pour fermer le jeu
        if event.type == pygame.QUIT:
            running= False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key]=True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False