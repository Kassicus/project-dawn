# Standard library imports
import pygame
import projectile

class DebugInterface():
    def __init__(self):
        self.font = pygame.font.SysFont("Courier", 16)

        self.fpsText = None
        self.mouseText = None
        self.playerText = None
        self.projectileText = None
        self.particleText = None

        self.displaySurface = pygame.display.get_surface()

        self.active = False

    def getFps(self, clock):
        fpsString = "FPS:     " + str(int(clock.get_fps()))
        fpsText = self.font.render(fpsString, 1, (255, 255, 255))
        return fpsText

    def getMouse(self):
        mouseString = "Mouse:  " + str(pygame.mouse.get_pos())
        mouseText = self.font.render(mouseString, 1, (255, 255, 255))
        return mouseText

    def getPlayer(self, player):
        playerString = "Player: (" + str(player.rect.x) + ", " + str(player.rect.y) + ")"
        playerText = self.font.render(playerString, 1, (255, 255, 255))
        return playerText

    def getProjectileCount(self):
        projectileString = "Proj:    " + str(int(len(projectile._projectiles)))
        projectileText = self.font.render(projectileString, 1, (255, 255, 255))
        return projectileText

    def getParticleCount(self):
        particles = 0
        for p in projectile._projectiles:
            count = len(p.particleSystem.particles)
            particles += count
        particleString = "Part:    " + str(particles)
        particleText = self.font.render(particleString, 1, (255, 255, 255))
        return particleText

    def draw(self):
        pygame.draw.rect(self.displaySurface, (0, 0, 0), (780, 0, 220, 110), 0)
        self.displaySurface.blit(self.fpsText, (800, 10))
        self.displaySurface.blit(self.mouseText, (800, 30))
        self.displaySurface.blit(self.playerText, (800, 50))
        self.displaySurface.blit(self.projectileText, (800, 70))
        self.displaySurface.blit(self.particleText, (800, 90))

    def update(self, clock, player):
        self.fpsText = self.getFps(clock)
        self.mouseText = self.getMouse()
        self.playerText = self.getPlayer(player)
        self.projectileText = self.getProjectileCount()
        self.particleText = self.getParticleCount()