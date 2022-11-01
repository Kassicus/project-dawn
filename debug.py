# Standard imports
import pygame

# Custom imports
import lib

class DebugInterface():
    def __init__(self) -> None:
        """Collects and draws out a ton of useful information"""

        self.font = pygame.font.SysFont("Courier", 16)
        self.fpsText = None
        self.mouseText = None
        self.playerText = None

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

    def getPlayerPos(self, player: pygame.sprite.Sprite) -> pygame.Surface:
        playerString = "Player: (" + str(player.rect.x) + ", " + str(player.rect.y) + ")"
        playerText = self.font.render(playerString, True, lib.color.WHITE)
        return playerText

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

    def drawLineToMouse(self, player: pygame.sprite.Sprite) -> None:
        rawMousePos = pygame.mouse.get_pos()
        worldMousePos = pygame.math.Vector2(rawMousePos[0], rawMousePos[1])

        pygame.draw.line(self.displaySurface, lib.color.RED, (player.pos.x - lib.globalOffset.x, player.pos.y - lib.globalOffset.y), (worldMousePos.x, worldMousePos.y), 1)

    def draw(self) -> None:
        self.displaySurface.blit(self.fpsText, (800, 10))
        self.displaySurface.blit(self.mouseText, (800, 30))
        self.displaySurface.blit(self.playerText, (800, 50))

    def update(self, clock: pygame.time.Clock, player: pygame.sprite.Sprite):
        self.fpsText = self.getFps(clock)
        self.mouseText = self.getMousePos()
        self.playerText = self.getPlayerPos(player)

        if self.active:
            self.drawLineToMouse(player)