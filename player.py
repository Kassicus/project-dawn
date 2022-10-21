# Standard library imports
import pygame
import math
import random

# Custom class imports
import projectile
import particle
import reference
import animation

#imports item library for inventory
import itemLib

# Primary player class (unless we ever end up with multiplayer, this will only ever be instanciated once)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        """Contains and controlls everything player related"""
        pygame.sprite.Sprite.__init__(self) # Initialize the super class

        # Position variables
        self.pos = pygame.math.Vector2(500, 400) # Vector to store x and y
        self.direction = pygame.math.Vector2() # Vector to store change in x and y

        # Generic player variables
        self.health = 40 # Player health (currently arbitrary)
        self.speed = 200 # This speed needs to be big because of the recent change to delta time

        # Player animation
        self.animation = animation.Animation( # Create the animation
            [
                pygame.image.load("assets/player/animation/anim_1.png").convert_alpha(), # Add all of the images in the players animation
                pygame.image.load("assets/player/animation/anim_2.png").convert_alpha(), # The second
                pygame.image.load("assets/player/animation/anim_3.png").convert_alpha(), # The third
                pygame.image.load("assets/player/animation/anim_4.png").convert_alpha() # The fourth
            ],
            4) # Animation speed

        # Image and drawing variables
        self.displaySurface = pygame.display.get_surface() # Get the display surface from the location that the class is instanciated
        self.image = self.animation.frames[0] # Get the first animation frame
        self.rect = self.image.get_rect() # Get the rect (w, h) of the loaded image
        self.rect.center = self.pos # Set the center of the rect to the player position

        # Player Currency
        self.mobSoulCount = 0
        self.miniBossSoulCount = 0
        self.regionBossSoulCount = 0

        #Player Inventory
        self.inventory = [itemLib.knife1, itemLib.pistol1, itemLib.shockMagic2]

    def draw(self):
        """Draw the player and all relative player objects/items"""
        self.image = self.animation.animate() # Update the image to the latest animation image
        rotated = self.rotateToMouse() # Get a copy of the latest rotated player and rect
        self.displaySurface.blit(rotated[0], rotated[1]) # Blit the latest rotated player surface (rotated[0]) at the latest rect position (rotated[1])

    def update(self, events):
        """Update the player
        
        Keyword argumements:
        events (pygame.event) : the output of pygame.event.get() (should be from main.py)
        """
    
        self.pos += self.direction * reference.dt # Add the direction vector to the player vector and multiply by delta time to get framerate independant movement
        self.rect.center = self.pos # update the center of the player

        self.eventHandler(events) # This is where the events really need to go

        # Testing the rapid fire weapon
        if pygame.mouse.get_pressed()[2]: # Check if the right click button is being held
            mouseX, mouseY = pygame.mouse.get_pos() # Get the current mouse position
            p = projectile.Projectile(self.pos.x, self.pos.y, mouseX, mouseY, 3, 3, particle.MagicParticleSystem(self.pos.x, self.pos.y), 400, "magic") # Fire a mothafuc*in projectile
            projectile._projectiles.add(p) # Make sure the projectile gets added to the global projectile list

    def printInventory(self):
        """Print everything in the player inventory to the terminal"""

        print("Your inventory consists of:\n ") # Print the header
        for x in self.inventory: # Go through each item
            print(x.itemName + ":", x.itemDescription) # Print the item name : description
        print("") # Empty line at the bottom to keep things clean

    def rotateToMouse(self):
        """Determine the angle from the player to the mouse, rotate player to that angle
        
        Returns:
        as (rotatedImage, newRect)\n
        rotatedImage (pygame.surface) : the image file after the rotation has been performed
        newRect (pygame.rect) : the updated rect to keep the image at its centerpoint
        """
        
        mouseX, mouseY = pygame.mouse.get_pos() # Get the mouse position
        angle = math.atan2(self.rect.x - mouseX, self.rect.y - mouseY) # Determine the angle of the two points using arc-tangent
        degrees = math.degrees(angle) # Convert the angle to degrees

        rotatedImage = pygame.transform.rotate(self.image, degrees) # Rotate the image based on those degrees
        newRect = rotatedImage.get_rect(center = self.image.get_rect(center = self.pos).center) # Get the new rect of the rotated image and adjust the center

        return(rotatedImage, newRect) # Return new player image and rect

    # Turn keyboard input into velocity to move the player
    def eventHandler(self, events):
        """Handles anything to do with pygame.event that needs to interact with the player
        
        Keyword arguments:
        events (pygame.event) : passed from self.update(), should be pygame.event.get() from main.py
        """
        
        keys = pygame.key.get_pressed() # Keep a list of all keys currently being pressed

        if keys[pygame.K_a]: # Check for the A key
            self.direction.x = -self.speed # Change the x part of the direction vector to -speed (move left)
        elif keys[pygame.K_d]: # Check for the D key
            self.direction.x = self.speed # Change the x part of the direction vector to speed (move right)
        else: # If none of our horizontal keys are being pressed
            self.direction.x = 0 # We get no horizontal movement

        if keys[pygame.K_w]: # Check for the W key
            self.direction.y = -self.speed # Change the y part of the direction vector to -speed (move up)
        elif keys[pygame.K_s]: # Checkf or the S key
            self.direction.y = self.speed # Change the y part of the direction vector to speed (move down)
        else: # If none of our vertical keys are being pressed
            self.direction.y = 0 # We get no vertical movement

        for event in events: # Parse events call
            if event.type == pygame.MOUSEBUTTONDOWN: # Check for the mousebuttondown event (this does not repeat when the button is held)
                if event.button == pygame.BUTTON_LEFT: # Check for the left click
                    mouseX, mouseY = pygame.mouse.get_pos() # Get the current mouse position
                    p = projectile.Projectile(self.pos.x, self.pos.y, mouseX, mouseY, 5, 5, particle.FireParticleSystem(self.pos.x, self.pos.y), 300, random.choice(["fireball", "fireball 2"])) # Create the projectile
                    projectile._projectiles.add(p) # Add the projectile to the global projectile list
