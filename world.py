import pygame
import layouts
import projectile
import uni

class Chunk(pygame.sprite.Sprite):
    def __init__(self, x, y, chunk_id, room):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)

        self.width = 50
        self.height = 50

        self.chunk_id = chunk_id
        self.wall = False

        self.room = room
        
        self.layout = self.room.layout[self.chunk_id]
        
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
    def __init__(self, layout):
        self.chunks = pygame.sprite.Group()

        self.width = 1000
        self.height = 800

        self.layout = layout

        self.door = None

        self.createChunks()

    def createChunks(self):
        chunk_id = 0

        for y in range(int(self.height / 50)):
            for x in range(int(self.width / 50)):
                c = Chunk(int(x * 50), int(y * 50), chunk_id, self)
                self.chunks.add(c)
                chunk_id += 1

    def draw(self, surface):
        self.chunks.draw(surface)

    def update(self, player):
        self.chunks.update()
        self.door.update(player)

    def containsPlayer(self, player):
        collide = pygame.sprite.spritecollide(player, self.chunks, True)

        for chunk in collide:
            return chunk.chunk_id

class Door():
    def __init__(self, x, y, width, height, target_room, sx, sy):
        self.pos = pygame.math.Vector2(x, y)
        self.width = width
        self.height = height

        self.target_room = target_room

        self.spawn_pos = pygame.math.Vector2(sx, sy)

    def update(self, player):
        if self.pos.x < player.pos.x < self.pos.x + self.width:
            if self.pos.y < player.pos.y < self.pos.y + self.height:
                uni.active_room = self.target_room
                player.pos = self.spawn_pos

starting_room = Room(layouts.starting_room)
second_room = Room(layouts.second_room)

starting_room_door = Door(150, 0, 100, 50, second_room, 175, 720)
starting_room.door = starting_room_door

second_room_door = Door(150, 750, 100, 50, starting_room, 175, 75)
second_room.door = second_room_door