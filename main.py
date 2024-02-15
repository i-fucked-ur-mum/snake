"""
This simple animation example shows how to bounce a rectangle
on the screen.

If Python and Arcade are installed, this example can be run
from the command line with:
python -m arcade.examples.bouncing_rectangle
"""

import arcade

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "snake"
SCREEN_UPDATE_RATE = 0.75

# snake info
BLOCK_SIZE = 50
BLOCK_COLOR = arcade.color.LIGHT_GREEN

BACKGROUND_COLOR = arcade.color.GRAY


class Snake:
    """ This class represents our snake """

    def __init__(self, start_body, default_direction):
    	self.body = start_body.copy()
    	self.direction = default_direction

    def update(self):
        # Move the snake
        for i in range(len(self.body) - 1):
        	self.body[i] = self.body[i + 1].copy()
        self.body[len(self.body) - 1][0] += self.direction[0]
        self.body[len(self.body) - 1][1] += self.direction[1]
        # Check if we need to bounce of right edge
        if self.body[len(self.body) - 1][0] < 0 or self.body[len(self.body) - 1][0] > (SCREEN_HEIGHT / BLOCK_SIZE) - 1 or self.body[len(self.body) - 1][1] < 0 or self.body[len(self.body) - 1][1] > (SCREEN_WIDTH / BLOCK_SIZE) - 1:
        	pass #DEATH

    def extention(self):
    	temp = [0, 0]
    	temp[0] = self.body[len(self.body) - 1][0] + self.direction[0]
    	temp[1] = self.body[len(self.body) - 1][1] + self.direction[1]
    	self.body.append(temp)
        
    def food(self):
    	pass

    def death(self):
    	pass

    def draw(self):
        # Draw the rectangle
        for i in range(len(self.body)):
	        arcade.draw_rectangle_filled((self.body[i][0] * BLOCK_SIZE) + (BLOCK_SIZE / 2),
                                     (self.body[i][1] * BLOCK_SIZE) + (BLOCK_SIZE / 2),
                                     BLOCK_SIZE,
                                     BLOCK_SIZE,
                                     BLOCK_COLOR)


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title, update_rate):
        super().__init__(width, height, title, update_rate = update_rate)

        # Create our snake
        self.snake = Snake([[0, 0], [0, 1], [0, 2]], [0, 1])

        # Set background color
        self.background_color = BACKGROUND_COLOR

    def on_update(self, delta_time):
        # Move the snake
        self.snake.update()

    def on_key_press(self, symbol, modifiers):
    	if symbol == arcade.key.D or symbol == arcade.key.RIGHT:
    		self.snake.direction = [1, 0]
    	if symbol == arcade.key.A or symbol == arcade.key.LEFT:
    		self.snake.direction = [-1, 0]
    	if symbol == arcade.key.W or symbol == arcade.key.UP:
    		self.snake.direction = [0, 1]
    	if symbol == arcade.key.S or symbol == arcade.key.DOWN:
    		self.snake.direction = [0, -1]
    	if symbol == arcade.key.P:
    		self.snake.extention()

    def on_draw(self):
        """ Render the screen. """

        # Clear screen
        self.clear()
        # Draw the snake
        self.snake.draw()


def main():
    """ Main function """
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_UPDATE_RATE)
    arcade.run()


if __name__ == "__main__":
    main()