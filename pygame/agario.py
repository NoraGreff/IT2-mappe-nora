import pygame as pg
from spiller import Spiller
from matbit import Matbit
import math



def sjekk_om_spiller_avsluttet():
    global running
    for event in pg.event.get():
        global running
        if event.type == pg.QUIT:
            running = False


pg.init()
vindu = pg.display.set_mode((400, 400))
clock = pg.time.Clock()
running = True

vindu.fill((255, 255, 255))

spiller1 = Spiller()

matbiter = []

for i in range(20):
    ny_matbit = Matbit()
    matbiter.append(ny_matbit)



while running:
    sjekk_om_spiller_avsluttet()
    vindu.fill((255, 255, 255))

    for matbit in matbiter:
        matbit.tegn(vindu)
        print(f"Matbit:({matbit.x}, {matbit.y})")
        avstand = math.sqrt((spiller1.x-matbit.x)**2+(spiller1.y-matbit.y)**2)
        if avstand <(spiller1.radius - matbit.radius):
            spiller1.spis()

    musX, musY = pg.mouse.get_pos()
    spiller1.oppdater_posisjon(musX, musY)


    spiller1.tegn(vindu)

    pg.display.flip()

    clock.tick(60)

pg.quit()