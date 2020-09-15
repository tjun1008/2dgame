from pico2d import *

open_canvas()
grass = load_image("image/"+'grass.png')
character = load_image("image/"+'character.png')
x = 0
while (x < 800):
    clear_canvas_now() #캔버스를 지우고 다시그리는걸 반복
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)
close_canvas()