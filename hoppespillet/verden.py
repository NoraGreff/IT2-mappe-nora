import pygame as pg
from spiller import Spiller
from hinder import Hinder

spiller1 = Spiller()
hindere = []

for i in range(3):
    nytt_hinder = Hinder()
    hindere.append(nytt_hinder)

pg.init()
VINDU_BREDDE = 500
VINDU_HØYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE,VINDU_HØYDE])

fortsett = True 
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    
    vindu.fill((200,250,250))

    spiller1.tegn(vindu)

    for hinder in hindere:
        hinder.tegn(vindu)
        hinder.flytt_venstre()

    pg.display.flip()
    time.sleep(1/8)

pg.quit()
print("Ferdig")