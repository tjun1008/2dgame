from pico2d import *
from gobj import *
import gfw

class Ball_L:
    SIZE = 150

    def __init__(self, pos, delta):
        self.image = gfw.image.load(RES_DIR + '/Fireball_Effect_05_L.png')
        self.pos = pos
        self.delta = delta
        self.radius = self.image.h // 2



    def draw(self):
        self.image.draw(*self.pos)

    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        x -= dx
        # y += dy
        # gravity = 0.1
        # dy -= gravity


        if x < -100 or x > get_canvas_width() + 100:
            if x < 0 + Ball_L.SIZE:
                gfw.world.remove(self)



        self.pos = x, y
        self.delta = dx, dy

    def get_bb(self):
        hw = 20
        hh = 40
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh

