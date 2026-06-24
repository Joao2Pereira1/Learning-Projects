# Ping Pong Game Documentation

## Overview

This is a simple implementation of the classic game Ping Pong using the Pygame library. The game features two paddles that can be controlled by the user, a ball that bounces around the screen, and a scoring system.

## Note

This is game for two players in the same keyboard one with A,W,S,D keys and other with J,I,K,L keys.

## Gameplay

The game starts with the ball in the center of the screen and the paddles at the top and bottom of the screen.
The user can control the paddles using the W and S keys for the left paddle and the U and J keys for the right paddle.
The ball will bounce off the walls and the paddles, and will score points when it hits the opponent's side of the screen.
The game will end when one player reaches a score of 10.

## Functions

draw(): This function is responsible for rendering the game screen, including the paddles, ball, and score.
reset_position(): This function resets the positions of the ball and paddles to their initial values.
main loop: This is the main game loop that handles user input, updates the game state, and renders the game screen.
Variables
SCREEN_WIDTH and SCREEN_HEIGHT: These variables define the dimensions of the game screen.
SPEED_RECT: This variable defines the speed at which the paddles move.
SPEED_BALL: This variable defines the speed at which the ball moves.
score_player_one and score_player_two: These variables keep track of the score for each player.
game_over: This variable indicates whether the game is over or not.
winner: This variable stores the winner of the game.

## Pygame Functions

py.init(): Initializes the Pygame library.
py.display.set_mode(): Sets the display mode for the game screen.
py.display.set_caption(): Sets the caption for the game window.
py.time.Clock(): Creates a clock object to control the frame rate.
py.event.get(): Gets a list of events from the event queue.
py.draw.rect(): Draws a rectangle on the screen.
py.draw.ellipse(): Draws an ellipse on the screen.
py.draw.aaline(): Draws an anti-aliased line on the screen.
py.font.SysFont(): Creates a font object.
py.display.flip(): Updates the entire display window.

## Sound Effects and Background Music

### Sound Effects:

Ball bouncing off the walls or paddles: bounce_sound.wav
Scoring a point: score_sound.wav
Game over: game_over_sound.wav

### Background Music:

background_music.mp3 (loops continuously)
