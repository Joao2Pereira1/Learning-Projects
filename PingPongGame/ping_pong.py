"""
This is a simple game of ping pong.
I used the pygame module for building this game.

Author: João Pereira
"""

import random
import sys

import pygame as py

py.init()

# *Colors

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)


# *Game Screen Interface

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # creating screen

# *GAME ICON
ICON_PATH = "craiyon_235937_dynamic_table_tennis_poster_design_with_vibrant_red_and_blue_colors.png"

clock = py.time.Clock()  # Frame rate

# *Rectangles

# Rectangles Dimensions
SURFACE = screen
RECT_WIDTH, RECT_HEIGHT = 10, 50
SPEED_RECT = 8

# Rectangles Positions
L_PADDLE_X = 20
L_PADDLE_Y = (SCREEN_HEIGHT / 2) - 25

R_PADDLE_X = SCREEN_WIDTH - 40
R_PADDLE_Y = (SCREEN_HEIGHT / 2) - 25


player1 = py.Rect(L_PADDLE_X, L_PADDLE_Y, RECT_WIDTH, RECT_HEIGHT)  # left paddle
player2 = py.Rect(R_PADDLE_X, R_PADDLE_Y, RECT_WIDTH, RECT_HEIGHT)  # right paddle

# *Ball

# ball dimensions
BALL_WIDTH, BALL_HEIGHT = 10, 10

# ball positions
BALL_X = (SCREEN_WIDTH / 2) - 5
BALL_Y = SCREEN_HEIGHT / 2

# ball speed
SPEED_BALL = 3.5
ball_speed_x = SPEED_BALL * random.choice([-1, 1])
ball_speed_y = SPEED_BALL

ball = py.Rect(BALL_X, BALL_Y, BALL_WIDTH, BALL_HEIGHT)  # ball object

# *score vars
score_player1 = 0
score_player2 = 0

# * GAME SOUND EFFECTS
py.mixer.init()
bounce_sound = py.mixer.Sound("bounce.mp3")
score_sound = py.mixer.Sound("score.mp3")


# * Menu Screen Interface
def menu_interface(winner: str) -> bool:
    """menu screen interface has options play game and exit game,
    if passed a empty str there is no winner, that means
    the game hasn't started, otherwise the game has finished
    Returns bool: True if play game, otherwise false"""

    screen.fill(WHITE)

    if winner:
        # write the winner on screen
        font = py.font.Font(None, 36)
        winner_text = font.render(winner, True, BLACK)
        menu_screen.blit(winner_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 - 20))

    # *GAME ICON
    programIcon = py.image.load(ICON_PATH)
    py.display.set_icon(programIcon)

    # *FONT
    font = py.font.Font(None, 36)
    text = font.render("Ping Pong Game", True, BLACK)
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
    menu_screen.blit(text, text_rect)  # colocar texto

    # * BUTTONS
    play_button = py.Rect(SCREEN_WIDTH / 2 - 95, SCREEN_HEIGHT / 2, 200, 50)
    exit_button = py.Rect(SCREEN_WIDTH / 2 - 95, SCREEN_HEIGHT / 2 + 50, 200, 50)

    # *DRAW BUTTONS
    py.draw.rect(menu_screen, BLACK, play_button, 2)
    py.draw.rect(menu_screen, BLACK, exit_button, 2)

    # *FONT FOR BUTTONS
    play_text = font.render("Play Game", True, BLACK)
    exit_text = font.render("Exit Game", True, BLACK)

    # *PLACE TEXT ON BUTTONS
    menu_screen.blit(play_text, (play_button.x + 20, play_button.y + 15))
    menu_screen.blit(exit_text, (exit_button.x + 20, exit_button.y + 15))

    py.display.flip()  # RENDER SCREEN

    # * EVENT HANDLER TO GET PLAYER INPUT(play or exit)
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            elif event.type == py.MOUSEBUTTONDOWN:
                # se o mouse estiver dentro do play button
                if play_button.collidepoint(event.pos):
                    return True
                # se o mouse estiver dentro do exit button
                elif event.type == py.MOUSEBUTTONDOWN:
                    if exit_button.collidepoint(event.pos):
                        return False


