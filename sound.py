import pygame

pygame.mixer.init() # Initialize the mixer

sounds = { # Create all of the sounds
    "fireball" : pygame.mixer.Sound("assets/audio/fireball.wav"),
    "fireball 2" : pygame.mixer.Sound("assets/audio/fireball_2.wav"),
    "magic" : pygame.mixer.Sound("assets/audio/magic_shot.wav")
}

def playSound(sound):
    """Plays a sound
    
    Keyword arguments:
    sound (pygame.Sound) : The dictionary key for the sound we want to play
    """
    
    pygame.mixer.Sound.set_volume(sounds[sound], 0.5) # Reduce the volume (shits loud)
    pygame.mixer.Sound.play(sounds[sound]) # Play the sound
    pygame.mixer.Sound.fadeout(sounds[sound], 750) # Create a nice fadeout after the sound is played