import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
SNAKE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Load the apple image and adjust the scale factor
apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (GRID_SIZE, GRID_SIZE))

# Initialize Snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (1, 0)

# Initialize Apple
apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Score
score = 0

# Game clock
clock = pygame.time.Clock()
playtime = 0

# Game loop
running = True
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for arrow key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -1):
        snake_direction = (0, 1)
    elif keys[pygame.K_LEFT] and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-1, 0):
        snake_direction = (1, 0)

    # Move the Snake
    x, y = snake[0]
    new_head = (x + snake_direction[0], y + snake_direction[1])

    # Check if the snake collides with the wall or itself
    if new_head[0] < 0:
        new_head = (GRID_WIDTH - 1, new_head[1])
    elif new_head[0] >= GRID_WIDTH:
        new_head = (0, new_head[1])
    elif new_head[1] < 0:
        new_head = (new_head[0], GRID_HEIGHT - 1)
    elif new_head[1] >= GRID_HEIGHT:
        new_head = (new_head[0], 0)

    if new_head in snake:
        running = False

    # Check if the snake eats the apple
    if new_head == apple:
        snake.insert(0, apple)
        apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        score += 1

    else:
        snake.insert(0, new_head)
        snake.pop()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the Apple
    screen.blit(
        apple_img, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE)
    )

    # Update the scoreboard
    score_text = f"Score: {score}"
    score_text_render = pygame.font.Font(None, 36).render(score_text, True, WHITE)
    screen.blit(score_text_render, (10, 10))

    # Update playtime
    elapsed_time = pygame.time.get_ticks() - start_time
    playtime = elapsed_time / 1000
    playtime_text = f"Playtime: {playtime:.1f} seconds"
    playtime_text_render = pygame.font.Font(None, 24).render(playtime_text, True, WHITE)
    screen.blit(playtime_text_render, (WIDTH - playtime_text_render.get_width() - 10, 10))

    # Draw the Snake
    for i, segment in enumerate(snake):
        if i == 0:
            # Draw the snake's head in green
            pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        else:
            # Draw the rest of the snake in white
            pygame.draw.rect(screen, WHITE, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.update()

    # Control the game speed
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
