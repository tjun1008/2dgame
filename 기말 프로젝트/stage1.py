from pico2d import *
from gobj import *
import gfw

class Stage1:
    def __init__(self):
        global grass,background, portal
        portal = Portal()
        background = load_image('image/background.png')
        grass = Grass()

    def draw(self):
        background.draw(640, 360)
        grass.draw()
        portal.draw()

    def update(self):
        pass



class Grass:
    def __init__(self):
        self.image = load_image(RES_DIR + '/grass1.png')
        self.grass1 = load_image(RES_DIR + '/Tile_10.png')
        self.grass2 = load_image(RES_DIR + '/Tile_11.png')
        self.grass3 = load_image(RES_DIR + '/Tile_12.png')
        self.ladder = load_image(RES_DIR + '/ladder1.png')
    def draw(self):
        self.image.draw(640, 30)
        self.grass1.draw(150, 300)
        self.grass2.draw(400, 300)
        self.grass3.draw(650, 300)

        self.grass1.draw(650, 600)
        self.grass2.draw(900, 600)
        self.grass3.draw(1150, 600)

        self.ladder.draw(150, 170)
        self.ladder.draw(650, 440)

    def update(self):
        pass

class Portal:
    def __init__(self):
        self.image = gfw.image.load(RES_DIR + '/portal.png')
        self.pos = (1100,650)

    def draw(self):
        self.image.draw(*self.pos)

    def update(self):
        pass

    def get_bb(self):
        hw = 20
        hh = 40
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh