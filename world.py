import pygame
import random

layout = [
    13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    13, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 9, 13,
    13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13
]

sprites = {
    "floor" : pygame.image.load("assets/tiles/ground/brick_test.png"),
    "bottom_flat" : pygame.image.load("assets/tiles/walls/bottom_flat.png"),
    "top_flat" : pygame.image.load("assets/tiles/walls/top_flat.png"),
    "left_flat" : pygame.image.load("assets/tiles/walls/left_flat.png"),
    "right_flat" : pygame.image.load("assets/tiles/walls/right_flat.png"),
    "top_left" : pygame.image.load("assets/tiles/walls/top_left.png"),
    "top_right" : pygame.image.load("assets/tiles/walls/top_right.png"),
    "bottom_left" : pygame.image.load("assets/tiles/walls/bottom_left.png"),
    "bottom_right" : pygame.image.load("assets/tiles/walls/bottom_right.png"),
    "top_left_invert" : pygame.image.load("assets/tiles/walls/top_left_invert.png"),
    "top_right_invert" : pygame.image.load("assets/tiles/walls/top_right_invert.png"),
    "bottom_left_invert" : pygame.image.load("assets/tiles/walls/bottom_left_invert.png"),
    "bottom_right_invert" : pygame.image.load("assets/tiles/walls/bottom_right_invert.png"),
    "out_of_bounds" : pygame.image.load("assets/tiles/walls/out_of_bounds.png")
}

tiles = [
    sprites["floor"], # 0
    sprites["bottom_flat"], # 1
    sprites["top_flat"], # 2
    sprites["left_flat"], # 3
    sprites["right_flat"], # 4
    sprites["top_left"], # 5
    sprites["top_right"], # 6
    sprites["bottom_left"], # 7
    sprites["bottom_right"], # 8
    sprites["top_left_invert"], # 9
    sprites["top_right_invert"], # 10
    sprites["bottom_left_invert"], # 11
    sprites["bottom_right_invert"], # 12
    sprites["out_of_bounds"], # 13
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

        self.image = tiles[layout[self.chunk_id]]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.update(self.x, self.y, self.width, self.height)

class Room():
    def __init__(self):
        self.chunks = pygame.sprite.Group()

        self.width = 1000
        self.height = 800

        self.display_surface = pygame.display.get_surface()

        self.createChunks()

    def createChunks(self):
        chunk_id = 0

        for y in range(int(self.height / 50)):
            for x in range(int(self.width / 50)):
                c = Chunk(int(x * 50), int(y * 50), chunk_id)
                self.chunks.add(c)
                chunk_id += 1

    def draw(self):
        self.chunks.draw(self.display_surface)

    def update(self):
        self.chunks.update()

    def containsPlayer(self, player):
        collide = pygame.sprite.spritecollide(player, self.chunks, True)

        for chunk in collide:
            return chunk.chunk_id

class Door():
    def __init__(self):
        pass

