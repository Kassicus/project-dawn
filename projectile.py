# Standard library imports
import pygame
import math

import reference

_projectiles = pygame.sprite.Group() # Python handles sprites in groups, this is for organization purposes

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, tx, ty, width, height, particleSystem, speed):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2()

        self.width = width
        self.height = height

        self.target = pygame.math.Vector2(tx, ty)

        self.particleSystem = particleSystem

        self.speed = speed

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(reference.WHITE)

        self.displaySurface = pygame.display.get_surface()

        self.rect = self.pos

        self.velocity.x = self.get_vectors()[0]
        self.velocity.y = self.get_vectors()[1]

    def get_vectors(self):
        distance = [self.target.x - self.pos.x, self.target.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normal, distance[1] / normal]
        vectors = [direction[0] * self.speed, direction[1] * self.speed]

        return vectors

    def update(self):
        self.particleSystem.draw(self.displaySurface)
        self.particleSystem.update()

        self.pos += self.velocity * reference.dt

        self.rect = self.pos

        self.particleSystem.pos = self.pos

        self.checkOverrun()

    def checkOverrun(self):
        if self.pos.x < -500 or self.pos.x > 1500:
            self.kill()
        
        if self.pos.y < -500 or self.pos.y > 1300:
            self.kill()
