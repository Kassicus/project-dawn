import pygame

class LinkedPlayerCamera(pygame.sprite.Group):
    def __init__(self, displaySurface):
        pygame.sprite.Group.__init__(self)
        self.displaySurface = displaySurface

    def cameraDraw(self):
        for sprite in self.sprites():
            self.displaySurface.blit(sprite.image, sprite.rect)

class PlayerCenterCamera(pygame.sprite.Group):
    def __init__(self, displaySurface, groundSurface):
        pygame.sprite.Group.__init__(self)
        self.displaySurface = displaySurface
        self.halfWidth = self.displaySurface.get_size()[0] // 2
        self.halfHeight = self.displaySurface.get_size()[1] // 2

        self.groundSurface = groundSurface
        self.groundRect = self.groundSurface.get_rect(topleft = (0, 0))
        self.offset = pygame.math.Vector2()

    def centerTargetCamera(self, target):
        self.offset.x = target.rect.centerx - self.halfWidth
        self.offset.y = target.rect.centery - self.halfHeight

    def cameraDraw(self, player):
        self.centerTargetCamera(player)

        groundOffset = self.groundRect.topleft - self.offset
        self.displaySurface.blit(self.groundSurface, groundOffset)

        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offsetPos = sprite.rect.topleft - self.offset
            self.displaySurface.blit(sprite.image, offsetPos)
