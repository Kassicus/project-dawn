# Standard imports
import pygame
import random

# Custom imports
import camera
import player
import wall
import particle
import enemy

class Level():
    def __init__(self, backgroundPath: str) -> None:
        """Initialize the level
        
        Arguments:
        backgroundPath: str - The path of the background image to be used for the level
        """

        # Display setup
        self.displaySurface = pygame.display.get_surface() # Get the drawable surface from the main game
        self.levelBackground = pygame.image.load(backgroundPath).convert_alpha() # Load the background passed on class creation
        
        # Early level setup
        self.worldCamera = camera.PlayerCenterCamera(self.displaySurface, self.levelBackground) # Create a camera that tracks the player
        self.player = player.Player(self) # Create the player
        self.collidables = pygame.sprite.Group() # Create a group to hold all collidable objects
        self.wallContainer = pygame.sprite.Group() # Held here to access all walls
        self.friendlyProjectiles = pygame.sprite.Group()
        self.hostileProjeciles = pygame.sprite.Group()
        self.enemyContainer = pygame.sprite.Group()

        # Create all of the walls (these should match the walls drawn on the background)
        self.walls = [ # Walls are 'point arrays' [x: int, y: int, width: int, height: int]
        [0, 0, 50, 300],
        [200, 300, 300, 50]
        ]

        # Late level setup
        self.createWalls(self.walls) # Create the walls, the get added to collidables
        self.worldCamera.add(self.player) # Add the player to the world camera

        # TODO: Refactor this, move into player?
        self.player.particleSystem = particle.PlayerParticleSystem(self.worldCamera) # Create the players particle system and add it to the world camera

    def draw(self) -> None:
        """Draw the level"""

        self.worldCamera.cameraDraw(self.player) # The camera needs access to the player in order to function

    def update(self) -> None:
        """Update the level"""

        self.worldCamera.update() # Update everything contained in the camera
        self.checkCollisions() # Check collisions
        self.friendlyProjectiles.update()
        self.hostileProjeciles.update()
        self.enemyContainer.update()
        
        for e in self.enemyContainer:
            e.chasePlayer(self.player)

        self.friendlyProjectileCollision()

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

    def checkCollisions(self) -> None:
        """Check the collisions between the player and everthing in the collidables group"""

        collisionTollerance = 15 # The maximum overlap that two collidables objects can have (we might need to tweak this once we get animations working)

        # Check all of the collisions
        for c in self.collidables: # Parse the collidables group
            for p in self.friendlyProjectiles:
                if p.rect.colliderect(c.rect):
                    p.kill()

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
                    p.kill()

    def createEnemies(self, count: int) -> None:
        for c in range(count):
            c = enemy.ChaserEnemy(random.randint(0, 1000), random.randint(0, 800), 20, 100, self.displaySurface)
            self.worldCamera.add(c)
            self.enemyContainer.add(c)