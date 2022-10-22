# Standard imports
import pygame
import random

# Constants
SCREEN_WIDTH = 1000 # How many pixels wide the game window is
SCREEN_HEIGHT = 800 # How many pixels tall the game window is
SCREEN_TITLE = "Dawn of the Abyss" # The text that appears at the top of the game window

class ColorLibrary():
    def __init__(self):
        """Contains all of the colors, and function to create random colors"""

        self.BLACK = pygame.Color(0, 0, 0, 255) # The color black
        self.WHITE = pygame.Color(255, 255, 255, 255) # The color white

        self.FIRE_PARTICLE = pygame.Color(247, 90, 27, 255) # The fire particle, a nice mid orange
        self.PLAYER_PARTICLE_1 = pygame.Color(99, 155, 255, 255) # The players particle color (light blue-ish)
        self.PLAYER_PARTICLE_2 = pygame.Color(91, 110, 255, 255) # The players particle color (light blue-ish)
        self.PLAYER_PARTICLE_3 = pygame.Color(146, 172, 255, 255) # The players particle color (light blue-ish)

    def getRandomColor(self, alpha):
        """Get a random color
        
        Keyword arguments:
        alpha (int) : 0-255, supplies the alpha value for the random color
        """
        
        color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), alpha) # Create the random color
        return color # Returnt the random color

    def getRandomChoice(self, colors):
        choice = random.randint(0, len(colors) - 1)
        return colors[choice]

color = ColorLibrary() # Create the color library

# Variables
dt = 0 # Delta time, time between frames

activeRoom = None # The current room that the player is in