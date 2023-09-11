from pygame import *

init()

WIDTH = 600
HEIGHT = 400
BLACK = (0, 0, 0)
back = (100, 200, 100)

snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_block = 10

game = True

move_x = 0
move_y = 0

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Змейка')

while game:
    mw.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False

    draw.rect(mw, BLACK, (snake_x, snake_y, snake_block, snake_block))

    display.update()
    time.delay(50)
