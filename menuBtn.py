# Standard library imports
import os
import string
import pygame
import pygame.color

import pygame.freetype as freetype

class Button():
    def __init__(self,x,y,width,height,btnTxtColor,btnTxt,btnTxtSize,bkImg:str=None,img:str=None):
        """
        Object for interactable sub elements in UI/Menus
        x: x coordinate for the origin point of the button
        y: y coordinate for the origin point of the button
        width: width of the button
        height: height of the button
        btnTxtColor: color of text that is on the button
        btnTxt: text that will appear on the button
        btnTxtSize: size of text to show on button
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
        self.btnTxtRect = font.get_rect(btnTxt , size = btnTxtSize)
        self.btnTxtRect.center = self.surface.get_rect().center

        if bkImg is not None:
            self.bkImg = pygame.image.load(bkImg)
            bkImgXCent = self.x+self.width / 2 - self.bkImg.get_width() / 2
            bkImgYCent = self.y+self.height / 2 - self.bkImg.get_height() / 2 #similarly..
            self.bkImgCent = (bkImgXCent,bkImgYCent)
        if img is not None:
            self.img = pygame.image.load(img)
            imgXCent = self.x+self.width / 2 - self.img.get_width() / 2
            imgYCent = self.y+self.height / 2 - self.img.get_height() / 2 #similarly..
            self.imgCent = (imgXCent,imgYCent)
