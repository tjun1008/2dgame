import gfw
from pico2d import *
from gobj import *
from player import Player
from ball import Ball
from ball_L import Ball_L

def enter():
    gfw.world.init(['bg', 'enemy', 'ball', 'player', 'ui'])
    global grass, player,background,portal
    portal = load_image('image/portal.png')
    background = load_image('image/background.png')
    grass = Grass()
    player = Player()

def update():
    player.update()
    for b in Ball.balls: b.update()
    for b in Ball_L.balls: b.update()

def draw():
    background.draw(640, 360)
    grass.draw()
    portal.draw(1100,650)
    for b in Ball.balls: b.draw()
    for b in Ball_L.balls: b.draw()
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
