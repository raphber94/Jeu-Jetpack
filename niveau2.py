import pygame
from game import Game
from obstacles import *
import time
from pygame.locals import *
#import psyco
#psyco.full()


def niveau2():
    # charger le jeu
    game = Game()

    pygame.mixer.music.load('sons/musique2.mp3')
    pygame.mixer.music.play()
    OOF = pygame.mixer.Sound('sons/OOF.mp3')
    # générer la fenetre de notre jeu
    pygame.display.set_caption("Jetpy")
    flags = DOUBLEBUF
    screen = pygame.display.set_mode((1100, 600), flags)
    screen.set_alpha(None)
    # horloge
    clock = pygame.time.Clock()
    fps = 60

    # temps de descente et temps de montée
    time_up = 0
    time_down = 0
    v0_up = 0
    v0_down = 0
    up = False

    # IMAGES POUR L'ANIMATION
    image_walk_1 = pygame.image.load('assets/walk1.bmp')
    image_walk_2 = pygame.image.load('assets/walk2.bmp')
    flying1 = pygame.image.load('assets/flying.bmp')
    flying2 = pygame.image.load('assets/flying2.bmp')



    #Images pour le fond
    plan5=pygame.image.load('assets/fond grotte/1_1.png').convert_alpha()
    plan4=pygame.image.load('assets/fond grotte/1_2.png').convert_alpha()
    plan3=pygame.image.load('assets/fond grotte/1_3.png').convert_alpha()
    plan2=pygame.image.load('assets/fond grotte/1_4.png').convert_alpha()
    plan1=pygame.image.load('assets/fond grotte/1_5.png').convert_alpha()

    plan5_x=0
    plan4_x=0
    plan3_x=0
    plan2_x=0
    plan1_x=0

    #OBSTACLES
    feu1=obstacle(game,715,300,"fire",0)
    feu2 = obstacle(game, 900, 0, "fire", 180)
    game.all_obstacles.add(feu1)
    game.all_obstacles.add(feu2)

    game.player.rect.y=435
    game.player.rect.y=435
    running=True
    # boucle tant que le jeu est lancé
    while running:
        # Pas basé sur le temps -> update tous les 0.5s
        # On récupère le temps actuel en s ===> "time.time()"
        # On le convertit en string ===> "str((time.time()))" -> ressemble à ABCDEF.abcde, a correspond au dixième de seconde
        # On sépare la string en un tableau de 2 éléments [0] = entier et [1] = décimal ===> "str((time.time())).split(".")"
        # On prend les décimals ===> "str((time.time())).split(".")[1]"
        # Ainsi, millis[0] va prendre toutes les valeurs de 0 à 9 toutes les 0.1s
        # millis[1] va prendre toutes les valeurs de 0 à 9 toutes les 0.01s
        # Et ainsi de suite
        millis = str((time.time())).split(".")[1]
        #print(millis)
        # Animation obstacle
        for k in game.all_obstacles:
            if k.rect.x <= 1100 and k.rect.x >= -200:
                k.fire_animation(millis)

        # Animation drapeau arrivée

        # Animation player
        # Au sol
        if (game.player.rect.y == 435):
            if (0 <= int(millis[0]) * 10 + int(millis[1]) < 25 or 50 <= int(millis[0]) * 10 + int(millis[1]) < 75):
                game.player.image = image_walk_1
            else:
                game.player.image = image_walk_2
        # En vol
        else:
            # Si barre espace pressée
            if (game.pressed.get(pygame.K_SPACE)):
                game.player.image = flying1
            else:
                game.player.image = flying2

        # si le joueur rappuie sur espace alors qu'il n'appuyait pas avant on remet le temps de montée à 0
        if game.pressed.get(pygame.K_SPACE):
            up = True
            if game.player.rect.y == 2:
                time_up = 1
            else:
                time_up += 1
            if (time_down > 0):
                time_down -= 1
        else:
            if game.player.rect.y < 435:
                time_down += 1
            else:
                time_down = 1
            if (time_up > 0):
                time_up -= 1
            up = False

        v0_down = game.player.move_up(time_up, v0_up)

        if game.player.rect.y < 435:
            v0_up = game.player.fall(time_down, v0_down)

        # avec la chute libre, le joueur sort parfois de l'écran donc on le remet dans le cadre
        if game.player.rect.y >435:
            game.player.rect.y = 435

        #vitesses des plans
        plan5_x -= 1 * 2
        plan4_x -= 1.3 * 2
        plan3_x -= 1.5 * 2
        plan2_x -= 1.7 * 2
        plan1_x -= 2 * 2

        # appliquer arriere plan en le répétant à l'infini avec des vitesses différentes en fonction du premier plan, deuxième,...
        # Pour tous les éléments du cinquième plan:
        if plan5_x > -1490:
            screen.blit(plan5, (plan5_x, 0))
            screen.blit(plan5, (plan5_x + 1490, 0))
        else:
            plan5_x = 0
            screen.blit(plan5, (plan5_x, 0))

        # Pour tous les éléments du quatrième plan:
        if plan4_x > -1490:
            screen.blit(plan4, (plan4_x, 0))
            screen.blit(plan4, (plan4_x + 1490, 0))
        else:
            plan4_x = 0
            screen.blit(plan4, (plan4_x, 0))

        # Pour tous les éléments du troisième plan:
        if plan3_x > -1490:
            screen.blit(plan3, (plan3_x, 0))
            screen.blit(plan3, (plan3_x + 1490, 0))
        else:
            plan3_x = 0
            screen.blit(plan3, (plan3_x, 0))

        # Pour tous les éléments du second plan:
        if plan2_x > -1490:
            screen.blit(plan2, (plan2_x, 0))
            screen.blit(plan2, (plan2_x + 1490, 0))
        else:
            plan2_x = 0
            screen.blit(plan2, (plan2_x, 0))

        # appliquer l'image du joueur
        screen.blit(game.player.image, game.player.rect)

        # Pour tous les éléments du premier plan:
        if plan1_x > -1490:
            screen.blit(plan1, (plan1_x, 0))
            screen.blit(plan1, (plan1_x + 1490, 0))
        else:
            plan1_x = 0
            screen.blit(plan1, (plan1_x, 0))



        # On affiche les obstacles et on les fait avancer
        for obst in game.all_obstacles:
            if obst.rect.x <= 1100 and obst.rect.x >= -200:
                screen.blit(obst.image, obst.rect)
            obst.move()


        if game.check_collision(game.player, game.all_obstacles):
            OOF.play()
            pygame.mixer.music.stop()
            return False

        if game.check_collision(game.player, game.all_finish):
            pygame.mixer.music.stop()
            return True

        # si le joueur ferme cette fenêtre
        for event in pygame.event.get():
            # si le joueur appuie sur la croix pour fermer le jeu
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

        # mise à jour de l'ecran
        pygame.display.flip()
        clock.tick(fps)
        #print(clock.get_fps())