# Standard imports
import pygame
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Dawn of the Abyss"

class ColorLibrary():
    def __init__(self) -> None:
        """Create and store all colors to be used in game"""

        # Standard colors
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)
        self.BLUE = pygame.Color(0, 0, 255, 255)
        self.RED = pygame.Color(255, 0, 0)
        self.GREEN = pygame.Color(0, 255, 0, 255)

        # Custom colors
        self.PLAYER1 = pygame.Color(99, 155, 255, 255)
        self.PLAYER2 = pygame.Color(91, 110, 255, 255)
        self.PLAYER3 = pygame.Color(146, 172, 255, 255)
        self.BACKGROUND = pygame.Color(9, 8, 16, 255)
        self.STATICENEMY = pygame.Color(245, 66, 111, 255)
        self.FIRETRAIL1 = pygame.Color(252, 169, 3, 255)
        self.FIRETRAIL2 = pygame.Color(237, 133, 5, 255)
        self.FIRETRAIL3 = pygame.Color(252, 188, 10, 255)

    def getRandomColor(self, alpha: int) -> pygame.Color:
        """Create a random color
        
        Arguments:
        alpha: int - How much transparency the color has (0-255)
        
        Returns:
        color: pygame.Color
        """
        
        color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), alpha) # Create the color using random ints
        return color # Retunr the color

    def getRandomChoice(self, colors: list) -> pygame.Color:
        """Return a random color of the choises presented
        
        Arguments:
        colors: list - The pygame.Color objects to be chosen from
        
        Returns:
        color: pygame.Color
        """
        choice = random.randint(0, len(colors) - 1) # Get the index of the random choice
        color = colors[choice] # Get the color at that index
        return color # Return the color

color = ColorLibrary() # Creat the color library

deltaTime = 0 # Delta time is a magical fucking thing
globalOffset = pygame.math.Vector2() # A global offset to be able to use the correct camera features
levelref = None