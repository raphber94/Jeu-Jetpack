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
    feu1 = obstacle(game, 750, 300, "fire", 0)
    feu2 = obstacle(game, 1000, 0, "fire", 180)
    feu3 = obstacle(game, 1300, 0, "fire", 180)
    feu4 = obstacle(game, 1600, 300, "fire", 0)
    feu5 = obstacle(game, 1900, 0, "fire", 180)
    feu6 = obstacle(game, 2000, 0, "fire", 180)
    feu7 = obstacle(game, 2100, 0, "fire", 180)
    feu8 = obstacle(game, 2350, 300, "fire", 0)
    feu9 = obstacle(game, 2450, 300, "fire", 0)
    feu10 = obstacle(game, 2600, 0, "fire", 180)
    feu11 = obstacle(game, 2800, 400, "fire", 0)
    feu12 = obstacle(game, 3000, 160, "fire", 90)
    feu13 = obstacle(game, 3300, 150, "fire", 270)
    feu14 = obstacle(game, 3300, 405, "fire", 90)
    feu15 = obstacle(game, 3600, 400, "fire", 270)
    feu16 = obstacle(game, 3700, -150, "fire", 180)
    feu17 = obstacle(game, 3800, 230, "fire", 90)
    feu18 = obstacle(game, 4100, 230, "fire", 270)
    feu19 = obstacle(game, 4400, 450, "fire", 0)
    feu20 = obstacle(game, 4400, -150, "fire", 180)
    feu21 = obstacle(game, 4600, -75, "fire", 180)
    feu22 = obstacle(game, 4600, 375, "fire", 0)
    feu23 = obstacle(game, 4900, 250, "fire", 135)
    feu24 = obstacle(game, 5100, 50, "fire", 315)
    feu25 = obstacle(game, 5400, 230, "fire", 90)
    feu26 = obstacle(game, 5700, 230, "fire", 270)
    feu27 = obstacle(game, 6200, 300, "fire", 0)

    game.all_obstacles.add(feu1)
    game.all_obstacles.add(feu2)
    game.all_obstacles.add(feu3)
    game.all_obstacles.add(feu4)
    game.all_obstacles.add(feu5)
    game.all_obstacles.add(feu6)
    game.all_obstacles.add(feu7)
    game.all_obstacles.add(feu8)
    game.all_obstacles.add(feu9)
    game.all_obstacles.add(feu10)
    game.all_obstacles.add(feu11)
    game.all_obstacles.add(feu12)
    game.all_obstacles.add(feu13)
    game.all_obstacles.add(feu14)
    game.all_obstacles.add(feu15)
    game.all_obstacles.add(feu16)
    game.all_obstacles.add(feu17)
    game.all_obstacles.add(feu18)
    game.all_obstacles.add(feu19)
    game.all_obstacles.add(feu20)
    game.all_obstacles.add(feu21)
    game.all_obstacles.add(feu22)
    game.all_obstacles.add(feu23)
    game.all_obstacles.add(feu24)
    game.all_obstacles.add(feu25)
    game.all_obstacles.add(feu26)
    game.all_obstacles.add(feu27)

    fin=arrivee(game,6210,100)
    game.all_finish.add(fin)
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
            if k.rect.x <= 1100 and k.rect.x >= -600:
                k.fire_animation(millis)

        # Animation drapeau arrivée
        if fin.rect.x <= 1100 and fin.rect.x >= -600:
            if (not int(millis[0]) % 2):
                        fin.image = pygame.image.load('assets/arrivee/' + millis[0] + '.png')
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

        # On affiche les obstacles et on les fait avancer
        for obst in game.all_obstacles:
            if obst.rect.x <= 1100 and obst.rect.x >= -600:
                screen.blit(obst.image, obst.rect)
            obst.move()

        if fin.rect.x<=1100 and fin.rect.x>=-600:
            screen.blit(fin.image, (fin.rect.x, fin.rect.y))
        fin.move()

        # Pour tous les éléments du premier plan:
        if plan1_x > -1490:
            screen.blit(plan1, (plan1_x, 0))
            screen.blit(plan1, (plan1_x + 1490, 0))
        else:
            plan1_x = 0
            screen.blit(plan1, (plan1_x, 0))

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