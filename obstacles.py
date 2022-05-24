import pygame
import game
pygame.init()

image_fire=pygame.image.load('assets/obstacles/feu/6.png')
image_laser=pygame.image.load('assets/obstacles/laser/1.png')
animation_laser=[]
for i in range(10):
    animation_laser.append(pygame.image.load('assets/obstacles/laser/' + str(i) + '.png'))
animation_fire=[]
for i in range(10):
    animation_fire.append(pygame.image.load('assets/obstacles/feu/' + str(i) + '.png'))


class obstacle(pygame.sprite.Sprite):
    def __init__(self,game,x,y,type,rotation):
        super().__init__()
        self.game=game
        self.rotation = rotation
        if type=="fire":
            self.image=image_fire
            self.velocity = 4
        elif type=="laser":
            self.image = image_laser
            self.velocity = 4
        self.image = pygame.transform.rotate(self.image, rotation)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


    def move(self):
        #if not self.game.check_collision(self,self.game.all_players):
            #if self.game.pressed.get(pygame.K_p) == False:
                self.rect.x-=self.velocity

    def laser_animation(self, millis):
        self.image = animation_laser[int(millis[0])]
        self.image = pygame.transform.rotate(self.image, self.rotation)

    def fire_animation(self, millis):
        self.image = animation_fire[int(millis[0])]
        self.image = pygame.transform.rotate(self.image, self.rotation)


class arrivee(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        super().__init__()
        self.game=game
        self.velocity=4
        self.image=pygame.image.load('assets/arrivee/0.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def move(self):
        self.rect.x-=self.velocity
