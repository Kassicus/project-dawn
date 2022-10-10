# Standard library imports
import pygame

# Primary player class (unless we ever end up with multiplayer, this will only ever be instanciated once)
class Player():
    def __init__(self):
        # Position variables
        self.x = 500
        self.y = 400

        # Velocity variables
        self.x_velocity = 0
        self.y_velocity = 0
        self.speed = 5

        # Bounding box variables
        self.width = 25
        self.height = 25

        # Generic player variables
        self.color = (255, 255, 255)

    # Handles the drawing of all items player related (requires a drawable pygame.surface element, we use the game.screen var)
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 0) # Placeholder white square to indicate the player

    # Hanldes all non-graphical updates and events (requires access to the game.events var)
    def update(self, events):
        # Update player location based on player velocity
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.movementController(events)

    # Turn keyboard input into velocity to move the player
    def movementController(self, events):
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

            if event.type == pygame.KEYUP: # Check for the keyup event to remove velocity
                # Kill horizontal velocity
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    self.x_velocity = 0

                # Kill vertical velocity
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.y_velocity = 0
