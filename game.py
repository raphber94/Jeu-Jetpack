import pygame
from player import Player

#classe jeu
class Game:
    def __init__(self):
        #generer le joueur
        self.player=Player()
        self.pressed={}