import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

width = 800
height = 600

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()

grid_size = 10

# Fonts
font_style = pygame.font.SysFont(None, 24)
score_font = pygame.font.SysFont(None, 20)


def display_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    window.blit(value, [0, 0])


def display_serpent(grid_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], grid_size, grid_size])


def message(text, color):
    msg = font_style.render(text, True, color)
    window.blit(msg, [width / 6, height / 3])


def game():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_size = 1
    snake_speed = 5

    apple_x = round(random.randrange(0, width - grid_size) / 10.0) * 10.0
    apple_y = round(random.randrange(0, height - grid_size) / 10.0) * 10.0

    while not game_over:

        while game_close:
            window.fill(white)
            message("Tu as perdu ! Appuie sur Q-Quitter ou C-Continuer", red)
            display_score(snake_size - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -grid_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = grid_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -grid_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = grid_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(green)
        pygame.draw.rect(window, red, [apple_x, apple_y, grid_size, grid_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_size:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        display_serpent(grid_size, snake_list)
        display_score(snake_size - 1)

        pygame.display.update()

        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, width - grid_size) / 10.0) * 10.0
            apple_y = round(random.randrange(0, height - grid_size) / 10.0) * 10.0
            snake_speed += 1
            snake_size += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game()