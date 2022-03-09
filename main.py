import pygame
from game import Game

pygame.init()



#générer la fenetre de notre jeu
pygame.display.set_caption("Jetpy")
screen=pygame.display.set_mode((1100, 600))

resize_x=1333
resize_y=1140
#importer les différents plan du fond
plan1=pygame.image.load('assets/background/plan1.png').convert_alpha()
plan1=pygame.transform.scale(plan1,(resize_x,resize_y))

plan2=pygame.image.load('assets/background/plan2.png').convert_alpha()
plan2=pygame.transform.scale(plan2,(resize_x,resize_y))

plan3=pygame.image.load('assets/background/plan3.png').convert_alpha()
plan3=pygame.transform.scale(plan3,(resize_x,resize_y))

plan4=pygame.image.load('assets/background/plan4.png').convert_alpha()
plan4=pygame.transform.scale(plan4,(resize_x,resize_y))

plan5=pygame.image.load('assets/background/plan5.png').convert_alpha()
plan5=pygame.transform.scale(plan5,(resize_x,resize_y))

plan6=pygame.image.load('assets/background/plan6.png').convert_alpha()
plan6=pygame.transform.scale(plan6,(resize_x,resize_y))

plan7=pygame.image.load('assets/background/plan7.png').convert_alpha()
plan7=pygame.transform.scale(plan7,(resize_x,resize_y))

planlight=pygame.image.load('assets/background/planlight.png').convert_alpha()
planlight=pygame.transform.scale(planlight,(resize_x,resize_y))





#charger le jeu
game=Game()

running=True

#horloge
clock = pygame.time.Clock()
fps=60

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

#temps de descente et temps de montée
time_up=0
time_down=0

up=False

#boucle tant que le jeu est lancé
while running:

    #appliquer arriere plan en le répétant à l'infini avec des vitesses différentes en fonction du premier plan, deuxième,...

    #vitesses de chaque plan:
    bg_seventh_plan_x -= 0.25*2
    bg_sixth_plan_x -= 0.5*2
    bg_fifth_plan_x -= 1*2
    bg_fourth_plan_x-=1.3*2
    bg_light_x-=1.5*2
    bg_third_plan_x-=1.8*2
    bg_second_plan_x-=2*2
    bg_firstplan_x -= 2.2*2

    #Pour tous les éléments du septième plan:
    if bg_seventh_plan_x>-1333:
        screen.blit(plan7, (bg_seventh_plan_x, bg_y))
        screen.blit(plan7, (bg_seventh_plan_x + 1333, bg_y))
    else:
        bg_seventh_plan_x=0
        screen.blit(plan7, (bg_seventh_plan_x, bg_y))

    #Pour tous les éléments du sixième plan:
    if bg_sixth_plan_x>-1333:
        screen.blit(plan6, (bg_sixth_plan_x, bg_y))
        screen.blit(plan6, (bg_sixth_plan_x + 1333, bg_y))
    else:
        bg_sixth_plan_x = 0
        screen.blit(plan6, (bg_sixth_plan_x, bg_y))


    # Pour tous les éléments du cinquième plan:
    if bg_fifth_plan_x>-1333:
        screen.blit(plan5, (bg_fifth_plan_x, bg_y))
        screen.blit(plan5, (bg_fifth_plan_x + 1333, bg_y))
    else:
        bg_fifth_plan_x=0
        screen.blit(plan5, (bg_fifth_plan_x, bg_y))


    #Pour tous les éléments du quatrième plan:
    if bg_fourth_plan_x>-1333:
        screen.blit(plan4, (bg_fourth_plan_x, bg_y))
        screen.blit(plan4, (bg_fourth_plan_x + 1333, bg_y))
    else:
        bg_fourth_plan_x=0
        screen.blit(plan4, (bg_fourth_plan_x, bg_y))

    #Plan avec lumière:
    if bg_light_x>-1333:
        screen.blit(planlight, (bg_light_x, bg_y))
        screen.blit(planlight, (bg_light_x + 1333, bg_y))

    else:
        bg_light_x=0
        screen.blit(planlight, (bg_light_x, bg_y))

    #Pour tous les éléments du troisième plan:
    if bg_third_plan_x>-1333:
        screen.blit(plan3, (bg_third_plan_x, bg_y))
        screen.blit(plan3, (bg_third_plan_x + 1333, bg_y))
    else:
        bg_third_plan_x=0
        screen.blit(plan3, (bg_third_plan_x, bg_y))

    #Pour tous les éléments du second plan:
    if bg_second_plan_x>-1333:
        screen.blit(plan2, (bg_second_plan_x, bg_y))
        screen.blit(plan2, (bg_second_plan_x + 1333, bg_y))
    else:
        bg_second_plan_x=0
        screen.blit(plan2, (bg_second_plan_x, bg_y))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)


    #Pour tous les éléments du premier plan:
    if bg_firstplan_x>-1333:
        screen.blit(plan1, (bg_firstplan_x, bg_y))
        screen.blit(plan1, (bg_firstplan_x+1333, bg_y))
    else:
        bg_firstplan_x=0
        screen.blit(plan1, (bg_firstplan_x, bg_y))

    #si le joueur rappuie sur espace alors qu'il n'appuyait pas avant on remet le temps de montée à 0
    if up==False and game.pressed.get(pygame.K_SPACE):
     time_up=0

    if up==True and game.pressed.get(pygame.K_SPACE)==False:
        time_down=0

    if game.pressed.get(pygame.K_SPACE) and game.player.rect.y>2:
        up=True
        time_up+=1
        game.player.move_up(time_up,time_down)
    else:
        up=False
        if game.player.rect.y<514:
            time_down+=2
            game.player.fall(time_down,time_up)

    #avec la chute libre, le joueur sort parfois de l'écran donc on le remet dans le cadre
    if game.player.rect.y > 514:
        game.player.rect.y=514
    elif game.player.rect.y<2:
        game.player.rect.y=2
        time_up=0



    #mise à jour de l'ecran
    pygame.display.flip()

    print(time_down)
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
