# Standard library imports
import pygame

# Generic status bar class, updates in real time, requires feed from updated value
class StatusBar():
    def __init__(self, x, y, width, height, bgColor, fgColor, value, maxValue):
        """Draw a dynamic status bar

        Keyword arguments:
        x (int) : The horizontal location of the status bar
        y (int) : The vertical location of the status bar
        width (int) : The total width of the status bar
        height (int) : The total height of the status bar
        bgColor (tuple) : The background color for the status bar
        fgColor (tuple) : The foreground color for the status bar
        value (int) : The initial value for bar (also feed this to the update function)
        maxValue (int) : The maximum possible value (can be changed)
        """
        
        # Position Variables
        self.pos = pygame.math.Vector2(x, y) # Vector to contain the x and y
        self.width = width # Width of the bar
        self.height = height # Height of the bar

        # Graphics variables
        self.bgColor = bgColor # The background color
        self.fgColor = fgColor # The foreground color
        self.displaySurface = pygame.display.get_surface() # Get the master surface

        # Value variables
        self.value = value # The inital value we start with, updated with the current value after the first update loop
        self.maxValue = maxValue # The maximum value we can have
        self.currentValue = int(self.width / self.maxValue) * self.value # Map the current value to a scale between the max and min, change the status bar to reflect (is dynamic)

    def draw(self):
        """Draws the background and foreground of the bar"""

        pygame.draw.rect(self.displaySurface, self.bgColor, (self.pos.x, self.pos.y, self.width, self.height), 0) # Draw the background
        pygame.draw.rect(self.displaySurface, self.fgColor, (self.pos.x + 2, self.pos.y + 2, self.currentValue - 4, self.height - 4)) # Draw the dynamic foreground

    def update(self, value):
        """Updates the bar
        
        Keyword arguments:
        value (int) : The current value for the bar
        """
        
        self.value = value # Update the value with the new current value
        self.currentValue = int(self.width / self.maxValue) * self.value # Map the current value to the width of the bar based on the new value