from pico2d import *


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, get_canvas_height()- 1-event.y #마우스가 이동하면, SDL_MOUSEMOTION 이벤트가 발생
            # event.x 및 y는, 윈도우 API 의 좌표계를 따름.
            # pico2d 좌표계 변환 필요.
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()
grass = load_image("image/"+'grass.png')
character = load_image("image/"+'run_animation.png')

running = True
x, y = 0,0
frame = 0
hide_cursor()

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
