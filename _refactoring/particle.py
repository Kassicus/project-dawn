import pygame
import random

import lib

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, minLife, maxLife):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)
        self.velo = pygame.math.Vector2()
        self.lifeTime = random.randint(minLife, maxLife)
        self.color = color
        self.image = pygame.Surface([width, height])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def update(self):
        self.pos += self.velo * lib.deltaTime
        self.rect.center = self.pos

        print(self.pos, self.velo)

        self.lifeTime -= 1
        if self.lifeTime <= 0:
            self.kill()

class ParticleSystem():
    def __init__(self, drawContainer):
        self.drawContainer = drawContainer
        self.particleContainer = pygame.sprite.Group()
        self.particleColor = lib.color.BLACK
        self.maxParticles = 100

    def createParticles(self, x, y, count, minParticleDim, maxParticleDim, particleOffset, minLife, maxLife, minVeloX, maxVeloX, minVeloY, maxVeloY, minAlpha, maxAlpha):
        for p in range(count):
            particleDim = random.randint(minParticleDim, maxParticleDim)
            spawnPos = pygame.math.Vector2(random.randint(x - particleOffset, x + particleOffset), random.randint(y - particleOffset, y + particleOffset))
            p = Particle(spawnPos.x, spawnPos.y, particleDim, particleDim, self.particleColor, minLife, maxLife)

            p.velo.x = random.uniform(minVeloX, maxVeloX)
            p.velo.y = random.uniform(minVeloY, maxVeloY)

            p.image.set_alpha(random.randint(minAlpha, maxAlpha))

            self.drawContainer.add(p)
            self.particleContainer.add(p)

class PlayerParticleSystem(ParticleSystem):
    def __init__(self, drawContainer):
        super().__init__(drawContainer)
        self.particleColor = lib.color.getRandomChoice([lib.color.PLAYER1, lib.color.PLAYER2, lib.color.PLAYER3])
        self.createParticles(500, 400, self.maxParticles, 3, 5, 15, 10, 25, -40, 40, -40, 40, 25, 255)

    def update(self):
        self.particleContainer.update()

        newCount = self.maxParticles - len(self.particleContainer)
        self.createParticles(500, 400, newCount, 3, 5, 15, 10, 25, -40, 40, -40, 40, 25, 255)