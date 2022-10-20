# Standard library imports
import pygame
import math

import reference

_projectiles = pygame.sprite.Group() # Python handles sprites in groups, this is for organization purposes

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, tx, ty, width, height, particle_system, speed):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2()

        self.width = width
        self.height = height

        self.target = pygame.math.Vector2(tx, ty)

        self.particle_system = particle_system

        self.speed = speed

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(reference.WHITE)

        self.display_surface = pygame.display.get_surface()

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
        self.particle_system.draw(self.display_surface)
        self.particle_system.update()

        self.pos += self.velocity * reference.dt

        self.rect = self.pos

        self.particle_system.pos = self.pos

        self.check_overrun()

    def check_overrun(self):
        if self.pos.x < -500 or self.pos.x > 1500:
            self.kill()
        
        if self.pos.y < -500 or self.pos.y > 1300:
            self.kill()
