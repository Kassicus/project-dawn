import pygame
import random
import layouts
import projectile

class Chunk(pygame.sprite.Sprite):
    def __init__(self, x, y, chunk_id):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)

        self.width = 50
        self.height = 50

        self.chunk_id = chunk_id
        self.wall = False
        
        self.layout = layouts.active_layout[self.chunk_id]
        
        if self.layout != 0:
            self.wall = True
        
        self.image = layouts.tiles[self.layout]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.update(self.pos.x, self.pos.y, self.width, self.height)

        if self.wall:
            self.collide()

    def collide(self):
        for p in projectile._projectiles:
            if self.pos.x < p.pos.x < self.pos.x + self.width:
                if self.pos.y < p.pos.y < self.pos.y + self.height:
                    p.kill()

class Room():
    def __init__(self):
        self.chunks = pygame.sprite.Group()

        self.width = 1000
        self.height = 800

        self.display_surface = pygame.display.get_surface()

        self.createChunks()

    def createChunks(self):
        chunk_id = 0

        for y in range(int(self.height / 50)):
            for x in range(int(self.width / 50)):
                c = Chunk(int(x * 50), int(y * 50), chunk_id)
                self.chunks.add(c)
                chunk_id += 1

    def draw(self):
        self.chunks.draw(self.display_surface)

    def update(self):
        self.chunks.update()

    def containsPlayer(self, player):
        collide = pygame.sprite.spritecollide(player, self.chunks, True)

        for chunk in collide:
            return chunk.chunk_id

class Door():
    def __init__(self):
        pass

