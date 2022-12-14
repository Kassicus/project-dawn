import pygame

import lib

images = {
    # TODO this is going to be the doors image library
}

class Door(pygame.sprite.Sprite):
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        rotation: int
    ) -> None:

        super().__init__()

        self.open = False
        self.rotation = rotation

        self.pos = pygame.math.Vector2(x * 50, y * 50)

        # TODO Load the correct door image on init

        self.image = pygame.Surface([width * 50, height * 50])
        self.image.fill(lib.color.GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def getState(self) -> bool:
        return self.open

    def changeState(self) -> None:
        if self.open:
            self.open = False
        else:
            self.open = True

        if self.open:
            self.image.set_colorkey(lib.color.GREEN)
            lib.levelref.collidables.remove(self)
        else:
            self.image.set_colorkey(lib.color.WHITE)
            lib.levelref.collidables.add(self)

        # TODO Open and close the door sprites
        