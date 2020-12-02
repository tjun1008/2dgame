import gfw
from pico2d import *
from gobj import *
from player import Player
from ball import Ball
from ball_L import Ball_L
from stage1 import  Stage1,Portal1
from stage2 import  Stage2,Portal2
from stage3 import  Stage3,Portal3
from stage4 import  Stage4,Portal4
from stage5 import  Stage5
from boss_monster import  Boss_monster
from monster import  Monster
from monster2 import  Monster2
from monster3 import  Monster3

STATE_IN_GAME,STATE_GAME_OVER,STATE_GAME_CLEAR = range(3)

def enter():
    gfw.world.init(['bg', 'monster', 'ball', 'player','portal','ui'])
    global player,stage1,stage2,stage3,stage4,stage5,portal1,portal2,portal3,portal4
    global image,image1,state
    portal1 = Portal1()
    portal2 = Portal2()
    portal3 = Portal3()
    portal4 = Portal4()
    #gfw.world.add(gfw.layer.portal, portal)

    stage1 = Stage1()
    stage2 = Stage2()
    stage3 = Stage3()
    stage4 = Stage4()
    stage5 = Stage5()


    player = Player()
    gfw.world.add(gfw.layer.player,player)

    image = load_image('image/clear.png')
    image1 = load_image('image/gameover.png')

    global map
    map = 1

    state = STATE_IN_GAME
    #global zombie_time
    #zombie_time = 2

def update():
    global stage1,stage2,stage3,stage4,stage5,map
    global state
    gfw.world.update()
    #player.update()
    #for b in Ball.balls: b.update()
    #for b in Ball_L.balls: b.update()


    if collides_box(player, portal1):
        player.pos = 30, 650
        del (stage1)
        map += 1
        print(map)

    if Monster.Over == True or Monster2.Over == True or Monster3.Over == True:
        end_game()



    if map ==2:
        stage2.update()
        if collides_box(player, portal2):
            player.pos = 100, 110
            del (stage2)
            map += 1
            print(map)

    if map == 3:
        stage3.update()
        if collides_box(player, portal3):
            player.pos = 100, 110
            del (stage3)
            map += 1
            print(map)

    if map == 4:
        stage4.update()
        if collides_box(player, portal4):
            player.pos = 100, 110
            del (stage4)
            map += 1
            print(map)

    if map ==5:
        stage5.update()
        if Boss_monster.finish == True:
            del (stage5)
            clear_game()
            map +=1


    #global zombie_time
    #zombie_time -= 1

    #if zombie_time >= 0:
        #gfw.world.add(gfw.layer.monster, Boss_monster())


def clear_game():
    global state
    print('Dead')
    gfw.world.remove(player)
    state = STATE_GAME_CLEAR

def end_game():
    global state
    print('Dead')
    gfw.world.remove(player)
    state = STATE_GAME_OVER


def draw():
    global state
    global image

    if(map == 1):
        stage1.draw()
    elif map ==2:
        stage2.draw()
    elif map ==3:
        stage3.draw()
    elif map == 4:
        stage4.draw()
    elif map == 5:
        stage5.draw()

    if state == STATE_GAME_OVER:
        image1.draw(640,360)

    if state == STATE_GAME_CLEAR:
        image.draw(640,360)


    #for b in Ball.balls: b.draw()
    #for b in Ball_L.balls: b.draw()
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
