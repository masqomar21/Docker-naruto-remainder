import pygame

class Music:

    def __init__(self, path):
        pygame.init()
        pygame.mixer.init()
        self.music = pygame.mixer.music
        self.sound = path
        self.music.load(self.sound)
        self.music.play(-1)
        self.music.set_volume(0.5)

    def volchange(self, volume):
        self.music.set_volume(volume)  # The set_volume range is from 0.00 to 1.00 (every 0.01)
    def isplaying(self):
        return self.music.get_busy()


class sound_effect:

    def __init__(self, path):
        pygame.init()
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(path)
        pygame.mixer.Sound.set_volume(self.sound, 0.5)

    def play(self):
        pygame.mixer.Sound.play(self.sound)