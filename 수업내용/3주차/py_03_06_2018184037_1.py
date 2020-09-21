from pico2d import *
from helper import *
import random


# 게임 오브젝트 클래스의 정의를 여기에

class Grass:
    def __init__(self):
        self.image = load_image('../res/grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('../res/run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        # self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    global arrive
    global delta
    global target
    global pos
    global speed
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            speed = speed + 1
            # print(speed)
            pos = (boy.x, boy.y)
            target = (event.x, get_canvas_height() - 1 - event.y)

            # print(move_toward(pos, delta, target))
            pos, arrive = move_toward(pos, delta(pos, target, speed), target)  # speed : 5
            boy.x, boy.y = pos
            # boy.x, boy.y = event.x, get_canvas_height()- 1-event.y
            # event.x 및 y는, 윈도우 API 의 좌표계를 따름.
            # pico2d 좌표계 변환 필요.
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# 초기화 코드
open_canvas()
boy = Boy()
grass = Grass()
running = True
arrive = True
speed = 1
list = []

# 게임 루프 코드
while running:
    clear_canvas()
    grass.draw()
    if arrive != True:
        pos, arrive = move_toward(pos, delta(pos, target, speed), target)  # speed : 5
        boy.x, boy.y = pos
    else:
        speed = 0
    boy.draw()
    update_canvas()
    handle_events()
    boy.update()
    delay(0.05)

# 종료 코드
close_canvas()
