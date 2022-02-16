import pygame

pygame.init()

#générer la fenetre de notre jeu
pygame.display.set_caption("Jetpy")
pygame.display.set_mode((1080, 720))

running=True

#boucle tant que le jeu est lancé
while running:

    #si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        #si le joueur appuie sur la croix pour fermer le jeu
        if event.type == pygame.QUIT:
            running= False
            pygame.quit()
            print("Fermeture du jeu")
