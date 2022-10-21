# Standard library imports
import pygame
import projectile

class DebugInterface():
    def __init__(self):
        """ Gets a ton of useful information and displays it for the user"""

        # Font and text variables
        self.font = pygame.font.SysFont("Courier", 16) # Set the font to a system default Courier size 16
        self.fpsText = None # Temp var for the fps
        self.mouseText = None # Temp var for the mouse
        self.playerText = None # Temp var for the player
        self.projectileText = None # Temp var for the projectiles
        self.particleText = None # Temp var for the particles

        # Drawing variables
        self.displaySurface = pygame.display.get_surface() # Get the main display surface
        self.active = False # By default we should be inactive

    def getFps(self, clock):
        """Get the FPS and convert it to a user friendly format
        
        Keyword arguments:
        clock (pygame.clock) : the main clock for the game
        
        Returns:
        fpsText (object) : the blit-able rendered text of the FPS
        """
        
        fpsString = "FPS:     " + str(int(clock.get_fps())) # Create a string containing the fps value
        fpsText = self.font.render(fpsString, 1, (255, 255, 255)) # Convert that string to an object
        return fpsText # Return said object

    def getMouse(self):
        """Get the mouse pos
        
        Returns:
        mouseText (object) : the blit-able rendered text of the mouse posision"""

        mouseString = "Mouse:  " + str(pygame.mouse.get_pos()) # Get the mouse position in a string
        mouseText = self.font.render(mouseString, 1, (255, 255, 255)) # Convert the string to an object
        return mouseText # Return said object

    def getPlayer(self, player):
        """Get the player position
        
        Keyword arguments:
        player (object) : the player for the game
        
        Returns:
        playerText (object) : the blit-able rendered text of the player position
        """
        
        playerString = "Player: (" + str(player.rect.x) + ", " + str(player.rect.y) + ")" # Get the player position in a string
        playerText = self.font.render(playerString, 1, (255, 255, 255)) # Convert that string to an object
        return playerText # Return said object

    def getProjectileCount(self):
        """Get the count of projectiles that are alive
        
        Returns:
        projectileText (object) : the blit-able rendered text of the projectile count
        """
        
        projectileString = "Proj:    " + str(int(len(projectile._projectiles))) # Get the count of projectiles in a string
        projectileText = self.font.render(projectileString, 1, (255, 255, 255)) # Convert the string to an object
        return projectileText # Return said object

    def getParticleCount(self):
        """Get the count of all particles on screen
        
        Returns:
        particleText (object) : the blit-able rendered text of the particle count
        """
        
        particles = 0 # Particles starts over at 0 for each render
        for p in projectile._projectiles: # Parse the projectiles
            count = len(p.particleSystem.particles) # Get the current particle count for each projectile
            particles += count # Add that to the overall particle count
        particleString = "Part:    " + str(particles) # Get the count of particles in a string
        particleText = self.font.render(particleString, 1, (255, 255, 255)) # Convert the string to an object
        return particleText # Return said object

    def draw(self):
        """Draw all of the fonts to the surface"""

        pygame.draw.rect(self.displaySurface, (0, 0, 0), (780, 0, 220, 110), 0) # Draw the background
        self.displaySurface.blit(self.fpsText, (800, 10)) # Draw the fps text
        self.displaySurface.blit(self.mouseText, (800, 30)) # Draw the mouse position
        self.displaySurface.blit(self.playerText, (800, 50)) # Draw the player position
        self.displaySurface.blit(self.projectileText, (800, 70)) # Draw the count of projectiles
        self.displaySurface.blit(self.particleText, (800, 90)) # Draw the count of particles

    def update(self, clock, player):
        """Update all of the fonts
        
        Keyword arguments:
        clock (pygame.clock) : Needed for the fps text
        player (object) : Needed to get the player position
        """
        
        self.fpsText = self.getFps(clock) # Update the fps text
        self.mouseText = self.getMouse() # Update the mouse text
        self.playerText = self.getPlayer(player) # Update the player text
        self.projectileText = self.getProjectileCount() # Update the projectile text
        self.particleText = self.getParticleCount() # Update the particle text