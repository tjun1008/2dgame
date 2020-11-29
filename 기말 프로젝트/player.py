import random
from pico2d import *
import gfw
from gobj import *
from ball import Ball
from ball_L import Ball_L
#import helper

class IdleState:
    @staticmethod
    def get(player):
        if not hasattr(IdleState, 'singleton'): 
            IdleState.singleton = IdleState()
            IdleState.singleton.player = player
        return IdleState.singleton

    def __init__(self):
        self.image = gfw.image.load(RES_DIR + '/Magic_Girl_Idle_animation.png')


    def enter(self):
        self.time = 0
        self.fidx = 0
    def exit(self):
        pass
    def draw(self):
        width = 100
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, 122, *self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        # self.player.pos = point_add(self.player.pos, self.player.delta)
        move_obj(self.player)
        self.player.pos = point_add(self.player.pos, self.player.delta)
        frame = self.time * 15
       # self.fidx = int(frame) % 5
        self.fidx = int(frame) % 8

    def fire(self):
        self.ball = Ball(self.player.pos, (5, 5))
        gfw.world.add(gfw.layer.ball, self.ball)
        #print('Ball count = %d' % len(Ball.balls))

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.player.delta = point_add(self.player.delta, Player.KEY_MAP[pair])
            if pair == (SDL_KEYDOWN, SDLK_RIGHT):
                self.player.set_state(Rightrun)
            if pair == (SDL_KEYDOWN, SDLK_LEFT):
                self.player.set_state(Leftrun)
            if pair == (SDL_KEYDOWN, SDLK_UP):
                self.player.set_state(Up)
            if pair == (SDL_KEYDOWN, SDLK_DOWN):
                self.player.set_state(Up)
        elif pair == Player.KEYDOWN_SPACE:
            self.fire()

class IdleState_L:
    @staticmethod
    def get(player):
        if not hasattr(IdleState_L, 'singleton'):
            IdleState_L.singleton = IdleState_L()
            IdleState_L.singleton.player = player
        return IdleState_L.singleton

    def __init__(self):
        self.image = gfw.image.load(RES_DIR + '/Magic_Girl_Idle_animation_L.png')

    def enter(self):
        self.time = 0
        self.fidx = 0
    def exit(self):
        pass
    def draw(self):
        width = 100
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, 122, *self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        move_obj(self.player)
        self.player.pos = point_add(self.player.pos, self.player.delta)
        frame = self.time * 15
       # self.fidx = int(frame) % 5
        self.fidx = int(frame) % 8

    def L_fire(self):
        self.ball_L = Ball_L(self.player.pos, (5, 5))
        gfw.world.add(gfw.layer.ball, self.ball_L)


    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.player.delta = point_add(self.player.delta, Player.KEY_MAP[pair])
            if pair == (SDL_KEYDOWN, SDLK_RIGHT):
                self.player.set_state(Rightrun)
            if pair == (SDL_KEYDOWN, SDLK_LEFT):
                self.player.set_state(Leftrun)
            if pair == (SDL_KEYDOWN, SDLK_UP):
                self.player.set_state(Up)
            if pair == (SDL_KEYDOWN, SDLK_DOWN):
                self.player.set_state(Up)
        elif pair == Player.KEYDOWN_SPACE:
            self.L_fire()

