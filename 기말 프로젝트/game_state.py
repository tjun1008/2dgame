import gfw
from pico2d import *
from gobj import *
from player import Player
from ball import Ball
from ball_L import Ball_L
from stage1 import  Stage1,Portal
from stage2 import  Stage2



def enter():
    gfw.world.init(['bg', 'enemy', 'ball', 'player','potal' 'ui'])
    global player,stage1,portal,stage2
    portal = Portal()
    stage1 = Stage1()
    stage2 = Stage2()
    player = Player()

    global map
    map = 1

def update():
    global stage1,map
    gfw.world.update()
    player.update()
    for b in Ball.balls: b.update()
    for b in Ball_L.balls: b.update()

    if collides_box(player, portal):
        print("COLLISION")
        player.pos = 100, 110
        del(stage1)
        map = 2



def draw():
    if(map == 1):
        stage1.draw()
    elif map ==2:
        stage2.draw()

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

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
