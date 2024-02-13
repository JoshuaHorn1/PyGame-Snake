# Imports & Initialisations...
import pygame
import random
pygame.init()

# Variables...
SCREEN = pygame.display.set_mode((1000, 720))  # display settings
GAME_ICON = pygame.image.load('snake_icon.png')

SCORE_FONT = pygame.font.SysFont("arialblack", 20)  # fonts
EXIT_FONT = pygame.font.Font("freesansbold.ttf", 20)
MSG_FONT = pygame.font.SysFont("arialblack", 20)

BLACK = (0, 0, 0)  # colour tuples
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (188, 227, 199)
YELLOW = (255, 255, 0)


# Functions...


def game_loop():
    # snake will be 20 x 20 pixels
    snake_x = 490  # centre point horizontally is (1000-20 snake width)/2 = 490
    snake_y = 350  # centre point vertically is (720-20 snake height)/2 = 350
    snake_x_change = 0  # holds the values of changes in the x-coordinate
    snake_y_change = 0  # holds the values of changes in the y-coordinate
    # Set random position for the food to start
    food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
    food_y = round(random.randrange(20, 720 - 20) / 20) * 20

    quit_game = False
    game_over = False
    clock = pygame.time.Clock()  # sets the speed that the snake moves

    while not quit_game:
        # Gives user the option to play again or quit upon death
        while game_over:
            message("You died! Press 'Q' to Quit, or 'A' to play Again",
                    BLACK, WHITE)
            pygame.display.update()
            # Check if user wants to play again (A) or quit (Q)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        quit_game = True
                        game_over = False
                    if event.key == pygame.K_a:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

        # Converts user key press to snake movement
        if event.type == pygame.KEYDOWN:  # Converts user key press to movement
            # if event.key == pygame.K_a:
            #     snake_x_change = -20
            #     snake_y_change = 0
            # elif event.key == pygame.K_d:
            #     snake_x_change = 20
            #     snake_y_change = 0
            # elif event.key == pygame.K_w:
            #     snake_x_change = 0
            #     snake_y_change = -20
            # elif event.key == pygame.K_s:
            #     snake_x_change = 0
            #     snake_y_change = 20
            if event.key == pygame.K_LEFT:
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
            game_over = True

        # Create rectangle for snake
        pygame.draw.rect(SCREEN, RED, [snake_x, snake_y, 20, 20])
        pygame.display.update()

        # Create circle for food
        pygame.draw.circle(SCREEN, YELLOW, [food_x, food_y], 10)
        pygame.display.update()
        # Detects collision between snake and food
        if snake_x == food_x - 10 and snake_y == food_y - 10:
            # Gives food a new random position
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 720 - 20) / 20) * 20

        clock.tick(5)  # sets the speed at which each iteration of the game loop
        # runs in frames per second (fps). In this case, it is set to 5 fps

    pygame.quit()
    quit()


def message(msg, txt_colour, bkg_colour):
    txt = MSG_FONT.render(msg, True, txt_colour, bkg_colour)
    # Centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    SCREEN.blit(txt, text_box)


# Main...
pygame.display.set_icon(GAME_ICON)  # Displays screen
pygame.display.set_caption("Totally Accurate Worm Simulator")
game_loop()