class Rightrun:
    @staticmethod
    def get(player):
        if not hasattr(Rightrun, 'singleton'):
            Rightrun.singleton = Rightrun()
            Rightrun.singleton.player = player
        return Rightrun.singleton

    def __init__(self):
        self.image = gfw.image.load(RES_DIR + '/Magic_Girl_Walk_Right_animation.png')

    def enter(self):
        self.time = 0
        self.fidx = 0
    def exit(self):
        pass
    def draw(self):
        width = 80
        sx = self.fidx * width
        #x,y = self.player.pos
        self.image.clip_draw(sx, 0, width, 122, *self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        move_obj(self.player)
        self.player.pos = point_add(self.player.pos, self.player.delta)
        frame = self.time * 15
        self.fidx = int(frame) % 6

    def fire(self):
        self.ball = Ball(self.player.pos, (5,5))
        gfw.world.add(gfw.layer.ball, self.ball)
        #Ball.balls.append(self.ball)
        #print('Ball count = %d' % len(Ball.balls))

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.player.delta = point_add(self.player.delta, Player.KEY_MAP[pair])
            if e.type == SDL_KEYUP: self.player.set_state(IdleState)
            if pair == (SDL_KEYDOWN, SDLK_RIGHT):
                self.player.set_state(Rightrun)
            if pair == (SDL_KEYDOWN, SDLK_LEFT):
                self.player.set_state(Leftrun)
            if pair == (SDL_KEYDOWN, SDLK_UP):
                self.player.set_state(Up)
            if pair == (SDL_KEYDOWN, SDLK_DOWN):
                self.player.set_state(Up)
        elif pair == Player.KEYDOWN_SPACE:
            self.fire()

class Leftrun:
    @staticmethod
    def get(player):
        if not hasattr(Leftrun, 'singleton'):
            Leftrun.singleton = Leftrun()
            Leftrun.singleton.player = player
        return Leftrun.singleton

    def __init__(self):
        self.image = gfw.image.load(RES_DIR + '/Magic_Girl_Walk_animation.png')

    def enter(self):
        self.time = 0
        self.fidx = 0
    def exit(self):
        pass
    def draw(self):
        width = 105
        sx = self.fidx * width
        #x,y = self.player.pos
        self.image.clip_draw(sx, 0, width, 122, *self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        move_obj(self.player)
        self.player.pos = point_add(self.player.pos, self.player.delta)
        frame = self.time * 15
        self.fidx = int(frame) % 6

    def L_fire(self):
        self.ball_L = Ball_L(self.player.pos, (5, 5))
        gfw.world.add(gfw.layer.ball, self.ball_L)

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.player.delta = point_add(self.player.delta, Player.KEY_MAP[pair])
            if e.type == SDL_KEYUP: self.player.set_state(IdleState_L)
            if pair == (SDL_KEYDOWN, SDLK_RIGHT):
                self.player.set_state(Rightrun)
            if pair == (SDL_KEYDOWN, SDLK_LEFT):
                self.player.set_state(Leftrun)
            if pair == (SDL_KEYDOWN, SDLK_UP):
                self.player.set_state(Up)
            if pair == (SDL_KEYDOWN, SDLK_DOWN):
                self.player.set_state(Up)
        elif pair == Player.KEYDOWN_SPACE:
            self.L_fire()


class Up:
    @staticmethod
    def get(player):
        if not hasattr(Up, 'singleton'):
            Up.singleton = Up()
            Up.singleton.player = player
        return Up.singleton

    def __init__(self):
        self.image = gfw.image.load(RES_DIR + '/Magic_Girl_Walk_up_animation.png')

    def enter(self):
        self.time = 0
        self.fidx = 0
    def exit(self):
        pass
    def draw(self):
        width = 71
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, 122, *self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        self.player.pos = point_add(self.player.pos, self.player.delta)
        move_obj(self.player)
        frame = self.time * 15
       # self.fidx = int(frame) % 5
        self.fidx = int(frame) % 8



    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            if e.type == SDL_KEYUP: self.player.set_state(IdleState)
            self.player.delta = point_add(self.player.delta, Player.KEY_MAP[pair])
            if pair == (SDL_KEYDOWN, SDLK_RIGHT):
                self.player.set_state(Rightrun)
            if pair == (SDL_KEYDOWN, SDLK_LEFT):
                self.player.set_state(Leftrun)
        elif pair == Player.KEYDOWN_SPACE:
            pass

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    image = None

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 100, 110
        self.delta = 0, 0
        self.fidx = 0
        self.target = None
        self.targets = []
        self.speed = 0
        self.time = 0
        #self.firestate = False
        self.state = None
        self.set_state(IdleState)

    def set_state(self, clazz):
        if self.state != None:
            self.state.exit()
        self.state = clazz.get(self)
        self.state.enter()

    def draw(self):
        self.state.draw()


    def update(self):
        self.state.update()


    def handle_event(self, e):
        self.state.handle_event(e)

    def get_bb(self):
        hw = 20
        hh = 40
        x, y = self.pos
        return x - hw, y - hh, x + hw, y + hh

