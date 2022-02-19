import pygame

#clase joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity_x=5
        self.velocity_y=6
        self.image=pygame.image.load('assets/walk1.bmp').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=200
        self.rect.y= 514

    def move_up(self):
        self.rect.y-=self.velocity_y

    def move_down(self):
        self.rect.y+=self.velocity_y