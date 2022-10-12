import pygame
import random

class Chunk(pygame.sprite.Sprite):
    def __init__(self, x, y, wall=False):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.width = 50
        self.height = 50

        self.wall = wall

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

        self.rect = (self.x, self.y)

    def update(self):
        self.rect = (self.x, self.y)

class Room():
    def __init__(self):
        self.chunks = pygame.sprite.Group()

        self.width = 1000
        self.height = 800

        self.createChunks()

    def createChunks(self):
        for x in range(int(self.width / 50)):
            for y in range(int(self.height / 50)):
                c = Chunk(int(x * 50), int(y * 50))
                self.chunks.add(c)

    def draw(self, surface):
        self.chunks.draw(surface)

    def update(self):
        self.chunks.update()

class Door():
    def __init__(self):
        pass

