import pygame
from player import Player
from obstacles import Fire1

#classe jeu
class Game:
    def __init__(self):
        #generer le joueur
        self.player=Player()
        self.pressed={}