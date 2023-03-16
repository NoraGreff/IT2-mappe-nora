import pygame as pg
from random import randint
class Hinder:

    def __init__(self):
        self._posx = 300
        self._posy = 50
        self._hoyde = randint(20, 100)
        self._bredde = 10

    def tegn(self, vindu):
        pg.draw.rect(vindu, (170,30,140), (self._posx, self._posy,self._hoyde, self._bredde))

    def flytt_venste(self):
        self._posx -= 5