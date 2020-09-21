from pico2d import *

def handle_events():
    global running #전역변수
    global dir

    events = get_events() #이벤트들이 담긴 리스트가 넘어옴
    for event in events: #이벤트를 하나씩 꺼내서 확인함
        if event.type == SDL_QUIT: #윈도우 종료시 발생
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1 #중립
            elif event.key == SDLK_LEFT:
                dir += 1 #중립


open_canvas()
grass = load_image("image/"+'grass.png')
character = load_image("image/"+'run_animation.png')

running = True
x = 0
frame = 0
dir = 0 #변수 dir 을 이용하여, x 축상의 방향을 표시

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas() #업데이트
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.01)
