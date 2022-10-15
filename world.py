import pygame
import random

tiles = [
    pygame.image.load("assets/tiles/ground/brick_test.png")
]

class Chunk(pygame.sprite.Sprite):
    def __init__(self, x, y, chunk_id, wall=False):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        self.width = 50
        self.height = 50

        self.chunk_id = chunk_id
        self.wall = wall

        self.image = tiles[0]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.update(self.x, self.y, self.width, self.height)

class Room():
    def __init__(self):
        self.chunks = pygame.sprite.Group()

        self.width = 1000
        self.height = 800

        self.createChunks()

    def createChunks(self):
        chunk_id = 0

        for x in range(int(self.width / 50)):
            for y in range(int(self.height / 50)):
                c = Chunk(int(x * 50), int(y * 50), chunk_id)
                self.chunks.add(c)
                chunk_id += 1

    def draw(self, surface):
        self.chunks.draw(surface)

    def update(self):
        self.chunks.update()

    def containsPlayer(self, player):
        collide = pygame.sprite.spritecollide(player, self.chunks, True)

        for chunk in collide:
            return chunk.chunk_id

class Door():
    def __init__(self):
        pass

