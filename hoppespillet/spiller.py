import pygame as pg

class Spiller:
    def __init__(self):
        self._posx = 20
        self._posy = 20
    
    def tegn(self, vindu):
        pg.draw.circle(vindu, (100,50,140), (100, 200), 25)