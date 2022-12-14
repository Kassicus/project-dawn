import pygame
import math
import random

import lib
import ui
import projectile
import particle
import spells

class BaseStaticEnemy(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.health = 100

        self.healthBar = ui.StatusBar(int(self.pos.x - 50), int(self.pos.y - 30), 100, 7, lib.color.WHITE, lib.color.RED, self.health, self.health)

        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.STATICENEMY)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.spell.update()

        self.healthBar.draw()
        self.healthBar.update(self.health)

        if self.health <= 0:
            self.kill()

class TurretEnemy(BaseStaticEnemy):
    def __init__(self, x: int, y: int, size: int) -> None:
        super().__init__(x, y, size)
        self.tag = "turret"
        self.spell = spells.MagicMissle("hostile")
        self.spell.maxCooldown = 120
        self.spell.cooldown = random.randint(0, self.spell.maxCooldown)

    def shootAtPlayer(self, player: pygame.sprite.Sprite) -> None:
        if self.spell.canBeCast:
            self.spell.castSpell(self.pos.x, self.pos.y, player.pos.x, player.pos.y)

class BaseEnemy(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, size: int) -> None:
        super().__init__()

        self.pos = pygame.math.Vector2(x, y)
        self.velo = pygame.math.Vector2()
        self.speed = 100
        self.health = 20

        self.healthBar = ui.StatusBar(int(self.pos.x - 20), int(self.pos.y - 30), 40, 7, lib.color.WHITE, lib.color.RED, self.health, self.health)
        
        self.image = pygame.Surface([size, size])
        self.image.fill(lib.color.RED)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self) -> None:
        self.pos += self.velo * lib.deltaTime
        self.rect.center = self.pos

        self.healthBar.draw()
        self.healthBar.update(self.health)
        self.healthBar.pos.x = int(self.pos.x - 20)
        self.healthBar.pos.y = int(self.pos.y - 30)

        if self.health <= 0:
            self.kill()

class ChaserEnemy(BaseEnemy):
    def __init__(self, x: int, y: int, size: int, speed: float) -> None:
        super().__init__(x, y, size)
        self.tag = "chaser"

        self.speed = speed
        self.health = 20

        self.targetPos = pygame.math.Vector2()
    
    def chasePlayer(self, player: pygame.sprite.Sprite) -> None:
        self.velo.x = self.getVectors(player.pos)[0]
        self.velo.y = self.getVectors(player.pos)[1]

    def getVectors(self, target: pygame.math.Vector2) -> list:
        self.targetPos = target
        
        distance = [target.x - self.pos.x, target.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normal, distance[1] / normal]
        vectors = [direction[0] * self.speed, direction[1] * self.speed]

        return vectors

class RangeChaserEnemy(BaseEnemy):
    def __init__(self, x: int, y: int, size: int, speed: float) -> None:
        super().__init__(x, y, size)
        self.tag = "rangechaser"

        self.speed = speed
        self.health = 40
        self.range = 150

        self.targetPos = pygame.math.Vector2()

    def chasePlayer(self, player: pygame.sprite.Sprite) -> None:
        if self.targetPos.x < self.pos.x + self.range:
            self.velo.x = self.getVectors(player.pos)[0]
            self.velo.y = self.getVectors(player.pos)[1]
        elif self.targetPos.x > self.pos.x - self.range:
            self.velo.x = self.getVectors(player.pos)[0]
            self.velo.y = self.getVectors(player.pos)[1]
        elif self.targetPos.y < self.pos.y + self.range:
            self.velo.x = self.getVectors(player.pos)[0]
            self.velo.y = self.getVectors(player.pos)[1]
        elif self.targetPos.y > self.pos.y - self.range:
            self.velo.x = self.getVectors(player.pos)[0]
            self.velo.y = self.getVectors(player.pos)[1]
        else:
            self.velo.x = 0
            self.velo.y = 0


    def getVectors(self, target: pygame.math.Vector2) -> list:
        self.targetPos = target

        distance = [target.x - self.pos.x, target.y - self.pos.y]
        normal = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normal, distance[1] / normal]
        vectors = [direction[0] * self.speed, direction[1] * self.speed]

        return vectors