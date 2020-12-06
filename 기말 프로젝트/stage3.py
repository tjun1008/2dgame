from pico2d import *
from gobj import *
import gfw
from monster2 import Monster2
from background import HorzScrollBackground

class Stage3:
    def __init__(self):
        global grass,bg, portal
        portal = Portal3()
        for n, speed in [(1, 30)]:
            bg = HorzScrollBackground('image/background1.png')
            bg.speed = speed
        grass = Grass()
        Monster2.load_all_images()
        global zombie_time

        zombie_time = 4

    def draw(self):
        bg.draw()
        grass.draw()
        portal.draw()

    def update(self):
        bg.update()
        global zombie_time
        # zombie_time -= gfw.delta_time
        zombie_time -= 1

        if zombie_time >= 0:
            gfw.world.add(gfw.layer.monster, Monster2())



class Grass:
    def __init__(self):
        self.tile1 = load_image(RES_DIR + '/Tile_2.png')
        self.grass1 = load_image(RES_DIR + '/Tile_13.png')
        self.grass2 = load_image(RES_DIR + '/Tile_14.png')
        self.grass3 = load_image(RES_DIR + '/Tile_15.png')
        self.ladder = load_image(RES_DIR + '/ladder1.png')
    def draw(self):
        self.tile1.draw(0, 30)
        self.tile1.draw(256, 30)

        self.grass2.draw(480, 30)
        self.grass1.draw(480, 286)
        self.ladder.draw(340, 170)

        self.tile1.draw(710, 286)
        self.tile1.draw(966, 286)
        self.tile1.draw(1222, 286)



    def update(self):
        pass

class Portal3:
    def __init__(self):
        self.image = gfw.image.load(RES_DIR + '/portal.png')
        self.pos = (1150,350)

    def draw(self):
        self.image.draw(*self.pos)

    def update(self):
        pass

    def get_bb(self):
        hw = 20
        hh = 40
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh