import pygame as pg

class Spiller:
    def __init__(self):
        self.x = 400
        self.y = 400
        self.fartX = 0
        self.fartY = 0
        self.radius = 20
    

    def beveg_opp(self):
        self.y += 1

    def beveg_ned(self):
        self.y -= 1

    def beveg_venstre(self):
        self.x -= 1

    def beveg_hoyre(self):
        self.x += 1

    def tegn(self, vindu):
        pg.draw.circle(vindu, (255 ,20, 147),(self.x, self.y), self.radius)
    ''' bilde = pg.image.load("agario/rihanna.jpeg")
        bilde = pg.transform.scale(bilde, (25,25))
        vindu.blit(bilde, (self.x, self.y))'''
    
    def spis(self):
        pop


    def oppdater_posisjon(self, musX, musY):
        print(musX, musY)
        avstandX = musX - self.x 
        avstandY = musY - self.y

        self.fartX = avstandX * 0.02
        self.fartY = avstandY * 0.02

        self.x += self.fartX
        self.y += self.fartY