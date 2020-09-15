from pico2d import *
open_canvas()
grass = load_image("image/"+'grass.png')
character = load_image("image/"+'run_animation.png')
x = 0
frame = 0
while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas() #화면 플리핑, 화면지우기
    frame = (frame + 1) % 8
    # frame += 1
    # if frame >= 8: frame =0
    x += 5
    delay(0.05)
    get_events()
close_canvas()
