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
        # Python screen setup
        self.screen = pygame.display.set_mode([reference.SCREEN_WIDTH, reference.SCREEN_HEIGHT])
        pygame.display.set_caption(reference.SCREEN_TITLE)

        # Game management variables
        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get() # Capturing this request into a variable to be used in other locations
        self.debugInterface = debug.DebugInterface()

        # Game object instances
        self.player = player.Player()
        self.healthBar = ui.StatusBar(10, 10, 200, 30, (87, 11, 6), (255, 0, 0), self.player.health, 100)
        self.pMenu = menu.PlayerInventoryMenu(50, 45, (120,113,93,120), (0,150,0))

        # Set the current room to the "starting room" from the world file
        reference.activeRoom = world.startingRoom

    # This function starts the game, but also starts the game loop, it determines the order of logic
    def start(self):
        while self.running:
            self.events = pygame.event.get()

            # Main event loop
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

                """
                TESTING
                [y]: decrease player health
                [u]: increase player health

                [m]: show menu

                [j]: emit smoke blast from player (only supports left and right currently)
                [k]: emit particle impact (static position currently)
                [i]: Display your inventory in the terminal (Graphical display are a WIP)
                [,]: Adds a short sword to your inventory
                """
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_u:
                        if self.player.health <= 90:
                            self.player.health += 10
                    if event.key == pygame.K_y:
                        if self.player.health >= 10:
                            self.player.health -= 10
                    if event.key == pygame.K_m:
                        if self.pMenu.isDrawn == False:
                            self.pMenu.isDrawn = True
                        else:
                            self.pMenu.isDrawn = False
                    if event.key == pygame.K_TAB:
                        if self.debugInterface.active:
                            self.debugInterface.active = False
                        else:
                            self.debugInterface.active = True
                    if event.key == pygame.K_i:
                        print("Your inventory consists of:\n ")
                        for x in self.player.inventory:
                            print(x.itemName +":", x.itemDescription)
                        print("")
                    if event.key == pygame.K_COMMA:
                        inventory.addItem(self.player.inventory, itemLib.sword1)
                """
                TESTING
                """

            self.draw()

            self.update()

    # Everything that needs to be drawn (graphical-updates) goes here
    def draw(self):
        self.screen.fill(reference.BLACK)

        reference.activeRoom.draw(self.screen) # This is kindof a group too?
        
        projectile._projectiles.draw(self.screen) # Groups should be the only thing that still need a surface passed?

        self.player.draw()
        self.healthBar.draw()

        if self.pMenu.isDrawn == True:
            self.pMenu.draw()

        if self.debugInterface.active:
            self.debugInterface.draw()

    # Everything that needs to be updated (non-graphical) goes here
    def update(self):
        self.player.update(self.events)
        self.healthBar.update(self.player.health)

        # See above disclaimer for this...
        projectile._projectiles.update()

        # Update all game elements before this point
        reference.activeRoom.update(self.player)
        self.debugInterface.update(self.clock, self.player)
        pygame.display.update()
        reference.dt = self.clock.tick() / 1000

if __name__ == '__main__':
    game = Game() # Create an instance of the game class
    game.start() # Start our instance of the game class
    pygame.quit() # When the game.running variables is set back to false, the code resumes here and this line kills the game and all other pygame/python tasks on the machine created by the game
    