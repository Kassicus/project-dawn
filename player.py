# Standard library imports
import pygame

# Custom class imports
import projectile

# Primary player class (unless we ever end up with multiplayer, this will only ever be instanciated once)
class Player():
    def __init__(self):
        # Position variables
        self.x = 500
        self.y = 400

        self.pos = (self.x, self.y)

        # Velocity variables
        self.x_velocity = 0
        self.y_velocity = 0
        self.speed = 5

        # Bounding box variables
        self.width = 50
        self.height = 50

        # Generic player variables
        self.color = (255, 255, 255)
        self.facing = "right"
        self.health = 40

        # Player Currency
        self.mobSoulCount = 0
        self.miniBossSoulCount = 0
        self.regionBossSoulCount = 0

    # Handles the drawing of all items player related (requires a drawable pygame.surface element, we use the game.screen var)
    def draw(self, surface):
        pygame.draw.rect(surface, (25, 100, 255), (self.x, self.y, self.width, self.height), 0)

    # Hanldes all non-graphical updates and events (requires access to the game.events var)
    def update(self, events):
        # Update player location based on player velocity
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.pos = (self.x, self.y)

        self.eventHandler(events)

    # Turn keyboard input into velocity to move the player
    def eventHandler(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN: # Check for the keydown event to add velocity
                # Check for left/right movement
                if event.key == pygame.K_a:
                    self.x_velocity = -self.speed
                    self.facing = "left"
                elif event.key == pygame.K_d:
                    self.x_velocity = self.speed
                    self.facing = "right"

                # Check for up/down movement
                if event.key == pygame.K_w:
                    self.y_velocity = -self.speed
                    self.facing = "away"
                elif event.key == pygame.K_s:
                    self.y_velocity = self.speed
                    self.facing = "forward"

                if event.key == pygame.K_SPACE:
                    p = projectile.Projectile(self.x, self.y, self.facing, 12, 5, (0, 255, 0))
                    projectile._projectiles.add(p)

                if event.key == pygame.K_g:
                    p = projectile.Projectile(self.x, self.y, self.facing, 4, 20, (0, 0, 255))
                    projectile._projectiles.add(p)

            if event.type == pygame.KEYUP: # Check for the keyup event to remove velocity
                # Kill horizontal velocity
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.x_velocity = 0

                # Kill vertical velocity
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.y_velocity = 0
