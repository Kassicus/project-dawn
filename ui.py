# Standard library imports
import pygame

import lib

class GenericUIComponent(pygame.sprite.Sprite):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        bgColor: pygame.Color,
        centered: bool,
    ) -> None:

        super().__init__()

        self.pos = pygame.math.Vector2(x, y)

        self.image = pygame.Surface([width, height])
        self.image.fill(bgColor)
        self.rect = self.image.get_rect()

        if centered:
            self.rect.center = self.pos
        else:
            self.rect.topleft = self.pos

# Generic status bar class, updates in real time, requires feed from updated value
class StatusBar():
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        bgColor: tuple,
        fgColor: tuple,
        value: int,
        maxValue: int
        ):
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
        self.displaySurface = lib.levelref.displaySurface # Get the master surface

        # Value variables
        self.value = value # The inital value we start with, updated with the current value after the first update loop
        self.maxValue = maxValue # The maximum value we can have
        self.currentValue = int(self.width / self.maxValue) * self.value # Map the current value to a scale between the max and min, change the status bar to reflect (is dynamic)

    def draw(self):
        """Draws the background and foreground of the bar"""

        pygame.draw.rect(self.displaySurface, self.bgColor, (self.pos.x - lib.globalOffset.x, self.pos.y - lib.globalOffset.y, self.width, self.height), 0) # Draw the background
        pygame.draw.rect(self.displaySurface, self.fgColor, (self.pos.x + 2 - lib.globalOffset.x, self.pos.y + 2 - lib.globalOffset.y, self.currentValue - 4, self.height - 4)) # Draw the dynamic foreground

    def update(self, value: int):
        """Updates the bar
        
        Keyword arguments:
        value (int) : The current value for the bar
        """
        
        self.value = value # Update the value with the new current value
        self.currentValue = int(self.width / self.maxValue) * self.value # Map the current value to the width of the bar based on the new value

class Slider():
    def __init__(
        self,
        x: int,
        y: int,
    ) -> None:

        self.pos = pygame.math.Vector2(x, y)
        self.slider = GenericUIComponent(x, y, 150, 10, lib.color.BLACK, False)
        self.piper = GenericUIComponent(x + 100, y + 5, 20, 20, lib.color.WHITE, True)
