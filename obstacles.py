import pygame
import game

class Fire1(pygame.sprite.Sprite):
    def __init__(self,game,x,y,type):
        super().__init__()
        self.game=game
        if type=="fire":
            self.image=pygame.image.load('assets/obstacles/firetrap1.png')
        elif type=="saw":
            self.image = pygame.image.load('assets/obstacles/roue2 GRANDE.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.velocity=4

    def move(self):
        if not self.game.check_collision(self,self.game.all_players):
            self.rect.x-=self.velocity