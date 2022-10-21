# Standard imports
import pygame

# Constants
SCREEN_WIDTH = 1000 # How many pixels wide the game window is
SCREEN_HEIGHT = 800 # How many pixels tall the game window is
SCREEN_TITLE = "Dawn of the Abyss" # The text that appears at the top of the game window


# Colors - also constants...
BLACK = pygame.Color(0, 0, 0, 255) # The color black
WHITE = pygame.Color(255, 255, 255, 255) # The color white

COLOR_FIRE = pygame.Color(247, 90, 27, 255) # A pretty mid-ground orange color

# Variables
dt = 0 # Delta time, time between frames

activeRoom = None # The current room that the player is in