# Standard library imports
import pygame
import pygame.color
import pygame.freetype as freetype

class PlayerInventoryMenu():
    def __init__(self, x, y, width, height, bg_color, fg_color):
        """
        bg_color: background color for menu
        fg_color: foreground color for menu
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

        self.isDrawn = False

    def draw(self, surface):
        # draws a semi transparent box
        s = pygame.Surface((self.width - (self.x * 2), self.height - (self.y * 2)), pygame.SRCALPHA)
        s.fill(self.bg_color)
        surface.blit(s,(self.x,self.y))

    #def update(self, value):
    #    self.value = value # Update the value with a live feed
    #    self.current_value = int(self.width / self.max_value) * self.value # Refresh status bar width to match live value
