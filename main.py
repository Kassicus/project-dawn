# Standard library imports
import pygame

# Custom class imports
import player

pygame.init() # This only needs to be called once, at the top of the primary game file (main.py)

# Main game class (despite being a class this will only ever be instanciated once)
class Game():
    def __init__(self):
        # Window information variables
        self.screen_width = 1000
        self.screen_height = 800
        self.window_title = "Project Dawn"

        # Python screen setup
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        pygame.display.set_caption(self.window_title)

        # Game management variables
        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get() # Capturing this request into a variable to be used in other locations

        # Game object instances
        self.player = player.Player()

    # This function starts the game, but also starts the game loop, it determines the order of logic
    def start(self):
        while self.running:
            self.events = pygame.event.get()

            # Main event loop
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    # Everything that needs to be drawn (graphical-updates) goes here
    def draw(self):
        self.screen.fill((0, 0, 0))
        # Draw all screen elements after this point

        self.player.draw(self.screen)

    # Everything that needs to be updated (non-graphical) goes here
    def update(self):
        self.player.update(self.events)

        # Update all game elements before this point
        pygame.display.update()
        self.clock.tick(30)

game = Game() # Create an instance of the game class

game.start() # Start our instance of the game class

pygame.quit() # When the game.running variables is set back to false, the code resumes here and this line kills the game and all other pygame/python tasks on the machine created by the game