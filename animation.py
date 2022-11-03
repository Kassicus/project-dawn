import lib

class Animation():
    def __init__(self, frames, animationSpeed):
        """Creates a playable animation
        
        Keyword arguments:
        frames (list) : The list of individual images in the animation
        animationSpeed (int) : The speed the animation gets played at
        """
        
        self.frames = frames # All of the images
        self.frameIndex = 0 # The current image we are on

        self.animationSpeed = animationSpeed # Animation speed... simple...

    def animate(self):
        """Do the animation
        
        Returns:
        image (pygame.Surface) : The current image of the animation
        """

        self.frameIndex += self.animationSpeed * lib.deltaTime # Increase our frame index at a rate that is independant of game framerate
        if self.frameIndex > len(self.frames): # If the frame index is too high
            self.frameIndex = 0 # Reset it
        image = self.frames[int(self.frameIndex)] # Get the new image
        return image # Return that image
