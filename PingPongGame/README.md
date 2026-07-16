# 🏓 Ping Pong Game Documentation

## Overview & Gameplay

This is a simple implementation of the classic game Ping Pong using the Pygame library. The game features two paddles that can be controlled by the users on the same keyboard, a ball that bounces around the screen, and an automatic scoring system.

*   **Setup:** The game starts with the ball in the center of the screen and the paddles positioned at the left and right sides of the screen.
*   **Mechanics:** The ball will bounce off the top and bottom walls as well as the paddles. It will score a point when it hits the opponent's side of the screen (passing their paddle).
*   **Match Limit:** The game will end automatically when one player reaches a score of 10.

### Controls

This is a local game designed for two players sharing the same keyboard:
*   **Left Paddle (Player 1):** `W` key to move up, `S` key to move down.
*   **Right Paddle (Player 2):** `I` key to move up, `K` key to move down.

## Functions & Variables

### Core Functions & Loops
*   `draw()`: This function is responsible for rendering the game screen, including drawing the paddles, the ball, and the current scores.
*   `reset_position()`: This function resets the positions of the ball and paddles back to their initial values after a point is scored.
*   **Main Loop:** This is the central game loop that handles user input events, updates the positional and collision states, and continuously triggers the screen rendering.

### Essential Variables
*   `SCREEN_WIDTH` and `SCREEN_HEIGHT`: These variables define the dimensions and display resolution of the game screen.
*   `SPEED_RECT`: This variable defines the speed at which the player paddles move.
*   `SPEED_BALL`: This variable defines the speed at which the ball moves across the court.
*   `score_player_one` and `score_player_two`: These variables keep track of the live score for each player.
*   `game_over`: This boolean variable indicates whether the match has ended or is still ongoing.
*   `winner`: This variable stores the identity of the winner once the score limit is reached.

## Pygame Methods Used

The game utilizes the following built-in Pygame functions to manage the application lifecycle, capture inputs, and handle graphics rendering:

| Method | Description / Purpose |
| :--- | :--- |
| `py.init()` | Initializes all imported Pygame modules. |
| `py.display.set_mode()` | Initializes a window or screen for display. |
| `py.display.set_caption()` | Sets the text caption at the top header of the game window. |
| `py.time.Clock()` | Creates a clock object to help track time and regulate the frame rate (FPS). |
| `py.event.get()` | Retrieves and clears all pending events from the internal event queue (e.g., key presses or closing the window). |
| `py.draw.rect()` | Draws the rectangular paddles on the screen. |
| `py.draw.ellipse()` | Draws the spherical game ball on the screen. |
| `py.draw.aaline()` | Draws an anti-aliased straight line to split the center of the court. |
| `py.font.SysFont()` | Creates a font object from system resources to render text and scores. |
| `py.display.flip()` | Updates the entire display surface to the window screen. |

## Sound Effects and Background Music

### Sound Effects
*   **Ball bouncing off the walls or paddles:** `bounce_sound.wav`
*   **Scoring a point:** `score_sound.wav`
*   **Game over:** `game_over_sound.wav`

### Background Music
*   `background_music.mp3` (loops continuously throughout the match)

---

# License

This project is distributed under the MIT License.
