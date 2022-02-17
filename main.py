import pygame
from game import Game

pygame.init()



#générer la fenetre de notre jeu
pygame.display.set_caption("Jetpy")
screen=pygame.display.set_mode((1027, 768))

#importer l'image du fond
background=pygame.image.load('assets/bg6.jpg')

#charger le jeu
game=Game()

running=True

#horloge
clock = pygame.time.Clock()
fps=120

#boucle tant que le jeu est lancé
while running:

    #appliquer arriere plan
    screen.blit(background,(0,0))

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
