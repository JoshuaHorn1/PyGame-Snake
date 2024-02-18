# Imports & Initialisations...
import pygame
import random
pygame.init()

# Variables...
SCREEN = pygame.display.set_mode((1000, 720))  # display settings
GAME_ICON = pygame.image.load('snake_icon.png')

SCORE_FONT = pygame.font.SysFont("snake chan.ttf", 20)  # fonts
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
    snake_x = 480  # centre point horizontally is (1000-20 snake width)/2 = 490
    snake_y = 340  # centre point vertically is (720-20 snake height)/2 = 350
    snake_x_change = 0  # holds the values of changes in the x-coordinate
    snake_y_change = 0  # holds the values of changes in the y-coordinate
    snake_list = []
    snake_length = 1
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

        # Handling response if user presses 'X' - give them the option to start
        # a new game, or keep playing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions = "Exit: 'Q' to Quit, SPACE to Resume, " \
                               "'R' to Reset"
                message(instructions, WHITE, BLACK)
                pygame.display.update()

                end = False
                while not end:
                    for event in pygame.event.get():
                        # If user presses X button, the game quits
                        if event.type == pygame.QUIT:
                            quit_game = True
                            end = True
                        if event.type == pygame.KEYDOWN:
                            # If user presses 'R' button, game is reset
                            if event.key == pygame.K_r:
                                end = True, game_loop()
                            # If user presses the space-bar,
                            # then game continues
                            if event.key == pygame.K_SPACE:
                                end = True
                            # If user presses 'Q' button, game quits
                            if event.key == pygame.K_q:
                                quit_game = True
                                end = True

            # Converts user key press to snake movement
            if event.type == pygame.KEYDOWN:
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
            game_over = True

        # Create snake (replaces rectangle in previous version)
        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
        draw_snake(snake_list)

        # Keep track of the player's score
        score = snake_length - 1
        player_score(score, WHITE)

        # Link speed of snake to player score - increasing difficulty
        if score > 3:
            speed = score
        else:
            speed = 3

        # Using a sprite (instead of the previous circle) to represent food
        food = pygame.Rect(food_x, food_y, 20, 20)
        apple = pygame.image.load('apple_3.png').convert_alpha()
        resized_apple = pygame.transform.smoothscale(apple, [20, 20])
        SCREEN.blit(resized_apple, food)
        pygame.display.update()
        # Detects collision between snake and food
        if snake_x == food_x and snake_y == food_y:
            # Gives food a new random position
            food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
            food_y = round(random.randrange(20, 720 - 20) / 20) * 20

            # Increase the length of the snake (by original size)
            snake_length += 1

        clock.tick(speed)  # sets the speed at which each iteration of the game loop
        # runs in frames per second (fps). In this case, it is set to 5 fps

    pygame.quit()
    quit()


def message(msg, txt_colour, bkg_colour):
    txt = MSG_FONT.render(msg, True, txt_colour, bkg_colour)
    # Centre rectangle: 1000/2 = 500 and 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))
    SCREEN.blit(txt, text_box)


def draw_snake(snake_list):
    for i in snake_list:
        pygame.draw.rect(SCREEN, RED, [i[0], i[1], 20, 20])


# Display player score throughout the game
def player_score(score, score_colour):
    display_score = SCORE_FONT.render(f"Score: {score}", True, score_colour)
    SCREEN.blit(display_score, (940, 700))  # coordinates for top-right


# Main...
pygame.display.set_icon(GAME_ICON)  # Displays screen
pygame.display.set_caption("Totally Accurate Worm Simulator")
game_loop()
