import pygame
from game import Game

pygame.init()



#générer la fenetre de notre jeu
pygame.display.set_caption("Jetpy")
screen=pygame.display.set_mode((928, 793))

#importer l'image du fond
background=pygame.image.load('assets/bg6.jpg')
brouillard1=pygame.image.load('assets/background/brouillard1.png')
brouillard2=pygame.image.load('assets/background/brouillard2.png')
feuillages=pygame.image.load('assets/background/feuillages.png')
fond=pygame.image.load('assets/background/fond.png')
herbe=pygame.image.load('assets/background/herbe.png')
lumiere1=pygame.image.load('assets/background/lumiere1.png')
lumiere2=pygame.image.load('assets/background/lumiere2.png')
ombres1=pygame.image.load('assets/background/ombres1.png')
ombres2=pygame.image.load('assets/background/ombres2.png')
ombres3=pygame.image.load('assets/background/ombres3.png')
terre=pygame.image.load('assets/background/terre.png')
tronc=pygame.image.load('assets/background/tronc.png')

#charger le jeu
game=Game()

running=True

#horloge
clock = pygame.time.Clock()
fps=60

#coordonnées du background
bg_x=0
bg_y=0

#boucle tant que le jeu est lancé
while running:

    #appliquer arriere plan
    #bg_x-=1
    #screen.blit(background,(bg_x,bg_y))
    screen.blit(fond,(0,0))
    screen.blit(brouillard2, (0, 0))
    screen.blit(brouillard1,(0,0))
    screen.blit(ombres3, (0, 0))
    screen.blit(ombres2, (0, 0))
    screen.blit(ombres1, (0, 0))
    screen.blit(herbe, (0, 0))
    screen.blit(tronc, (0, 0))
    screen.blit(terre, (0, 0))
    screen.blit(feuillages, (0, 0))
    screen.blit(lumiere2, (0, 0))
    screen.blit(lumiere1, (0, 0))




    #appliquer l'image du joueur
    screen.blit(game.player.image,game.player.rect)

    if game.pressed.get(pygame.K_SPACE)and game.player.rect.y>105:
        game.player.move_up()
    elif game.pressed.get(pygame.K_s) and game.player.rect.y<580:
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