import pygame
from player import Player
from obstacles import obstacle

#classe jeu
class Game:
    def __init__(self):
        #generer le joueur
        self.all_players=pygame.sprite.Group()
        self.player=Player()
        self.all_players.add(self.player)
        self.pressed={}
        self.all_obstacles = pygame.sprite.Group()

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)