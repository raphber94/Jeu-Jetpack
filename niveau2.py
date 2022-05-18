import pygame
from game import Game
from obstacles import *
from niveau1 import *
import time
from pygame.locals import *
#import psyco
#psyco.full()


def niveau2():
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

    # charger le jeu
    game = Game()

    # IMAGES POUR L'ANIMATION
    image_walk_1 = pygame.image.load('assets/walk1.bmp')
    image_walk_2 = pygame.image.load('assets/walk2.bmp')
    flying1 = pygame.image.load('assets/flying.bmp')
    flying2 = pygame.image.load('assets/flying2.bmp')

    #Images pour le fond
    plan3=pygame.image.load('assets/fond_vert/back.png')
    plan2=pygame.image.load('assets/fond_vert/middle.png')
    plan1=pygame.image.load('assets/fond_vert/near.png')

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

        # Animation drapeau arrivée

        # Animation player
        # Au sol
        if (game.player.rect.y == 514):
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
        if up == False and game.pressed.get(pygame.K_SPACE):
            time_up = 0

        if up == True and game.pressed.get(pygame.K_SPACE) == False:
            time_down = 0

        if game.pressed.get(pygame.K_SPACE):
            up = True
            time_up += 1
            v0_down = game.player.move_up(time_up, v0_up)
        else:
            up = False
            if game.player.rect.y < 514:
                time_down += 1
                v0_up = game.player.fall(time_down, v0_down)

        # avec la chute libre, le joueur sort parfois de l'écran donc on le remet dans le cadre
        if game.player.rect.y > 514:
            game.player.rect.y = 514

        # appliquer arriere plan en le répétant à l'infini avec des vitesses différentes en fonction du premier plan, deuxième,...
        screen.blit(plan3, (0, 0))
        screen.blit(plan2, (0, 0))
        screen.blit(plan1, (0, 0))
        # appliquer l'image du joueur
        screen.blit(game.player.image, game.player.rect)


        # On affiche les obstacles et on les fait avancer
        for obst in game.all_obstacles:
            if obst.rect.x <= 1100 and obst.rect.x >= -200:
                screen.blit(obst.image, obst.rect)
            obst.move()


        if game.check_collision(game.player, game.all_obstacles):
            return False

        if game.check_collision(game.player, game.all_finish):
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