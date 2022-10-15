# Standard library imports
import pygame
import math

_projectiles = pygame.sprite.Group() # Python handles sprites in groups, this is for organization purposes

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, tx, ty, particle_system, speed):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        self.width = 1
        self.height = 1

        self.tx = tx
        self.ty = ty

        self.particle_system = particle_system

        self.speed = speed

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0, 0, 0))

        self.rect = (self.x, self.y)

        self.x_vel, self.y_vel = self.get_vectors()

    def get_vectors(self):
        distance = [self.tx - self.x, self.ty - self.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normal, distance[1] / normal]
        vectors = [direction[0] * self.speed, direction[1] * self.speed]

        return vectors

    def update(self, surface):
        self.particle_system.draw(surface)
        self.particle_system.update()

        self.x += self.x_vel
        self.y += self.y_vel

        self.rect = (self.x, self.y)

        self.particle_system.x = self.x
        self.particle_system.y = self.y

        self.check_overrun()

    def check_overrun(self):
        if self.x < -500 or self.x > 1500:
            self.kill()
        
        if self.y < -500 or self.y > 1300:
            self.kill()
