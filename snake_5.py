# Imports & Initialisations
import pygame
pygame.init()

# Screen creation
SCREEN = pygame.display.set_mode((1000, 720))
GAME_ICON = pygame.image.load('snake_icon.png')
pygame.display.set_icon(GAME_ICON)
pygame.display.set_caption("Totally Accurate Worm Simulator")

# Tuples containing colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (188, 227, 199)

# Fonts
SCORE_FONT = pygame.font.SysFont("arialblack", 20)
EXIT_FONT = pygame.font.Font("freesansbold.ttf")

# snake will be 20 x 20 pixels
snake_x = 490  # centre point horizontally is (1000-20 snake width)/2 = 490
snake_y = 350  # centre point vertically is (720-20 snake height)/2 = 350
snake_x_change = 0  # holds the values of changes in the x-coordinate
snake_y_change = 0  # holds the values of changes in the y-coordinate

quit_game = False
clock = pygame.time.Clock()  # sets the speed that the snake moves

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True

    # Converts user key press to snake movement
    if event.type == pygame.KEYDOWN:  # Converts user key press to movement
        if event.key == pygame.K_a:
            snake_x_change = -20
            snake_y_change = 0
        elif event.key == pygame.K_d:
            snake_x_change = 20
            snake_y_change = 0
        elif event.key == pygame.K_w:
            snake_x_change = 0
            snake_y_change = -20
        elif event.key == pygame.K_s:
            snake_x_change = 0
            snake_y_change = 20
        elif event.key == pygame.K_LEFT:
            snake_x_change = -20
            snake_y_change = 0
        elif event.key == pygame.K_RIGHT:
            snake_x_change = 20
            snake_y_change = 0
        elif event.key == pygame.K_UP:
            snake_x_change = 0
            snake_y_change = -20
        elif event.key == pygame.K_DOWN:
            snake_x_change = 0
            snake_y_change = 20

    snake_x += snake_x_change
    snake_y += snake_y_change
    SCREEN.fill(BLACK)

    if snake_x >= 1000 or snake_x < 0 or snake_y >= 720 or snake_y < 0:
        pygame.quit()
        quit()

    # Create rectangle for snake
    pygame.draw.rect(SCREEN, RED, [snake_x, snake_y, 20, 20])
    pygame.display.update()

    clock.tick(10)  # sets the speed at which each iteration of the game loop
    # runs in frames per second (fps). In this case, it is set to 10 fps

pygame.quit()
quit()
