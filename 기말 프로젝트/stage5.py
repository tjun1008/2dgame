from pico2d import *
from gobj import *
import gfw


class Stage5:
    def __init__(self):
        global grass,background
        background = load_image('image/background1.png')
        grass = Grass()



    def draw(self):
        background.draw(640, 360)
        grass.draw()

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


    def update(self):
        pass
