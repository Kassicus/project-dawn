import pygame
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Dawn of the Abyss"

class ColorLibrary():
    def __init__(self):
        self.BLACK = pygame.Color(0, 0, 0, 255)
        self.WHITE = pygame.Color(255, 255, 255, 255)
        self.BLUE = pygame.Color(0, 0, 255, 255)

        self.PLAYER1 = pygame.Color(99, 155, 255, 255)
        self.PLAYER2 = pygame.Color(91, 110, 255, 255)
        self.PLAYER3 = pygame.Color(146, 172, 255, 255)

    def getRandomColor(self, alpha):
        color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), alpha)
        return color

    def getRandomChoice(self, colors):
        choice = random.randint(0, len(colors) - 1)
        return colors[choice]

color = ColorLibrary()

deltaTime = 0
