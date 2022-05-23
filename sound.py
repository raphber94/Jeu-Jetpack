import pygame


class Sound:

    def __init__(self):
        self.elec_sound = pygame.mixer.Sound('sons/electrocution.wav')
        self.jetpackclassique_sound = pygame.mixer.Sound('sons/jetpack2.wav')
        self.sound_volume()
        self.music1 = pygame.mixer.music.load('sons/background.wav')
        self.music_volume = pygame.mixer.music.set_volume(0.25)
        """self.music1_play = pygame.mixer.music.play(-1)
        self.music1_stop=pygame.mixer.music.stop()"""

    def sound_volume(self):
        self.elec_sound.set_volume(0.20)
        self.jetpackclassique_sound.set_volume(0.02)


