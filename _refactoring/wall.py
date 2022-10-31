import pygame

import lib

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)
        self.image = pygame.Surface([width, height])
        self.image.fill(lib.color.BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
