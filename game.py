import pygame
from player import Player
from obstacles import Fire1

#classe jeu
class Game:
    def __init__(self):
        #generer le joueur
        self.all_players=pygame.sprite.Group()
        self.player=Player()
        self.all_players.add(self.player)
        self.pressed={}
        self.all_fires = pygame.sprite.Group()

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)