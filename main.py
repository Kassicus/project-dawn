# Standard library imports
import pygame
import pygame.examples.fonty
import pygame.examples.freetype_misc

# Custom class imports
import player
import ui
import projectile
import menu
import debug
import world
import inventory
import itemLib
import reference

pygame.init() # This only needs to be called once, at the top of the primary game file (main.py)

# Main game class (despite being a class this will only ever be instanciated once)
class Game():
    def __init__(self):
        """This is the game, everything that is anything is done in here"""

        # Python screen setup
        self.screen = pygame.display.set_mode([reference.SCREEN_WIDTH, reference.SCREEN_HEIGHT])
        pygame.display.set_caption(reference.SCREEN_TITLE)

        # Game management variables
        self.running = True # Better than just saying while true
        self.clock = pygame.time.Clock() # System clock, allows for measuring delta time and capping the games framerate
        self.events = pygame.event.get() # Capturing this request into a variable to be used in other locations
        self.debugInterface = debug.DebugInterface() # Create an instance of the debug interface

        # Game object instances
        self.player = player.Player() # Our only instance of the player!
        self.healthBar = ui.StatusBar(10, 10, 200, 30, (87, 11, 6), (255, 0, 0), self.player.health, 100) # The players health bar, subject to change
        self.pMenu = menu.PlayerInventoryMenu(50, 45, (120,113,93,120), (0,150,0))
        reference.activeRoom = world.startingRoom # Set the current room to the "starting room" from the world file

    # This function starts the game, but also starts the game loop, it determines the order of logic
    def start(self):
        """Starts the main game loop, this is also what keeps everthing going"""

        while self.running: # This is really the main game loop (odd that its inside a function named start...)
            self.events = pygame.event.get() # Update our events list

            # Main event loop
            for event in self.events: # Parse the events list
                if event.type == pygame.QUIT: # Check for pygame.QUIT, called when the [X] for the game window is pressed
                    self.running = False # Set running to false, we could kill the game here but its cleaner to do it outside the loop. This allows the loop to finish its last run

                # TESTING
                # [y]: decrease player health
                # [u]: increase player health

                # [m]: show menu

                # [i]: Display your inventory in the terminal (Graphical display are a WIP)
                # [,]: Adds a short sword to your inventory

                if event.type == pygame.KEYDOWN: # Check for the keydown (does not repeat)
                    if event.key == pygame.K_u: # Check for the U key
                        if self.player.health <= 90: # If the player health is not full
                            self.player.health += 10 # Increase it!

                    if event.key == pygame.K_y: # Check for the Y key
                        if self.player.health >= 10: # If the player health is not empty
                            self.player.health -= 10 # Reduce it!

                    if event.key == pygame.K_m: # Check for the M key
                        if self.pMenu.isDrawn == False: # If the menu is not currently being drawn
                            self.pMenu.isDrawn = True # Draw it!
                        else: # If it is
                            self.pMenu.isDrawn = False # Close it!

                    if event.key == pygame.K_TAB: # Check for the TAB key
                        if self.debugInterface.active: # If the debug interface is currently active
                            self.debugInterface.active = False # Close it
                        else: # If its closed
                            self.debugInterface.active = True # Open it

                    if event.key == pygame.K_i: # Check for the I key
                        self.player.printInventory() # Call the players print inventory function

                    if event.key == pygame.K_COMMA: # Check for the COMMA key
                        inventory.addItem(self.player.inventory, itemLib.sword1) # Give the player something new!

            self.draw() # Call the draw function

            self.update() # Call the update function

    def draw(self):
        """Draws everything that is anything to the screen"""

        self.screen.fill(reference.BLACK) # Set the screen to black, paint over everything from the old frame

        reference.activeRoom.draw(self.screen) # Draw the active room, pass the screen because the rooms are not created in this file
        
        projectile._projectiles.draw(self.screen) # Draw all projectiles to the screen, also passes screen because those are not created in this file

        self.player.draw() # Draw the player, can reference the screen internally, no passthrough
        self.healthBar.draw() # Draw the healthbar ^^^

        # Draw the menu
        if self.pMenu.isDrawn == True: # If the menu should be drawn
            self.pMenu.draw() # Call the draw function

        # Draw the debug interface
        if self.debugInterface.active: # If the debug interface is true
            self.debugInterface.draw() # Call the draw function

    def update(self):
        """Updates everything that is anything"""

        self.player.update(self.events) # Update the player, pass events
        self.healthBar.update(self.player.health) # Update the healthbar, specifically pass the players health

        projectile._projectiles.update() # Update all projectiles

        # |IMPORTANT| Update all game elements before this point |IMPORTANT|
        reference.activeRoom.update(self.player) # Update the active room and pass the player for the doors!
        self.debugInterface.update(self.clock, self.player) # Give information to the debug interface so that it can be helpful
        pygame.display.update() # Update the display element
        reference.dt = self.clock.tick() / 1000 # Get the current delta time

if __name__ == '__main__': # This is literally the only part of the PEP 8 python standard we use...
    game = Game() # Create an instance of the game class
    game.start() # Start our instance of the game class
    pygame.quit() # When the game.running variables is set back to false, the code resumes here and this line kills the game and all other pygame/python tasks on the machine created by the game
    