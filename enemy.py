import pygame
import math

import lib

class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.velo = pygame.math.Vector2()
        self.speed = 100
        
        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.RED)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.velo * lib.deltaTime
        self.rect.center = self.pos

class ChaserEnemy(BaseEnemy):
    def __init__(self, x: int, y: int, size: int, speed: float) -> None:
        super().__init__(x, y, size)

        self.speed = speed
    
    def chasePlayer(self, player: pygame.sprite.Sprite) -> None:
        self.velo.x = self.getVectors(player.pos)[0]
        self.velo.y = self.getVectors(player.pos)[1]

    def getVectors(self, target: pygame.math.Vector2) -> list:
        distance = [target.x - self.pos.x, target.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normal, distance[1] / normal]
        vectors = [direction[0] * self.speed, direction[1] * self.speed]

        return vectors