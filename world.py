import pygame
import layouts
import projectile
import reference

class Chunk(pygame.sprite.Sprite):
    def __init__(self, x, y, chunkId, room):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pygame.math.Vector2(x, y)

        self.width = 50
        self.height = 50

        self.chunkId = chunkId
        self.wall = False

        self.room = room
        
        self.layout = self.room.layout[self.chunkId]
        
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

        self.doors = []

        self.createChunks()

    def createChunks(self):
        chunkId = 0

        for y in range(int(self.height / 50)):
            for x in range(int(self.width / 50)):
                c = Chunk(int(x * 50), int(y * 50), chunkId, self)
                self.chunks.add(c)
                chunkId += 1

    def draw(self, surface):
        self.chunks.draw(surface)

    def update(self, player):
        self.chunks.update()
        try:
            for door in self.doors:
                door.update(player)
        except:
            pass

    def containsPlayer(self, player):
        collide = pygame.sprite.spritecollide(player, self.chunks, True)

        for chunk in collide:
            return chunk.chunk_id

class Door():
    def __init__(self, x, y, width, height, targetRoom, sx, sy):
        self.pos = pygame.math.Vector2(x, y)
        self.width = width
        self.height = height

        self.targetRoom = targetRoom

        self.spawnPos = pygame.math.Vector2(sx, sy)

    def update(self, player):
        if self.pos.x < player.pos.x < self.pos.x + self.width:
            if self.pos.y < player.pos.y < self.pos.y + self.height:
                reference.activeRoom = self.targetRoom
                player.pos = self.spawnPos

startingRoom = Room(layouts.startingRoom)
secondRoom = Room(layouts.secondRoom)
thirdRoom = Room(layouts.thirdRoom)

doorOne = Door(150, 0, 100, 50, secondRoom, 175, 720)
startingRoom.doors.append(doorOne)

doorTwo = Door(150, 750, 100, 50, startingRoom, 175, 75)
secondRoom.doors.append(doorTwo)

doorThree = Door(950, 250, 50, 100, thirdRoom, 75, 275)
secondRoom.doors.append(doorThree)

doorFour = Door(0, 250, 50, 100, secondRoom, 875, 275)
thirdRoom.doors.append(doorFour)