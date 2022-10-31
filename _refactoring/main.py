# Standard Imports
import pygame

# Custom Imports
import lib
import level

pygame.init() # Initialize the pygame module (called once)

class Game(): # Main game class
    def __init__(self) -> None:
        """Initialize the main game, referencing the lib script"""

        # Game window setup
        self.screen = pygame.display.set_mode([lib.SCREEN_WIDTH, lib.SCREEN_HEIGHT]) # Create the game window
        pygame.display.set_caption(lib.SCREEN_TITLE) # Set the game window caption

        # Vars needed to make the game run
        self.running = True # If this gets set to false we close the game
        self.clock = pygame.time.Clock() # The main clock element
        self.events = pygame.event.get() # Holds all of our events

        # Gameplay vars
        self.level = level.Level("_refactoring/assets/background/test_1.png") # The level, this holds most of our logic

    def run(self) -> None:
        """Calls all of the functions that run the game"""

        # Main game loop
        while self.running: # While the game is happening
            self.eventHandler() # Process all events
            self.draw() # Draw eveything to the screen
            self.update() # Apply all of the new processes

    def eventHandler(self) -> None:
        """Handles all input/event logic for the game"""

        self.events = pygame.event.get() # Refresh our event list
        for event in self.events: # Parse the event list
            if event.type == pygame.QUIT: # If we hear the quit event
                self.running = False # Stop the game from running

    def draw(self) -> None:
        """Handles drawing all graphical elements"""

        # Refresh the screen
        self.screen.fill(lib.color.BLACK) # Fill the screen, effectively erases the screen every frame

        # Draw everything here, things are drawn to screen in order, items at the bottom are drawn over items at the top
        self.level.draw() # Invoke the active levels draw method

    def update(self) -> None:
        """Updates everything, applies all physics/events changes"""

        # Do all game logic here
        self.level.update() # Update the game level

        # Do these last
        pygame.display.update() # Update the display (push the new elements from the draw method)
        lib.deltaTime = self.clock.tick(120) / 1000 # Update the delta time and tick the clock (locked to 120fps)

# Run the game
if __name__ == '__main__': # Fun python stuff
    game = Game() # Create an instance of the game
    game.run() # Tell that instance to run
    pygame.quit() # When the game is no longer running, kill pygame and cleanup
