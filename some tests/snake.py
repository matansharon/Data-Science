import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Define snake properties
snake_size = 20
snake_speed = 15

# Define font for displaying score
font = pygame.font.SysFont(None, 30)

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(window, white, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
    target_y = round(random.randrange(0, height - snake_size) / snake_size) * snake_size

    while not game_over:

        while game_close:
            window.fill(black)
            game_over_message = font.render("Game Over! Press Q to Quit or C to Play Again", True, red)
            window.blit(game_over_message, [width / 3, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        run_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                elif event.key == pygame.K_UP:
                    y_speed = -snake_size
                    x_speed = 0
                elif event.key == pygame.K_DOWN:
                    y_speed = snake_size
                    x_speed = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        window.fill(black)
        pygame.draw.rect(window, red, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)

        score = font.render("Score: " + str(snake_length - 1), True, white)
        window.blit(score, [0, 0])

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / snake_size) * snake_size
            target_y = round(random.randrange(0, height - snake_size) / snake_size) * snake_size
            snake_length += 1

        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()