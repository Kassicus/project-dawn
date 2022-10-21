import pygame

# Grid layout for the starting room
startingRoom = [
    13, 13, 4, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    13, 12, 8, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 9, 13,
    13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13
]

# Grid layout for the second room
secondRoom = [
    13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    13, 12, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 1,
    13, 4, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    13, 4, 0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 2,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 3, 13,
    13, 10, 6, 0, 0, 5, 2, 2, 2, 2, 2, 2, 2, 15, 2, 2, 2, 2, 9, 13,
    13, 13, 4, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13
]

# Grid layout for the third room
thirdRoom = [
    13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    13, 12, 1, 1, 1, 1, 11, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    13, 4, 0, 0, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    13, 4, 0, 0, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    1, 8, 0, 0, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    0, 0, 0, 0, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    0, 0, 0, 0, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    2, 6, 0, 0, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    13, 4, 0, 0, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    13, 4, 0, 0, 0, 0, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 13,
    13, 10, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 9, 13,
    13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13
]

# Dictionary of all sprites
sprites = {
    "floor" : pygame.image.load("assets/tiles/ground/brick_test.png"),
    "bottomFlat" : pygame.image.load("assets/tiles/walls/bottom_flat.png"),
    "topFlat" : pygame.image.load("assets/tiles/walls/top_flat.png"),
    "leftFlat" : pygame.image.load("assets/tiles/walls/left_flat.png"),
    "rightFlat" : pygame.image.load("assets/tiles/walls/right_flat.png"),
    "topLeft" : pygame.image.load("assets/tiles/walls/top_left.png"),
    "topRight" : pygame.image.load("assets/tiles/walls/top_right.png"),
    "bottomLeft" : pygame.image.load("assets/tiles/walls/bottom_left.png"),
    "bottomRight" : pygame.image.load("assets/tiles/walls/bottom_right.png"),
    "topLeftInvert" : pygame.image.load("assets/tiles/walls/top_left_invert.png"),
    "topRightInvert" : pygame.image.load("assets/tiles/walls/top_right_invert.png"),
    "bottomLeftInvert" : pygame.image.load("assets/tiles/walls/bottom_left_invert.png"),
    "bottomRightInvert" : pygame.image.load("assets/tiles/walls/bottom_right_invert.png"),
    "outOfBounds" : pygame.image.load("assets/tiles/walls/out_of_bounds.png"),
    "bottomDoubleInvert" : pygame.image.load("assets/tiles/walls/bottom_double_invert.png"),
    "topDoubleInvert" : pygame.image.load("assets/tiles/walls/top_double_invert.png"),
    "leftDoubleInvert" : pygame.image.load("assets/tiles/walls/left_double_invert.png"),
    "rightDoubleInvert" : pygame.image.load("assets/tiles/walls/right_double_invert.png"),
    "topBottomFlat" : pygame.image.load("assets/tiles/walls/top_bottom_flat.png"),
    "leftRightFlat" : pygame.image.load("assets/tiles/walls/left_right_flat.png"),
    "topU" : pygame.image.load("assets/tiles/walls/top_u.png"),
    "bottomU" : pygame.image.load("assets/tiles/walls/bottom_u.png"),
    "leftU" : pygame.image.load("assets/tiles/walls/left_u.png"),
    "rightU" : pygame.image.load("assets/tiles/walls/right_u.png"),
}

# List of all tiles, reference the index to get the corresponding image
tiles = [
    sprites["floor"], # 0
    sprites["bottomFlat"], # 1
    sprites["topFlat"], # 2
    sprites["leftFlat"], # 3
    sprites["rightFlat"], # 4
    sprites["topLeft"], # 5
    sprites["topRight"], # 6
    sprites["bottomLeft"], # 7
    sprites["bottomRight"], # 8
    sprites["topLeftInvert"], # 9
    sprites["topRightInvert"], # 10
    sprites["bottomLeftInvert"], # 11
    sprites["bottomRightInvert"], # 12
    sprites["outOfBounds"], # 13
    sprites["bottomDoubleInvert"], # 14
    sprites["topDoubleInvert"], # 15
    sprites["leftDoubleInvert"], # 16
    sprites["rightDoubleInvert"], # 17
    sprites["topBottomFlat"], # 18
    sprites["leftRightFlat"], # 19
    sprites["topU"], # 20
    sprites["bottomU"], # 21
    sprites["leftU"], # 22
    sprites["rightU"], # 23
]