import pygame

#clase joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity_x=5
        self.velocity_y=10
        self.image=pygame.image.load('assets/walk1.bmp').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=200
        self.rect.y= 514

    def move_up(self,time_up,time_down):
        self.rect.y-=(self.velocity_y/2)*(time_up/60)**2+(5*time_down/360)
        if self.rect.y<2:
            self.rect.y=2

    def move_down(self):
        self.rect.y+=self.velocity_y

    def fall(self,time_down,time_up):
        if self.rect.y<514:
            self.rect.y+=5*(time_down/60)**2-self.velocity_y*(time_up/180)
        else:
            self.rect.y=514
