import pygame

starter_room = [
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

test_room = [
    13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
    13, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 13,
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
    13, 10, 6, 0, 0, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 9, 13,
    13, 13, 4, 0, 0, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13
]

sprites = {
    "floor" : pygame.image.load("assets/tiles/ground/brick_test.png"),
    "bottom_flat" : pygame.image.load("assets/tiles/walls/bottom_flat.png"),
    "top_flat" : pygame.image.load("assets/tiles/walls/top_flat.png"),
    "left_flat" : pygame.image.load("assets/tiles/walls/left_flat.png"),
    "right_flat" : pygame.image.load("assets/tiles/walls/right_flat.png"),
    "top_left" : pygame.image.load("assets/tiles/walls/top_left.png"),
    "top_right" : pygame.image.load("assets/tiles/walls/top_right.png"),
    "bottom_left" : pygame.image.load("assets/tiles/walls/bottom_left.png"),
    "bottom_right" : pygame.image.load("assets/tiles/walls/bottom_right.png"),
    "top_left_invert" : pygame.image.load("assets/tiles/walls/top_left_invert.png"),
    "top_right_invert" : pygame.image.load("assets/tiles/walls/top_right_invert.png"),
    "bottom_left_invert" : pygame.image.load("assets/tiles/walls/bottom_left_invert.png"),
    "bottom_right_invert" : pygame.image.load("assets/tiles/walls/bottom_right_invert.png"),
    "out_of_bounds" : pygame.image.load("assets/tiles/walls/out_of_bounds.png")
}

tiles = [
    sprites["floor"], # 0
    sprites["bottom_flat"], # 1
    sprites["top_flat"], # 2
    sprites["left_flat"], # 3
    sprites["right_flat"], # 4
    sprites["top_left"], # 5
    sprites["top_right"], # 6
    sprites["bottom_left"], # 7
    sprites["bottom_right"], # 8
    sprites["top_left_invert"], # 9
    sprites["top_right_invert"], # 10
    sprites["bottom_left_invert"], # 11
    sprites["bottom_right_invert"], # 12
    sprites["out_of_bounds"], # 13
]

active_layout = starter_room