# Standard library imports
import os
import pygame
import pygame.color

import pygame.freetype as freetype

class Button():
    def __init__(self,x,y,width,height,btnTxtColor,btnTxt,btnTxtSize):
        """
        Object for interactable sub elements in UI/Menus
        x: x coordinate for the origin point of the button
        y: y coordinate for the origin point of the button
        width: width of the button
        height: height of the button
        btnTxtColor: color of text that is on the button
        btnTxt: Text that will appear on the button
        """
        font = freetype.Font("data/Orbitron-Regular.ttf")
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width,height),pygame.SRCALPHA)
        self.btnTxt = btnTxt
        self.btnTxtColor = btnTxtColor
        self.isHovered = False
        self.isActive = False
        self.screenNum = 0
        self.linkedSection2DictKey = ""
        self.linkedSection3DictKey = ""
        self.btnTxtRect = font.get_rect(btnTxt , size = btnTxtSize)
        self.btnTxtRect.center = self.surface.get_rect().center
