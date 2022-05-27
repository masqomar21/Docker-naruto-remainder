from pygame import *
from random import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Cards(sprite.Sprite) :
    def __init__(self, filename, posx, posy, theme) :
        super().__init__()
        self.theme = theme
        self.name = filename.split(".")[0]

        self.original_image = image.load("assets/images/"+self.theme+"/cards/"+filename)

        self.back_image = image.load("assets/images/"+self.theme+"/card_bg.png")
        # draw.rect(self.back_image, WHITE, self.back_image.get_rect())

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft= (posx, posy))
        self.shown = False

    def show(self) :
        self.shown = True
    def hide(self) :
        self.shown = False
    
    def update(self) :
        if self.shown :
            self.image = self.original_image
        else :
            self.image = self.back_image