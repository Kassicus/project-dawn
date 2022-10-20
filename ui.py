# Standard library imports
import pygame

# Generic status bar class, updates in real time, requires feed from updated value
class StatusBar():
    def __init__(self, x, y, width, height, bgColor, fgColor, value, maxValue):
        """
        bgColor: background color for bar
        fgColor: foreground color for bar
        value: initial value for bar (also feed this to the update function)
        maxValue: maximum possible value (can be changed)
        """
        
        # Position Variables
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Graphics variables
        self.bgColor = bgColor
        self.fgColor = fgColor

        self.displaySurface = pygame.display.get_surface()

        # Value
        self.value = value
        self.maxValue = maxValue

        self.currentValue = int(self.width / self.maxValue) * self.value # Map the current value to a scale between the max and min, change the status bar to reflect (is dynamic)

    def draw(self):
        pygame.draw.rect(self.displaySurface, self.bgColor, (self.x, self.y, self.width, self.height), 0) # Background
        pygame.draw.rect(self.displaySurface, self.fgColor, (self.x + 2, self.y + 2, self.currentValue - 4, self.height - 4)) # Dynamic foreground

    def update(self, value):
        self.value = value # Update the value with a live feed
        self.currentValue = int(self.width / self.maxValue) * self.value # Refresh status bar width to match live value