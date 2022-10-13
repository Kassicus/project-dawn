# Standard library imports
import pygame

# Custom class imports
import projectile

#imports item library for inventory
import itemLib

# Primary player class (unless we ever end up with multiplayer, this will only ever be instanciated once)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Position variables
        self.x = 500
        self.y = 400

        # Velocity variables
        self.x_velocity = 0
        self.y_velocity = 0
        self.speed = 5

        # Bounding box variables
        self.width = 30
        self.height = 30

        # Generic player variables
        self.color = (255, 255, 255)
        self.facing = "right"
        self.health = 40

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = self.x - int(self.width / 2)
        self.rect.y = self.y - int(self.height / 2)

        # Player Currency
        self.mobSoulCount = 0
        self.miniBossSoulCount = 0
        self.regionBossSoulCount = 0

        #Player Inventory
        self.inventory = [itemLib.knife1, itemLib.pistol1, itemLib.shockMagic2]

    # Handles the drawing of all items player related (requires a drawable pygame.surface element, we use the game.screen var)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    # Hanldes all non-graphical updates and events (requires access to the game.events var)
    def update(self, events):
        # Update player location based on player velocity
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.rect.update(self.x - int(self.width / 2), self.y - int(self.height / 2), self.width, self.height)

        self.eventHandler(events)

    # Turn keyboard input into velocity to move the player
    def eventHandler(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN: # Check for the keydown event to add velocity
                # Check for left/right movement
                if event.key == pygame.K_a:
                    self.x_velocity = -self.speed
                elif event.key == pygame.K_d:
                    self.x_velocity = self.speed

                # Check for up/down movement
                if event.key == pygame.K_w:
                    self.y_velocity = -self.speed
                elif event.key == pygame.K_s:
                    self.y_velocity = self.speed

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
