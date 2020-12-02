from pico2d import *
from gobj import *
import gfw

class Item:
    def __init__(self, item, x,y):
        self.heart = load_image(RES_DIR + '/health_full.png')
        self.coin = load_image(RES_DIR + '/pngegg.png')

        self.item = item
        self.pos = (x,y)


    def draw(self):
        if self.item == 1:
            self.heart.draw(*self.pos,50,50)
        elif self.item == 2:
            self.coin.draw(*self.pos,50,50)

    def update(self):
        pass

    def get_bb(self):
        hw = 20
        hh = 40
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh