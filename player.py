import pygame

#clase joueur
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity_x=5
        self.velocity_y=5
        self.image=pygame.image.load('assets/walk1.bmp').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=200
        self.rect.y= 514
        self.m=10

    def move_up(self,time_up,v0_up):
        """self.rect.y = self.rect.y - (self.velocity_y / 2) * (time_up / 60) ** 2 + v0_up * time_up / 60
        if self.rect.y<2:
            self.rect.y=2
            return 0
        else:
            print("vitesse de montée:",- (self.velocity_y / 2) * (time_up / 60) ** 2 + v0_up * time_up / 60)
            return self.velocity_y*time_up/60+v0_up"""
        self.rect.y=self.rect.y-1/2*self.velocity_y*(time_up/60)**2
        if self.rect.y<2:
            self.rect.y=2
        return 0

    def fall(self,time_down,v0_down):
        """if self.rect.y<510:
            self.rect.y=self.rect.y+7.5*(time_down/60)**2-v0_down*time_down/60
            print("vitesse de descente:",7.5*(time_down/60)**2-v0_down*time_down/60)
            return 5 * (time_down / 60) + v0_down

        elif self.rect.y==513:
            return 0
        else:
            self.rect.y=514
            return 0"""
        self.rect.y = self.rect.y + 1 / 2 * 10 * (time_down / 60) ** 2




