# Standard library imports
import pygame
import math

# Custom class imports
import projectile
import particle
import uni

#imports item library for inventory
import itemLib
import inventory

# Primary player class (unless we ever end up with multiplayer, this will only ever be instanciated once)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Position variables
        self.pos = pygame.math.Vector2(500, 400)
        self.direction = pygame.math.Vector2()

        self.speed = 200

        # Bounding box variables
        self.width = 1
        self.height = 1

        # Generic player variables
        self.color = (255, 255, 255)
        self.facing = "right"
        self.health = 40

        self.display_surface = pygame.display.get_surface()

        self.image = pygame.image.load("assets/player/temp.png")

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # Player Currency
        self.mobSoulCount = 0
        self.miniBossSoulCount = 0
        self.regionBossSoulCount = 0

        #Player Inventory
        self.inventory = [itemLib.knife1, itemLib.pistol1, itemLib.shockMagic2]


    # Handles the drawing of all items player related (requires a drawable pygame.surface element, we use the game.screen var)
    def draw(self):
        rotated = self.rotateToMouse()
        self.display_surface.blit(rotated[0], rotated[1])

    # Hanldes all non-graphical updates and events (requires access to the game.events var)
    def update(self, events):
        # Update player location based on player velocity
        self.pos += self.direction * uni.dt
        self.rect.center = self.pos

        #self.rect.update(self.x - int(self.width / 2), self.y - int(self.height / 2), self.width, self.height)

        self.eventHandler(events)

        if pygame.mouse.get_pressed()[2]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            p = projectile.Projectile(self.pos.x, self.pos.y, mouse_x, mouse_y, 3, 3, particle.MagicParticleSystem(self.pos.x, self.pos.y), 400)
            projectile._projectiles.add(p)

    def rotateToMouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(self.rect.x - mouse_x, self.rect.y - mouse_y)
        degrees = math.degrees(angle)

        rotatedImage = pygame.transform.rotate(self.image, degrees)
        new_rect = rotatedImage.get_rect(center = self.image.get_rect(center = self.pos).center)

        return(rotatedImage, new_rect)

    # Turn keyboard input into velocity to move the player
    def eventHandler(self, events):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.direction.x = -self.speed
        elif keys[pygame.K_d]:
            self.direction.x = self.speed
        else:
            self.direction.x = 0

        if keys[pygame.K_w]:
            self.direction.y = -self.speed
        elif keys[pygame.K_s]:
            self.direction.y = self.speed
        else:
            self.direction.y = 0

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    p = projectile.Projectile(self.pos.x, self.pos.y, mouse_x, mouse_y, 5, 5, particle.FireParticleSystem(self.pos.x, self.pos.y), 300)
                    projectile._projectiles.add(p)
