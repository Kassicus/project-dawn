import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(int(lib.SCREEN_WIDTH / 2), int(lib.SCREEN_HEIGHT / 2))
        self.velo = pygame.math.Vector2()
        self.speed = 200

        self.particleSystem = None

        self.image = pygame.Surface([40, 40])
        self.image.fill(lib.color.WHITE)
        self.image.set_colorkey(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.pos += self.velo * lib.deltaTime
        self.rect.center = self.pos

        self.move()

        if self.particleSystem is not None:
            self.particleSystem.update(self.pos.x, self.pos.y)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velo.x = -self.speed
        elif keys[pygame.K_d]:
            self.velo.x = self.speed
        else:
            self.velo.x = 0

        if keys[pygame.K_w]:
            self.velo.y = -self.speed
        elif keys[pygame.K_s]:
            self.velo.y = self.speed
        else:
            self.velo.y = 0
