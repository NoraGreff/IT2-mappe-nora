from random import randint
import pygame as pg
class Matbit:

    def __init__(self):
        self.x = randint(0,400)
        self.y = randint(0,400)
        self.radius = randint(2,7)
        self.r = randint(0, 255)
        self.g = randint(0, 255)
        self.b = randint(0, 255)
    
    def tegn(self, vindu):
        pg.draw.circle(vindu, (self.r, self.g, self.b), (self.x, self.y), self.radius)