# Standard library imports
import pygame

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
        self.width = 25
        self.height = 40

        # Player sprites
        self.right_sprite = pygame.image.load("assets/player/right.png")
        self.left_sprite = pygame.image.load("assets/player/left.png")
        self.away_sprite = pygame.image.load("assets/player/away.png")
        self.forward_sprite = pygame.image.load("assets/player/forward.png")

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
        if self.facing == "right":
            surface.blit(self.right_sprite, self.pos)
        elif self.facing == "left":
            surface.blit(self.left_sprite, self.pos)
        elif self.facing == "away":
            surface.blit(self.away_sprite, self.pos)
        elif self.facing == "forward":
            surface.blit(self.forward_sprite, self.pos)

    # Hanldes all non-graphical updates and events (requires access to the game.events var)
    def update(self, events):
        # Update player location based on player velocity
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.pos = (self.x, self.y)

        self.movementController(events)

    # Turn keyboard input into velocity to move the player
    def movementController(self, events):
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

            if event.type == pygame.KEYUP: # Check for the keyup event to remove velocity
                # Kill horizontal velocity
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.x_velocity = 0

                # Kill vertical velocity
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.y_velocity = 0
