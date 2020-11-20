from pico2d import *
from gobj import *
import gfw

class Ball:
    balls = []

    def __init__(self, pos, delta):
        self.image = gfw.image.load(RES_DIR + '/Fireball_Effect_05.png')
        self.pos = pos
        self.delta = delta
        self.radius = self.image.h // 2


        # print('Radius = %d' % self.radius)

    def draw(self):
        self.image.draw(*self.pos)

    def update(self):
        x, y = self.pos
        dx, dy = self.delta
        x += dx
        # y += dy
        # gravity = 0.1
        # dy -= gravity


        if x < -100 or x > get_canvas_width() + 100:
            if len(Ball.balls)>0:
                Ball.balls.remove(self)
                print('Ball count - %d' % len(Ball.balls))


        self.pos = x, y
        self.delta = dx, dy

