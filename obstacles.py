import pygame

class Fire1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load('assets/firetrap1.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.velocity=4

    def move(self):
        self.rect.x-=self.velocity