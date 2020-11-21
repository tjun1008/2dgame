import gfw
from pico2d import *
from gobj import *
from player import Player
from zombie import Zombie
from ball import Ball
from ball_L import Ball_L
from stage1 import  Stage1,Portal1
from stage2 import  Stage2,Portal2
from stage3 import  Stage3,Portal3
from stage4 import  Stage4,Portal4



def enter():
    gfw.world.init(['bg', 'monster', 'ball', 'player','portal','ui'])
    Zombie.load_all_images()
    global player,stage1,stage2,stage3,stage4,portal1,portal2,portal3,portal4
    portal1 = Portal1()
    portal2 = Portal2()
    portal3 = Portal3()
    #gfw.world.add(gfw.layer.portal, portal)

    stage1 = Stage1()
    stage2 = Stage2()
    stage3 = Stage3()
    stage4 = Stage4()

    player = Player()
    gfw.world.add(gfw.layer.player,player)

    global map
    map = 1

    global zombie_time
    zombie_time = 1

def update():
    global stage1,stage2,stage3,stage4,map
    gfw.world.update()
    player.update()
    for b in Ball.balls: b.update()
    for b in Ball_L.balls: b.update()

    if collides_box(player, portal1):
        player.pos = 30, 650
        del (stage1)
        map += 1
        print(map)

    if collides_box(player, portal2):
        player.pos = 100, 110
        del (stage2)
        map += 1
        print(map)

    if collides_box(player, portal3):
        player.pos = 100, 110
        del (stage3)
        map += 1
        print(map)

    global zombie_time
    zombie_time -= gfw.delta_time
    if zombie_time <= 0:
        gfw.world.add(gfw.layer.monster, Zombie())
        zombie_time = 5




def draw():

    if(map == 1):
        stage1.draw()
    elif map ==2:
        stage2.draw()
    elif map ==3:
        stage3.draw()
    elif map == 4:
        stage4.draw()

    for b in Ball.balls: b.draw()
    for b in Ball_L.balls: b.draw()
    #player.draw()
    gfw.world.draw()

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
