import pygame_menu

from pygame import *
from random import randrange

init()
font.init()

font_style = font.SysFont('comicsansms', 20)

WIDTH = 600
HEIGHT = 400
BLACK = (0, 0, 0)
RED = (255, 0, 0)
back = (200, 200, 200)

mw = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Змейка')

snake_block = 10
speed = 10
body_snake = []

def start_the_game():
    length = 0
    snake_x = WIDTH // 2
    snake_y = HEIGHT // 2
    game = True
    move_x = 0
    move_y = 0
    food_x = randrange(0, WIDTH, snake_block)
    food_y = randrange(0, HEIGHT, snake_block)

    while game:

        mw.fill(back)
        score = font_style.render(f'Количество очков: {length}', True, RED)
        mw.blit(score, (10, 20))
        for e in event.get():
            if e.type == QUIT:
                game = False
            if e.type == KEYDOWN and e.key == K_LEFT and move_x != speed:
                move_x = -speed
                move_y = 0
            if e.type == KEYDOWN and e.key == K_RIGHT and move_x != -speed:
                move_x = speed
                move_y = 0
            if e.type == KEYDOWN and e.key == K_UP and move_y != speed:
                move_y = -speed
                move_x = 0
            if e.type == KEYDOWN and e.key == K_DOWN and move_y != -speed:
                move_y = speed
                move_x = 0
        snake_x += move_x
        snake_y += move_y
        draw.rect(mw, BLACK, (snake_x, snake_y, snake_block, snake_block))
        draw.rect(mw, RED, (food_x, food_y, snake_block, snake_block))

        snake_head = [snake_x, snake_y]

        body_snake.append(snake_head)
        for x in body_snake:
            draw.rect(mw, BLACK, (x[0], x[1], snake_block, snake_block))

        # удаляем квадраты с того момента, как тело становится больше допустимой длины
        if len(body_snake) > length:
            del body_snake[0]
        if snake_x == food_x and snake_y == food_y:
            food_x = randrange(0, WIDTH, snake_block)
            food_y = randrange(0, HEIGHT, snake_block)
            length += 1
        # нельзя касаться тела
        for x in body_snake[:-1]:
            if x == snake_head:
                # print('сам себя')
                game = False
                body_snake.clear()
        if snake_x > WIDTH or snake_x < 0 or snake_y > HEIGHT or snake_y < 0:
            # print("стена")
            game = False
            body_snake.clear()

        display.update()
        time.delay(50)


menu = pygame_menu.Menu('Алгоритмика', 400, 300,
                        theme=pygame_menu.themes.THEME_BLUE)
submenu_theme = pygame_menu.themes.THEME_BLUE.copy()

info = pygame_menu.Menu(
    height=HEIGHT,
    theme=submenu_theme,
    title='Школа программирования',
    width=WIDTH
)
ABOUT = ['Международная школа программирования Алгоритмика',
         'Каналы на Youtube:',
         '@algoritmikakz, @algoritmikaby, @FunCode.school',
         'Автор: Евгений']
for m in ABOUT:
    info.add.label(m, align=pygame_menu.locals.ALIGN_CENTER, font_size=20)

menu.add.text_input('Name :', default='Eugene')
menu.add.button('Play', start_the_game)
menu.add.button('About', info)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(mw)

