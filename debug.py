# Standard imports
import pygame

# Custom imports
import lib

class DebugInterface():
    def __init__(self, level: object) -> None:
        """Collects and draws out a ton of useful information"""

        self.level = level
        self.player = self.level.player

        self.font = pygame.font.SysFont("Courier", 16)
        self.fpsText = None
        self.mouseText = None
        self.playerText = None
        self.projectileText = None
        self.enemyText = None

        self.displaySurface = pygame.display.get_surface()
        self.active = False

    def getFps(self, clock: pygame.time.Clock) -> pygame.Surface:
        fpsString = "FPS: " + str(int(clock.get_fps()))
        fpsText = self.font.render(fpsString, True, lib.color.WHITE)
        return fpsText

    def getMousePos(self) -> pygame.Surface:
        mouseString = "Mouse: " + str(pygame.mouse.get_pos())
        mouseText = self.font.render(mouseString, True, lib.color.WHITE)
        return mouseText

    def getPlayerPos(self) -> pygame.Surface:
        playerString = "Player: (" + str(self.player.rect.x) + ", " + str(self.player.rect.y) + ")"
        playerText = self.font.render(playerString, True, lib.color.WHITE)
        return playerText

    def getProjectileCount(self) -> pygame.Surface:
        projectileString = "Projectiles: " + str(len(self.level.friendlyProjectiles))
        projectileText = self.font.render(projectileString, True, lib.color.WHITE)
        return projectileText

    def getEnemyCount(self) -> pygame.Surface:
        enemyString = "Enemies: " + str(len(self.level.enemyContainer))
        enemyText = self.font.render(enemyString, True, lib.color.WHITE)
        return enemyText

    def changeWallVisibility(self, walls: pygame.sprite.Group) -> None:
        for wall in walls:
            if wall.image.get_colorkey() == lib.color.BLUE:
                wall.image.set_colorkey(lib.color.WHITE)
            else:
                wall.image.set_colorkey(lib.color.BLUE)

    def toggleActive(self, walls: pygame.sprite.Group) -> None:
        if self.active:
            self.active = False
        else:
            self.active = True

        self.changeWallVisibility(walls)

    def drawLineToMouse(self) -> None:
        rawMousePos = pygame.mouse.get_pos()
        worldMousePos = pygame.math.Vector2(rawMousePos[0], rawMousePos[1])

        pygame.draw.line(self.displaySurface, lib.color.RED, (self.player.pos.x - lib.globalOffset.x, self.player.pos.y - lib.globalOffset.y), (worldMousePos.x, worldMousePos.y), 1)

    def drawEnemyToTarget(self) -> None:
        for e in self.level.enemyContainer:
            pygame.draw.line(self.displaySurface, lib.color.GREEN, (e.pos.x - lib.globalOffset.x, e.pos.y - lib.globalOffset.y), (e.targetPos.x - lib.globalOffset.x, e.targetPos.y - lib.globalOffset.y), 1)

    def draw(self) -> None:
        self.displaySurface.blit(self.fpsText, (800, 10))
        self.displaySurface.blit(self.mouseText, (800, 30))
        self.displaySurface.blit(self.playerText, (800, 50))
        self.displaySurface.blit(self.projectileText, (800, 70))
        self.displaySurface.blit(self.enemyText, (800, 90))

    def update(self, clock: pygame.time.Clock):
        self.fpsText = self.getFps(clock)
        self.mouseText = self.getMousePos()
        self.playerText = self.getPlayerPos()
        self.projectileText = self.getProjectileCount()
        self.enemyText = self.getEnemyCount()

        if self.active:
            self.drawLineToMouse()
            self.drawEnemyToTarget()