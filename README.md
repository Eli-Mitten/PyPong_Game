# PyPong Game

PyPong is a classic Pong game implemented in Python using the `turtle` graphics library. Two players control paddles on the left and right sides of the screen, trying to bounce a ball back and forth. The first player to miss the ball loses the point.

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pypong.git
    cd pypong
    ```

2. Install required libraries (if not already installed):
    ```bash
    pip install turtle
    ```

### Running the Game

Run the `main.py` script to start the game:
```bash
python main.py
```
## Game Controls

### Player 1 (Left Paddle):
- Move Up: `W`
- Move Down: `S`

### Player 2 (Right Paddle):
- Move Up: `Up Arrow`
- Move Down: `Down Arrow`

## Game Mechanics
- The ball bounces off the top and bottom walls.
- The ball bounces off the paddles when they are hit.
- If the ball goes past a paddle, the opposing player scores a point.
- The game continues indefinitely, and the score is displayed at the top of the screen.

## Code Overview

### `main.py`
This file initializes the game screen, creates the paddle, ball, and scoreboard objects, and contains the main game loop.

### `ball.py`
This file defines the `Ball` class, which handles the ball's movement, bouncing, and resetting the position when a point is scored.

### `scoreboard.py`
This file defines the `Scoreboard` class, which handles the display and updating of the players' scores.

### `paddle.py`
This file defines the `Paddle` class, which handles the creation and movement of the paddles.
