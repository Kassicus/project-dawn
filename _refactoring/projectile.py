import pygame
import math

import lib

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, targetX: int, targetY: int, size: int, speed: float) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.targetPos = pygame.math.Vector2(targetX, targetY)
        self.speed = speed

        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def getVectors(self) -> None:
        """Takes the spawn position and target position and does fancy math to move the bullet"""

        distance = [self.target.x - self.pos.x, self.target.y - self.pos.y] # Difference in the x values and difference in the y values
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2) # This is just pythagorean theorum. A^2 + B^2 = C^2, but for us its C = sqrt(A^2 + B^2)
        direction = [distance[0] / normal, distance[1] / normal] # Divide the difference by the normal to get a rise over run step
        vectors = [direction[0] * self.speed, direction[1] * self.speed] # Multiply that step by speed to get the actual change in rise over run for the projectile

        return vectors # Return those projectiles

    def update(self) -> None:
        self.pos += self.velocity * lib.deltaTime
        self.rect.center = self.pos

        if self.overrun():
            self.kill()

    def overrun(self) -> bool:
        if self.pos.x < -500 or self.pos.x > 1500 or self.pos.y < -500 or self.pos.y > 1300:
            return True
        else:
            return False