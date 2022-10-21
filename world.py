# Standard imports
import pygame

# Custom imports
import layouts
import projectile
import reference

class Chunk(pygame.sprite.Sprite):
    def __init__(self, x, y, chunkId, room):
        """50x50 pixel building block for the world
        
        Keyword arguments:
        x (int) : the horizontal position of the chunk (top-left)
        y (int) : the vertical position of the chunk (top-left)
        chunkId (int) : the unique id (per room) given to the chunk
        room (class) : the parent of this class, the room it resides
        """
        
        pygame.sprite.Sprite.__init__(self) # Initialize the super class
        
        # Position and size variables
        self.pos = pygame.math.Vector2(x, y) # Vector to store x and y
        self.width = 50 # Hard coded width
        self.height = 50 # Hard coded height

        # Chunk generation variables
        self.chunkId = chunkId # This chunks unique identifier
        self.wall = False # Is this chunk a wall (collidable)
        self.room = room # The master room that owns this chunk
        self.layout = self.room.layout[self.chunkId] # Get our layout (code of what image we get, based on chunkId)
        
        # Set wall based on layout
        if self.layout != 0: # This is the ground tile, when we have different types this will check if self.layout not in _something
            self.wall = True # If we arent a ground tile, we are a wall
        
        # Image variables
        self.image = layouts.tiles[self.layout] # Set the image to the layout.tiles, with our layout code
        self.rect = self.image.get_rect() # Get the rect of the image

    def update(self, player):
        """Update the tile"""

        self.rect.update(self.pos.x, self.pos.y, self.width, self.height) # Keep our rect up to date, just incase we get dynamic world movement in the future (and good practice)

        # Check if we are a wall
        if self.wall: # If we are
            self.collideProjectiles() # Enable our collision detection
            #self.collidePlayer(player)

    #def collidePlayer(self, player):
    #    """Check collisions with the player
    #    
    #    Keyword arguments:
    #    player (object) : The player of the game
    #    """
    #
    #    offset = 10
    #
    #    # If we are in the vertical slice of the object
    #    if self.pos.y < player.pos.y < self.pos.y + self.height:
    #        if self.pos.x < player.pos.x < self.pos.x + self.width:
    #            if player.direction.x > 0: # Moving right
    #                player.pos.x -= offset
    #                player.direction.x = 0
    #            if player.direction.x < 0: # Moving left
    #                #player.pos.x = self.pos.x + self.width + offset
    #                player.direction.x = 0

    def collideProjectiles(self):
        """Check collisions with projectiles"""

        # Check collisions with projectiles
        for p in projectile._projectiles: # Get each projectile
            if self.pos.x < p.pos.x < self.pos.x + self.width: # If its inside of us horizontally
                if self.pos.y < p.pos.y < self.pos.y + self.height: # If its inside of us vertically
                    p.kill() # Murder the fucker

class Room():
    def __init__(self, layout):
        """Serves as the container for all chunks and doors for each 'room'
        
        Keyword arguments:
        layout (class) : index grid from layouts.py
        """
        
        # Room dimensions
        self.width = 1000 # Total width of the room (bust be divisible by 50) - should match window dims
        self.height = 800 # Total height of the room (must be divisible by 50) - should match window dims

        # Adminstrative variables
        self.chunks = pygame.sprite.Group() # Create the sprite group for the chunks
        self.layout = layout # Bind the given layout
        self.doors = [] # Empty list for doors (there will usually be at least one, unless the room is a teleport in/out only)

        # Setup
        self.createChunks() # Populate the chunks group

    def createChunks(self):
        """Create chunks and populate the chunks group"""
        
        chunkId = 0 # Unique id for each chunk

        for y in range(int(self.height / 50)): # Starting with the height means that we orient the grid correctly
            for x in range(int(self.width / 50)): # Go through each horizontal slice of the first vertical slice
                c = Chunk(int(x * 50), int(y * 50), chunkId, self) # Create each chunk, based on where we are in the slices and assign the chunkId and pass the host room (self)
                self.chunks.add(c) # Add the chunk to our chunk group
                chunkId += 1 # Increment the chunkId

    def draw(self, surface):
        """Draws the chunk group
        
        Keyword arguments:
        surface (pygame.surface) : a valid pygame.Surface() needs to be passed here because the rooms are not generated in main.py
        """
        
        self.chunks.draw(surface) # Draw all chunks to screen

    def update(self, player):
        """Update the chunks"""

        self.chunks.update(player) # Call the chunks update function

        # This is messy, but its a workaround for rooms without doors
        try: # Try the following
            for door in self.doors: # For each of our doors
                door.update(player) # Update the door and pass the player
        except: # If the above fails
            pass # Ignore the failure

class Door():
    def __init__(self, x, y, width, height, targetRoom, sx, sy):
        """Object that allows player to move between rooms
        
        Keyword arguments:
        x (int) : the horizontal position of the door (top-left)
        y (int) : the vertical position of the door (top-left)
        width (int) : the width of the doors hitbox
        height (int) : the height of the doors hitbox
        targetRoom (object) : the room that we be loaded when we move through the door
        sx (int) : the horizontal position for the spawn of the player in the targetRoom
        sy (int) : the vertical position for the spawn of the player in the targetRoom
        """

        # Position variables
        self.pos = pygame.math.Vector2(x, y) # Vector to contain the doors x and y
        
        # Hitbox dims
        self.width = width # Width of the hitbox
        self.height = height # Height of the hitbox

        # Non hosted door variables
        self.targetRoom = targetRoom
        self.spawnPos = pygame.math.Vector2(sx, sy)

    def update(self, player):
        """Only really checks for the player in the hitbox
        
        Keyword arguments:
        player (object) : the player object (should be player from main.py
        """
        
        # Hitbox detection
        if self.pos.x < player.pos.x < self.pos.x + self.width: # If the player is horizontally inside hitbox
            if self.pos.y < player.pos.y < self.pos.y + self.height: # Then if the player is vertically inside hitbox
                reference.activeRoom = self.targetRoom # Change the active room to the target room
                player.pos = self.spawnPos # Move the player to the other side of the door (reference spot in new room)

# Creating rooms
startingRoom = Room(layouts.startingRoom)
secondRoom = Room(layouts.secondRoom)
thirdRoom = Room(layouts.thirdRoom)

# Creating doors
doorOne = Door(150, 0, 100, 50, secondRoom, 175, 720) # Door to second room
startingRoom.doors.append(doorOne) # Lives in first room

doorTwo = Door(150, 750, 100, 50, startingRoom, 175, 75) # Door to first room
secondRoom.doors.append(doorTwo) # Lives in second room

doorThree = Door(950, 250, 50, 100, thirdRoom, 75, 275) # Door to third room
secondRoom.doors.append(doorThree) # Also lives in second room

doorFour = Door(0, 250, 50, 100, secondRoom, 875, 275) # Door to second room
thirdRoom.doors.append(doorFour) # Lives in third room