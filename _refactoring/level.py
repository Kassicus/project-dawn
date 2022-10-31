import pygame

import lib
import camera
import player
import wall
import particle

class Level():
    def __init__(self):
        self.displaySurface = pygame.display.get_surface()
        self.levelBackground = pygame.image.load("_refactoring/assets/background/test_1.png").convert_alpha()
        self.worldCamera = camera.PlayerCenterCamera(self.displaySurface, self.levelBackground)
        self.player = player.Player()

        self.collidables = pygame.sprite.Group()
        self.collisionTollerance = 10

        self.walls = [
        [0, 0, 50, 300],
        [200, 300, 300, 50]
        ]

        self.createWalls(self.walls)
        self.worldCamera.add(self.player)

        self.player.particleSystem = particle.PlayerParticleSystem(self.worldCamera)

    def draw(self):
        self.worldCamera.cameraDraw(self.player)

    def update(self):
        self.worldCamera.update()

        self.checkCollisions()

    def createWalls(self, wallArray):
        for pointArray in range(len(wallArray)):
            w = wall.Wall(wallArray[pointArray][0], wallArray[pointArray][1], wallArray[pointArray][2], wallArray[pointArray][3])
            self.worldCamera.add(w)
            self.collidables.add(w)

    def checkCollisions(self):
        for c in self.collidables:
            if self.player.rect.colliderect(c.rect):
                if abs(self.player.rect.left - c.rect.right) < self.collisionTollerance:
                    self.player.velo.x = 0
                    self.player.pos.x = c.rect.right + self.player.rect.width / 2
                if abs(self.player.rect.right - c.rect.left) < self.collisionTollerance:
                    self.player.velo.x = 0
                    self.player.pos.x = c.rect.left - self.player.rect.width / 2

                if abs(self.player.rect.top - c.rect.bottom) < self.collisionTollerance:
                    self.player.velo.y = 0
                    self.player.pos.y = c.rect.bottom + self.player.rect.height / 2
                if abs(self.player.rect.bottom - c.rect.top) < self.collisionTollerance:
                    self.player.velo.y = 0
                    self.player.pos.y = c.rect.top - self.player.rect.height / 2
