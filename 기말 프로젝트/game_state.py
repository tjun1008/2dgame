import gfw
from pico2d import *
from gobj import *
from player import Player

def enter():
    global grass, player,background
    background = load_image('image/background.png')
    grass = Grass()
    player = Player()

def update():
    player.update()
    #for b in Ball.balls: b.update()

def draw():
    background.draw(640, 360)
    grass.draw()
    #for b in Ball.balls: b.draw()
    player.draw()

def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)
    #Boy.handle_event(boy, e)

    # print(balls)
def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
