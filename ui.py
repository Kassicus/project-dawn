# Standard library imports
import pygame

# Generic status bar class, updates in real time, requires feed from updated value
class StatusBar():
    def __init__(self, x, y, width, height, bg_color, fg_color, value, max_value):
        """
        bg_color: background color for bar
        fg_color: foreground color for bar
        value: initial value for bar (also feed this to the update function)
        max_value: maximum possible value (can be changed)
        """
        
        # Position Variables
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Graphics variables
        self.bg_color = bg_color
        self.fg_color = fg_color

        # Value
        self.value = value
        self.max_value = max_value

        self.current_value = int(self.width / self.max_value) * self.value # Map the current value to a scale between the max and min, change the status bar to reflect (is dynamic)

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.width, self.height), 0) # Background
        pygame.draw.rect(surface, self.fg_color, (self.x + 2, self.y + 2, self.current_value - 4, self.height - 4)) # Dynamic foreground

    def update(self, value):
        self.value = value # Update the value with a live feed
        self.current_value = int(self.width / self.max_value) * self.value # Refresh status bar width to match live value