from pico2d import *
from gobj import *

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# 초기화 코드
open_canvas()
boy = Boy()
grass = Grass()
running = True

team = [Boy() for i in range(11)] #객체 생성



# 게임 루프 코드
while running:
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    handle_events()
    for boy in team:
        boy.update()
    delay(0.05)

# 종료 코드
close_canvas()