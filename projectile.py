import pygame
import math

import lib

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, targetX: int, targetY: int, size: int, speed: float, particleSystem: object, drawContainer: pygame.sprite.Group, damage: int) -> None:
        """Create a projectile
        
        Arguments:
        x: int - The initial horizontal posision of the projectile
        y: int - The initial vertical position of the projectile
        targetX: int - The intended horizontal position of the projectile
        targetY: int - The intended vertical position of the projectile
        size: int - The amount of pixels the projectile is wide and tall
        speed: float - The speed of the projectile
        particleSystem: object - The particle system of the projectile
        drawContainer: pygame.sprite.Group - The levels main camera object
        """
        
        pygame.sprite.Sprite.__init__(self)

        self.pos = pygame.math.Vector2(x, y)
        self.velo = pygame.math.Vector2()
        self.targetPos = pygame.math.Vector2(targetX, targetY)
        self.speed = speed
        self.damage = damage
        self.lifetime = 1000

        self.particleSystem = particleSystem(self.pos.x, self.pos.y, drawContainer)

        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.velo.x = self.getVectors()[0]
        self.velo.y = self.getVectors()[1]

    def getVectors(self) -> list:
        """Takes the spawn position and target position and does fancy math to get the bullet vectors
        
        Returns:
        vectors: list - The calculated vectors [0] = x, [1] = y
        """

        distance = [self.targetPos.x - self.pos.x, self.targetPos.y - self.pos.y] # Difference in the x values and difference in the y values
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2) # This is just pythagorean theorum. A^2 + B^2 = C^2, but for us its C = sqrt(A^2 + B^2)
        direction = [distance[0] / normal, distance[1] / normal] # Divide the difference by the normal to get a rise over run step
        vectors = [direction[0] * self.speed, direction[1] * self.speed] # Multiply that step by speed to get the actual change in rise over run for the projectile

        return vectors # Return those projectiles

    def update(self) -> None:
        self.pos += self.velo * lib.deltaTime
        self.rect.center = self.pos

        if self.particleSystem is not None:
            self.particleSystem.update(self.pos.x, self.pos.y)

        self.lifetime -= 1

        if self.lifetime <= 0:
            self.kill()