import pygame
from game import Game
from obstacles import *
from niveau1 import *
import time


def niveau1():
    # générer la fenetre de notre jeu
    pygame.display.set_caption("Jetpy")
    screen = pygame.display.set_mode((1100, 600))

    resize_x = 1333
    resize_y = 1140

    # importer les différents plan du fond
    plan1 = pygame.image.load('assets/background/plan1.png').convert_alpha()
    plan1 = pygame.transform.scale(plan1, (resize_x, resize_y))

    plan2 = pygame.image.load('assets/background/plan2.png').convert_alpha()
    plan2 = pygame.transform.scale(plan2, (resize_x, resize_y))

    plan3 = pygame.image.load('assets/background/plan3.png').convert_alpha()
    plan3 = pygame.transform.scale(plan3, (resize_x, resize_y))

    plan4 = pygame.image.load('assets/background/plan4.png').convert_alpha()
    plan4 = pygame.transform.scale(plan4, (resize_x, resize_y))

    plan5 = pygame.image.load('assets/background/plan5.png').convert_alpha()
    plan5 = pygame.transform.scale(plan5, (resize_x, resize_y))

    plan6 = pygame.image.load('assets/background/plan6.png').convert_alpha()
    plan6 = pygame.transform.scale(plan6, (resize_x, resize_y))

    plan7 = pygame.image.load('assets/background/plan7.png').convert_alpha()
    plan7 = pygame.transform.scale(plan7, (resize_x, resize_y))

    planlight = pygame.image.load('assets/background/planlight.png').convert_alpha()
    planlight = pygame.transform.scale(planlight, (resize_x, resize_y))

    # charger le jeu
    game = Game()

    running = True
    # obstacles
    laser = obstacle(game, 1600, 0, "laser", 0)
    laser2 = obstacle(game, 1600, 200, "laser", 0)
    laser3 = obstacle(game, 2200, 170, "laser", 0)
    laser4 = obstacle(game, 2200, 370, "laser", 0)
    laser5 = obstacle(game, 2400, 170, "laser", 0)
    laser6 = obstacle(game, 2400, 370, "laser", 0)
    laser7 = obstacle(game, 2600, 370, "laser", 0)
    laser8 = obstacle(game, 2800, 0, "laser", 0)
    laser9 = obstacle(game, 3200, 0, "laser", 45)
    laser10 = obstacle(game, 3200, 370, "laser", -45)
    laser11 = obstacle(game, 3450, 0, "laser", -45)
    laser12 = obstacle(game, 3450, 370, "laser", 45)
    # losange 1
    laser13 = obstacle(game, 3650, 87, "laser", -45)
    laser14 = obstacle(game, 3650, 370 - 87, "laser", 45)
    laser15 = obstacle(game, 3650 + 175, 87, "laser", 45)
    laser16 = obstacle(game, 3650 + 175, 370 - 87, "laser", -45)
    ####
    laser17 = obstacle(game, 4100, -10, "laser", 45)
    laser18 = obstacle(game, 4100, 380, "laser", -45)
    laser19 = obstacle(game, 4300, 125, "laser", 90)
    laser20 = obstacle(game, 4300, 350, "laser", 90)
    laser21 = obstacle(game, 4500, 125, "laser", 90)
    laser22 = obstacle(game, 4500, 350, "laser", 90)
    laser23 = obstacle(game, 4700, 125, "laser", 90)
    laser24 = obstacle(game, 4700, 350, "laser", 90)
    # losange 2
    laser25 = obstacle(game, 5050, 87, "laser", -45)
    laser26 = obstacle(game, 5050, 370 - 87, "laser", 45)
    laser27 = obstacle(game, 5050 + 175, 87, "laser", 45)
    laser28 = obstacle(game, 5050 + 175, 370 - 87, "laser", -45)
    # pic vers le haut
    laser29 = obstacle(game, 5400, 385, "laser", -45)
    laser30 = obstacle(game, 5542, 243, "laser", -45)
    laser31 = obstacle(game, 5684, 101, "laser", -45)
    laser32 = obstacle(game, 5884, 101, "laser", 45)
    laser33 = obstacle(game, 6026, 243, "laser", 45)
    laser34 = obstacle(game, 6168, 385, "laser", 45)
    # pic vers le bas
    laser35 = obstacle(game, 6184, 0, "laser", 45)
    laser36 = obstacle(game, 6326, 142, "laser", 45)
    laser37 = obstacle(game, 6468, 284, "laser", 45)
    laser38 = obstacle(game, 6668, 284, "laser", -45)
    laser39 = obstacle(game, 6810, 142, "laser", -45)
    laser40 = obstacle(game, 6952, 0, "laser", -45)
    # petit pic vers le haut
    laser41 = obstacle(game, 6893, 385, "laser", -45)
    laser42 = obstacle(game, 7035, 243, "laser", -45)
    laser43 = obstacle(game, 7235, 243, "laser", 45)
    laser44 = obstacle(game, 7377, 385, "laser", 45)
    # petit pic vers le bas
    laser45 = obstacle(game, 7300, 0, "laser", 45)
    laser46 = obstacle(game, 7442, 142, "laser", 45)
    laser47 = obstacle(game, 7642, 142, "laser", -45)
    laser48 = obstacle(game, 7784, 0, "laser", -45)
    # petit pic vers le haut2
    laser49 = obstacle(game, 7700, 385, "laser", -45)
    laser50 = obstacle(game, 7842, 243, "laser", -45)
    laser51 = obstacle(game, 8042, 243, "laser", 45)
    laser52 = obstacle(game, 8184, 385, "laser", 45)
    # croix 1
    laser53 = obstacle(game, 8250, 0, "laser", 45)
    laser54 = obstacle(game, 8250, 0, "laser", -45)
    # croix 2
    laser55 = obstacle(game, 8450, 370, "laser", 45)
    laser56 = obstacle(game, 8450, 370, "laser", -45)
    # croix 3
    laser57 = obstacle(game, 8650, 150, "laser", 45)
    laser58 = obstacle(game, 8650, 150, "laser", -45)
    # coix 4
    laser59 = obstacle(game, 8920, 0, "laser", 45)
    laser60 = obstacle(game, 8920, 0, "laser", -45)
    # croix 5
    laser61 = obstacle(game, 9000, 370, "laser", -45)
    laser62 = obstacle(game, 9000, 370, "laser", 45)
    # croix 6
    laser63 = obstacle(game, 9200, 75, "laser", 45)
    laser64 = obstacle(game, 9200, 75, "laser", -45)
    # croix 7
    laser65 = obstacle(game, 9400, 300, "laser", -45)
    laser66 = obstacle(game, 9400, 300, "laser", 45)
    # croix 8
    laser67 = obstacle(game, 9550, 0, "laser", 45)
    laser68 = obstacle(game, 9550, 0, "laser", -45)
    # croix 9
    laser69 = obstacle(game, 9650, 370, "laser", 45)
    laser70 = obstacle(game, 9650, 370, "laser", -45)
    # croix 10
    laser71 = obstacle(game, 9850, 150, "laser", -45)
    laser72 = obstacle(game, 9850, 150, "laser", 45)
    # croix 11
    laser73 = obstacle(game, 9850, 0, "laser", -45)
    laser74 = obstacle(game, 9850, 0, "laser", 45)
    # croix 12
    laser75 = obstacle(game, 10025, 370, "laser", -45)
    laser76 = obstacle(game, 10025, 370, "laser", 45)
    # croiw 13
    laser77 = obstacle(game, 10125, 120, "laser", -45)
    laser78 = obstacle(game, 10125, 120, "laser", 45)
    # lasers arrivée
    laser79 = obstacle(game, 10600, 0, "laser", 0)
    laser80 = obstacle(game, 10600, 370, "laser", 0)

    game.all_obstacles.add(laser)
    game.all_obstacles.add(laser2)
    game.all_obstacles.add(laser3)
    game.all_obstacles.add(laser4)
    game.all_obstacles.add(laser5)
    game.all_obstacles.add(laser6)
    game.all_obstacles.add(laser7)
    game.all_obstacles.add(laser8)
    game.all_obstacles.add(laser9)
    game.all_obstacles.add(laser10)
    game.all_obstacles.add(laser11)
    game.all_obstacles.add(laser12)
    game.all_obstacles.add(laser13)
    game.all_obstacles.add(laser14)
    game.all_obstacles.add(laser15)
    game.all_obstacles.add(laser16)
    game.all_obstacles.add(laser17)
    game.all_obstacles.add(laser18)
    game.all_obstacles.add(laser19)
    game.all_obstacles.add(laser20)
    game.all_obstacles.add(laser21)
    game.all_obstacles.add(laser22)
    game.all_obstacles.add(laser23)
    game.all_obstacles.add(laser24)
    game.all_obstacles.add(laser25)
    game.all_obstacles.add(laser26)
    game.all_obstacles.add(laser27)
    game.all_obstacles.add(laser28)
    game.all_obstacles.add(laser29)
    game.all_obstacles.add(laser30)
    game.all_obstacles.add(laser31)
    game.all_obstacles.add(laser32)
    game.all_obstacles.add(laser33)
    game.all_obstacles.add(laser34)
    game.all_obstacles.add(laser35)
    game.all_obstacles.add(laser36)
    game.all_obstacles.add(laser37)
    game.all_obstacles.add(laser38)
    game.all_obstacles.add(laser39)
    game.all_obstacles.add(laser40)
    game.all_obstacles.add(laser41)
    game.all_obstacles.add(laser42)
    game.all_obstacles.add(laser43)
    game.all_obstacles.add(laser44)
    game.all_obstacles.add(laser45)
    game.all_obstacles.add(laser46)
    game.all_obstacles.add(laser47)
    game.all_obstacles.add(laser48)
    game.all_obstacles.add(laser49)
    game.all_obstacles.add(laser50)
    game.all_obstacles.add(laser51)
    game.all_obstacles.add(laser52)
    game.all_obstacles.add(laser53)
    game.all_obstacles.add(laser54)
    game.all_obstacles.add(laser55)
    game.all_obstacles.add(laser56)
    game.all_obstacles.add(laser57)
    game.all_obstacles.add(laser58)
    game.all_obstacles.add(laser59)
    game.all_obstacles.add(laser60)
    game.all_obstacles.add(laser61)
    game.all_obstacles.add(laser62)
    game.all_obstacles.add(laser63)
    game.all_obstacles.add(laser64)
    game.all_obstacles.add(laser65)
    game.all_obstacles.add(laser66)
    game.all_obstacles.add(laser67)
    game.all_obstacles.add(laser68)
    game.all_obstacles.add(laser69)
    game.all_obstacles.add(laser70)
    game.all_obstacles.add(laser71)
    game.all_obstacles.add(laser72)
    game.all_obstacles.add(laser73)
    game.all_obstacles.add(laser74)
    game.all_obstacles.add(laser75)
    game.all_obstacles.add(laser76)
    game.all_obstacles.add(laser77)
    game.all_obstacles.add(laser78)
    game.all_obstacles.add(laser79)
    game.all_obstacles.add(laser80)

    # horloge
    clock = pygame.time.Clock()
    fps = 60

    # coordonnées du background
    bg_y = -485
    bg_seventh_plan_x = 0
    bg_sixth_plan_x = 0
    bg_fifth_plan_x = 0
    bg_fourth_plan_x = 0
    bg_third_plan_x = 0
    bg_second_plan_x = 0
    bg_firstplan_x = 0
    bg_light_x = 0

    # temps de descente et temps de montée
    time_up = 0
    time_down = 0
    v0_up = 0
    v0_down = 0

    # arrivée
    fin = arrivee(game, 10700, 200)
    game.all_finish.add(fin)

    up = False

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
        # print(millis)
        # Animation obstacle
        for k in game.all_obstacles:
            k.image = pygame.image.load('assets/obstacles/laser/' + millis[0] + '.png')
            k.image = pygame.transform.rotate(k.image, k.rotation)

        # Animation drapeau arrivée
        if (not int(millis[0]) % 2):
            fin.image = pygame.image.load('assets/arrivee/' + millis[0] + '.png').convert_alpha()
        # Animation player
        # Au sol
        if (game.player.rect.y == 514):
            if (0 <= int(millis[0]) * 10 + int(millis[1]) < 25 or 50 <= int(millis[0]) * 10 + int(millis[1]) < 75):
                game.player.image = pygame.image.load('assets/walk1.bmp').convert_alpha()
            else:
                game.player.image = pygame.image.load('assets/walk2.bmp').convert_alpha()
        # En vol
        else:
            # Si space pressed
            if (game.pressed.get(pygame.K_SPACE)):
                game.player.image = pygame.image.load('assets/flying.bmp').convert_alpha()
            else:
                game.player.image = pygame.image.load('assets/flying2.bmp').convert_alpha()

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
        # Pour tous les éléments du septième plan:

        # vitesses de chaque plan
        bg_seventh_plan_x -= 0.25 * 2
        bg_sixth_plan_x -= 0.5 * 2
        bg_fifth_plan_x -= 1 * 2
        bg_fourth_plan_x -= 1.3 * 2
        bg_light_x -= 1.5 * 2
        bg_third_plan_x -= 1.8 * 2
        bg_second_plan_x -= 2 * 2
        bg_firstplan_x -= 2.2 * 2

        if bg_seventh_plan_x > -1333:
            screen.blit(plan7, (bg_seventh_plan_x, bg_y))
            screen.blit(plan7, (bg_seventh_plan_x + 1333, bg_y))
        else:
            bg_seventh_plan_x = 0
            screen.blit(plan7, (bg_seventh_plan_x, bg_y))

        # Pour tous les éléments du sixième plan:
        if bg_sixth_plan_x > -1333:
            screen.blit(plan6, (bg_sixth_plan_x, bg_y))
            screen.blit(plan6, (bg_sixth_plan_x + 1333, bg_y))
        else:
            bg_sixth_plan_x = 0
            screen.blit(plan6, (bg_sixth_plan_x, bg_y))

        # Pour tous les éléments du cinquième plan:
        if bg_fifth_plan_x > -1333:
            screen.blit(plan5, (bg_fifth_plan_x, bg_y))
            screen.blit(plan5, (bg_fifth_plan_x + 1333, bg_y))
        else:
            bg_fifth_plan_x = 0
            screen.blit(plan5, (bg_fifth_plan_x, bg_y))

        # Pour tous les éléments du quatrième plan:
        if bg_fourth_plan_x > -1333:
            screen.blit(plan4, (bg_fourth_plan_x, bg_y))
            screen.blit(plan4, (bg_fourth_plan_x + 1333, bg_y))
        else:
            bg_fourth_plan_x = 0
            screen.blit(plan4, (bg_fourth_plan_x, bg_y))

        # Plan avec lumière:
        if bg_light_x > -1333:
            screen.blit(planlight, (bg_light_x, bg_y))
            screen.blit(planlight, (bg_light_x + 1333, bg_y))

        else:
            bg_light_x = 0
            screen.blit(planlight, (bg_light_x, bg_y))

        # Pour tous les éléments du troisième plan:
        if bg_third_plan_x > -1333:
            screen.blit(plan3, (bg_third_plan_x, bg_y))
            screen.blit(plan3, (bg_third_plan_x + 1333, bg_y))
        else:
            bg_third_plan_x = 0
            screen.blit(plan3, (bg_third_plan_x, bg_y))

        # Pour tous les éléments du second plan:
        if bg_second_plan_x > -1333:
            screen.blit(plan2, (bg_second_plan_x, bg_y))
            screen.blit(plan2, (bg_second_plan_x + 1333, bg_y))
        else:
            bg_second_plan_x = 0
            screen.blit(plan2, (bg_second_plan_x, bg_y))

        # appliquer l'image du joueur
        screen.blit(game.player.image, game.player.rect)

        # Pour tous les éléments du premier plan:
        if bg_firstplan_x > -1333:
            screen.blit(plan1, (bg_firstplan_x, bg_y))
            screen.blit(plan1, (bg_firstplan_x + 1333, bg_y))
        else:
            bg_firstplan_x = 0
            screen.blit(plan1, (bg_firstplan_x, bg_y))

        # On affiche les obstacles et on les fait avancer
        for obst in game.all_obstacles:
            if obst.rect.x <= 1100 and obst.rect.x >= -200:
                screen.blit(obst.image, obst.rect)
            obst.move()

        fin.move()
        screen.blit(fin.image, (fin.rect.x, fin.rect.y))
        # mise à jour de l'ecran
        pygame.display.flip()
        clock.tick(fps)

        #if game.check_collision(game.player, game.all_obstacles):
            #return False

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