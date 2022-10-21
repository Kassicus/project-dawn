# Standard library imports
import os
import pygame
import pygame.color

class Button():
    def __init__(self,x,y,width,height,btnTxtColor):
        """
        Object for interactable sub elements in UI/Menus
        x: x coordinate for the origin point of the button
        y: y coordinate for the origin point of the button
        width: width of the button
        height: height of the button
        btnTxtColor: color of text that is on the button
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width,height),pygame.SRCALPHA)
        self.btnTxtColor = btnTxtColor
        self.isActive = False
        self.linkedSection2DictKey = ""
        self.linkedSection3DictKey = ""
