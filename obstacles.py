import pygame
import game

class obstacle(pygame.sprite.Sprite):
    def __init__(self,game,x,y,type,rotation):
        super().__init__()
        self.game=game
        self.rotation = rotation
        if type=="fire":
            self.image=pygame.image.load('assets/obstacles/firetrap1.png')
        elif type=="saw":
            self.image = pygame.image.load('assets/obstacles/roue2 GRANDE.png')
        elif type=="laser":
            self.image = pygame.image.load('assets/obstacles/laser_grand.png')
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.velocity=4

    def move(self):
        #if not self.game.check_collision(self,self.game.all_players):
            #if self.game.pressed.get(pygame.K_p) == False:
                self.rect.x-=self.velocity

class arrivee(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        super().__init__()
        self.game=game
        self.velocity=4
        self.image=pygame.image.load('assets/arrivee/0.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def move(self):
        self.rect.x-=self.velocity
