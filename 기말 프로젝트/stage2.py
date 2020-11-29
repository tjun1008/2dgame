from pico2d import *
from gobj import *
import gfw
from monster import Monster

class Stage2:
    def __init__(self):
        global grass,background, portal
        portal = Portal2()
        background = load_image('image/background1.png')
        grass = Grass()
        Monster.load_all_images()
        global zombie_time

        zombie_time = 3


    def draw(self):
        #global zombie_time
        background.draw(640, 360)
        grass.draw()
        portal.draw()

    def update(self):
       global zombie_time
       #zombie_time -= gfw.delta_time
       zombie_time -= 1
       if zombie_time >= 0:
           gfw.world.add(gfw.layer.monster, Monster())


           # zombie_time = 5




class Grass:
    def __init__(self):
        self.image = load_image(RES_DIR + '/grass1.png')
        self.grass1 = load_image(RES_DIR + '/Tile_10.png')
        self.grass2 = load_image(RES_DIR + '/Tile_11.png')
        self.grass3 = load_image(RES_DIR + '/Tile_12.png')
        self.ladder = load_image(RES_DIR + '/ladder1.png')
    def draw(self):
        self.image.draw(640, 30)
        self.grass1.draw(30, 600)
        self.grass2.draw(230, 600)
        self.grass3.draw(480, 600)

        self.grass1.draw(480, 300)
        self.grass2.draw(720, 300)
        self.grass3.draw(960, 300)

        self.ladder.draw(480, 450)
        self.ladder.draw(960, 170)

    def update(self):
        pass

class Portal2:
    def __init__(self):
        self.image = gfw.image.load(RES_DIR + '/portal.png')
        self.pos = (1100,100)

    def draw(self):
        self.image.draw(*self.pos)

    def update(self):
        pass

    def get_bb(self):
        hw = 20
        hh = 40
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh