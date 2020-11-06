import random
from pico2d import *

RES_DIR = 'image'

def rand(val):
    return val * random.uniform(0.9, 1.1)

def point_add(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return x1+x2, y1+y2

def move_obj(obj):
    obj.pos = point_add(obj.pos, obj.delta)

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


if __name__ == "__main__":
	print("Running test code ^_^")
