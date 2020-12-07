from pico2d import *
from gobj import *
import gfw
from monster3 import Monster3
from background import HorzScrollBackground

class Stage4:
    def __init__(self):
        global grass,bg, portal
        portal = Portal4()
        for n, speed in [(1, 30)]:
            bg = HorzScrollBackground('image/background1.png')
            bg.speed = speed
        grass = Grass()

        Monster3.load_all_images()
        global zombie_time

        zombie_time = 5

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
            gfw.world.add(gfw.layer.monster, Monster3())



class Grass:
    def __init__(self):
        self.image = load_image(RES_DIR + '/grass1.png')
        self.grass1 = load_image(RES_DIR + '/Tile_10.png')
        self.grass2 = load_image(RES_DIR + '/Tile_11.png')
        self.grass3 = load_image(RES_DIR + '/Tile_12.png')
        self.ladder = load_image(RES_DIR + '/ladder1.png')



        
    def draw(self):
        self.image.draw(640, 30)

        self.grass1.draw(30, 300)
        self.grass3.draw(230, 300)

        self.grass1.draw(490, 300)
        self.grass3.draw(730, 300)

        self.grass1.draw(900, 300)
        self.grass3.draw(1100, 300)

        self.ladder.draw(100, 170)
        self.ladder.draw(500, 170)
        self.ladder.draw(970, 170)

    def update(self):
        pass

class Portal4:
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