# Standard imports
import pygame
import random

# Custom imports
import lib
import camera
import player
import wall
import door
import particle
import enemy

class Level():
    def __init__(self, backgroundPath: str) -> None:
        """Initialize the level
        
        Arguments:
        backgroundPath: str - The path of the background image to be used for the level
        """
        lib.levelref = self

        # Display setup
        self.displaySurface = pygame.display.get_surface() # Get the drawable surface from the main game
        self.levelBackground = pygame.image.load(backgroundPath).convert_alpha() # Load the background passed on class creation
        
        # Early level setup
        self.worldCamera = camera.PlayerCenterCamera(self.displaySurface, self.levelBackground) # Create a camera that tracks the player
        self.player = player.Player() # Create the player
        self.collidables = pygame.sprite.Group() # Create a group to hold all collidable objects
        self.wallContainer = pygame.sprite.Group() # Held here to access all walls
        self.doorContainer = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()
        self.friendlyProjectiles = pygame.sprite.Group()
        self.hostileProjectiles = pygame.sprite.Group()
        self.enemyContainer = pygame.sprite.Group()

        # Create all of the walls (these should match the walls drawn on the background)
        self.walls = [ # Walls are 'point arrays' [x: int, y: int, width: int, height: int]
        [2, 2, 10, 1], [2, 3, 1, 10], [2, 13, 10, 1], [11, 12, 1, 1], [11, 3, 1, 7], [12, 9, 6, 1], [18, 6, 1, 4], [18, 5, 17, 1],
        [22, 6, 1, 4], [26, 6, 1, 4], [30, 6, 1, 4], [22, 12, 1, 4], [26, 12, 1, 4], [30, 12, 1, 4], [34, 6, 1, 10], [18, 16, 17, 1],
        [18, 12, 1, 4], [12, 12, 1, 1], [17, 12, 1, 1], [13, 12, 1, 6], [16, 12, 1, 6], [5, 18, 9, 1], [16, 18, 9, 1], [5, 19, 1, 18],
        [24, 19, 1, 18], [5, 37, 9, 1], [16, 37, 9, 1], [13, 38, 1, 4], [16, 38, 1, 4], [12, 41, 1, 1], [17, 41, 1, 1], [11, 38, 1, 4],
        [18, 38, 1, 4], [4, 38, 7, 1], [19, 38, 7, 1], [4, 39, 1, 8], [25, 39, 1, 8], [4, 47, 8, 1], [11, 44, 1, 3], [12, 44, 7, 1],
        [18, 45, 1, 3], [19, 47, 7, 1]
        ]

        self.doors = [
        [11, 10, 1, 2], [18, 10, 1, 2], [19, 9, 3, 1], [23, 9, 3, 1], [27, 9, 3, 1], [31, 9, 3, 1], [19, 12, 3, 1], [23, 12, 3, 1],
        [27, 12, 3, 1], [31, 12, 3, 1]
        ]

        self.turretLocations = [
        [20, 7], [24, 7], [28, 7], [32, 7]
        ]

        # Late level setup
        self.createWalls(self.walls) # Create the walls, the get added to collidables
        self.createDoors(self.doors)
        self.createTurrets()
        self.worldCamera.add(self.player) # Add the player to the world camera

        # TODO: Refactor this, move into player?
        self.player.particleSystem = particle.PlayerParticleSystem() # Create the players particle system and add it to the world camera

    def draw(self) -> None:
        """Draw the level"""

        self.worldCamera.cameraDraw(self.player) # The camera needs access to the player in order to function

    def update(self) -> None:
        """Update the level"""

        self.worldCamera.update() # Update everything contained in the camera
        self.checkCollisions() # Check collisions
        self.friendlyProjectiles.update()
        self.hostileProjectiles.update()
        self.enemyContainer.update()
        self.particles.update()
        
        for e in self.enemyContainer:
            if e.tag == "chaser":
                e.chasePlayer(self.player)
            if e.tag == "turret":
                e.shootAtPlayer(self.player)

        self.friendlyProjectileCollision()
        #self.hostileProjectileCollision()

    def createWalls(self, wallArray: list) -> None:
        """Creates walls for each entry in self.walls
        
        Arguments:
        wallArray: list - List of lists, should be self.walls
        """

        # Make all of the walls
        for pointArray in range(len(wallArray)): # For each entry in the point array
            w = wall.Wall(wallArray[pointArray][0], wallArray[pointArray][1], wallArray[pointArray][2], wallArray[pointArray][3]) # Create a wall based on the points in each arrray
            self.worldCamera.add(w) # Add the wall to the camera to be drawn TODO make invisible
            self.collidables.add(w) # Add the wall to the collidables to make the player hit it
            self.wallContainer.add(w)

    def createDoors(self, doorArray: list) -> None:
        for pointArray in range(len(doorArray)):
            d = door.Door(doorArray[pointArray][0], doorArray[pointArray][1], doorArray[pointArray][2], doorArray[pointArray][3])
            self.worldCamera.add(d)
            self.collidables.add(d)
            self.doorContainer.add(d)

    def checkCollisions(self) -> None:
        """Check the collisions between the player and everthing in the collidables group"""

        collisionTollerance = 15 # The maximum overlap that two collidables objects can have (we might need to tweak this once we get animations working)

        # Check all of the collisions
        for c in self.collidables: # Parse the collidables group
            for p in self.friendlyProjectiles:
                if p.rect.colliderect(c.rect):
                    p.destroy()

            for p in self.hostileProjectiles:
                if p.rect.colliderect(c.rect):
                    p.destroy()

            if self.player.rect.colliderect(c.rect): # If the player collides with a collidable
                # Horizontal
                if abs(self.player.rect.left - c.rect.right) < collisionTollerance: # Check the positive horizontal collision
                    self.player.velo.x = 0 # Kill velocity
                    self.player.pos.x = c.rect.right + self.player.rect.width / 2 # Set the player to the right spot
                if abs(self.player.rect.right - c.rect.left) < collisionTollerance: # Check the negative horizontal collision
                    self.player.velo.x = 0 # Kill velocity
                    self.player.pos.x = c.rect.left - self.player.rect.width / 2 # Set the player to the right spot
                # Vertical
                if abs(self.player.rect.top - c.rect.bottom) < collisionTollerance: # Check the positive vertical collision
                    self.player.velo.y = 0 # Kill velocity
                    self.player.pos.y = c.rect.bottom + self.player.rect.height / 2 # Set the player to the right spot
                if abs(self.player.rect.bottom - c.rect.top) < collisionTollerance: # Check the negative vertical collision
                    self.player.velo.y = 0 # Kill velocity
                    self.player.pos.y = c.rect.top - self.player.rect.height / 2 # Set the player to the right spot

    def friendlyProjectileCollision(self) -> None:
        for e in self.enemyContainer:
            for p in self.friendlyProjectiles:
                if e.rect.colliderect(p.rect):
                    e.health -= p.damage
                    p.destroy()

    def hostileProjectileCollision(self) -> None:
        for p in self.hostileProjectiles:
            if self.player.rect.colliderect(p.rect):
                self.player.health -= p.damage
                p.destroy()

    def createTurrets(self):
        for x in range(len(self.turretLocations)):
            e = enemy.TurretEnemy(int((self.turretLocations[x][0] * 50) + 25), int((self.turretLocations[x][1] * 50) + 25), 30)
            self.enemyContainer.add(e)
            self.worldCamera.add(e)

    def createEnemies(self, count: int) -> None:
        for c in range(count):
            c = enemy.ChaserEnemy(random.randint(0, 1000), random.randint(0, 800), 20, 100)
            self.worldCamera.add(c)
            self.enemyContainer.add(c)