# *draw interface
def render():
    """
    The `render()` function in this Python code uses Pygame to render a game screen with paddles, a ball,
    a middle line, a scoreboard, and a game over screen, updating the display to show the changes made.
    """
    screen.fill(WHITE)

    # ? render paddles

    py.draw.rect(SURFACE, BLACK, player1)
    py.draw.rect(SURFACE, BLACK, player2)

    py.draw.ellipse(SURFACE, GREY, ball)  # ball

    py.draw.aaline(
        SURFACE, BLACK, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT)
    )  # middle line

    # ?scoreboard

    score_1 = f"Score 1: {score_player1}"
    score_2 = f"Score 2: {score_player2}"
    font = py.font.SysFont(None, 30)
    screen.blit(font.render(score_1, True, BLACK), (5, 5))
    screen.blit(font.render(score_2, True, BLACK), (SCREEN_WIDTH - 115, 5))

    # *game over screen

    py.display.flip()  # RENDER SCREEN


# *reset positions when someone scores
def reset_position():
    global ball_speed_x, ball_speed_y
    """
    The function `reset_position` sets the initial positions and speeds for the ball and players in a
    game.
    """

    # at start randomize the side where ball goes
    ball_speed_x = SPEED_BALL * random.choice([-1, 1])
    ball_speed_y = SPEED_BALL

    ball.x = (SCREEN_WIDTH / 2) - 5
    ball.y = SCREEN_HEIGHT / 2

    player1.x = 20
    player1.y = (SCREEN_HEIGHT / 2) - 25

    player2.x = SCREEN_WIDTH - 40
    player2.y = (SCREEN_HEIGHT / 2) - 25


game_over = False  # *variable to check if player 1 or 2 won

menu_screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # creating screen
menu_screen.fill(WHITE)
py.display.set_caption("Ping Pong")

# * menu screen
start_game = menu_interface("")  # get buttons input play or exit

if start_game:
    pass
else:
    sys.exit()

# *main loop
while True:

    # Event handling
    for i in py.event.get():
        # *exit game
        if i.type == py.QUIT:
            py.quit()
            sys.exit()

    # Players Controls
    keys = py.key.get_pressed()

    # Player 1 (W/S)
    if keys[py.K_w]:
        player1.y -= SPEED_RECT
    if keys[py.K_s]:
        player1.y += SPEED_RECT

    # Player 2 (U/J)
    if keys[py.K_u]:
        player2.y -= SPEED_RECT
    if keys[py.K_j]:
        player2.y += SPEED_RECT

    # *ball movement, the side where goes is random
    ball.x += int(ball_speed_x)
    ball.y += int(ball_speed_y)

    # *fields limits(to paddles dont go out of the fields)

    # player 1
    if -10 < player1.y < 0:
        player1.y = player1.y + RECT_HEIGHT
    elif 380 > player1.y > 370:
        player1.y = player1.y - RECT_HEIGHT

    # player 2
    if 0 < player2.y < 10:
        player2.y = player2.y + RECT_HEIGHT
    elif 380 > player2.y > 370:
        player2.y = player2.y - RECT_HEIGHT

    # *ball collisions with left paddle

    if (ball.x + ball.width > player1.x and ball.x < player1.x + player2.width) and (
        player1.y < ball.y < player1.y + RECT_HEIGHT
    ):
        ball_speed_x = -(ball_speed_x + 1)  # increase velocity and reverse direction
        bounce_sound.set_volume(random.uniform(0.5, 1.3))
        bounce_sound.play()

    # *ball collisions with right paddle

    if (ball.x + ball.width > player2.x and ball.x < player2.x + player2.width) and (
        player2.y < ball.y < player2.y + RECT_HEIGHT
    ):
        ball_speed_x = -(ball_speed_x + 1)  # increase velocity and reverse direction
        bounce_sound.set_volume(random.uniform(0.7, 1.0))
        bounce_sound.play()

    # *ball collisions with bottom and top walls

    if ball.y < 0 or ball.y + ball.height > SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y
        bounce_sound.set_volume(random.uniform(0.7, 1.0))
        bounce_sound.play()

    # *ball collisions with side walls

    if ball.x < 0:
        score_player2 += 1  # scoring when ball collides with wall
        reset_position()  # when it scores reset ball and paddles position

    elif ball.x + ball.width > SCREEN_WIDTH:
        score_player1 += 1  # scoring when ball collides with wall
        reset_position()  # when it scores reset ball and paddles position

    # *in case someone get to 10 points game over

    if (score_player1 or score_player2) == 10:
        score_sound.play()
        game_over = True
        if score_player1 == 10:
            winner = "Winner: Player 1"
        else:
            winner = "Winner: Player 2"
        play_again = menu_interface(winner)
        if play_again:
            reset_position()
            game_over = False
            score_player1 = 0
            score_player2 = 0
            pass
        else:
            sys.exit()

    render()  # it will render everything
    clock.tick(60)  # it will render at 60 fps
