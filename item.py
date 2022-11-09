# Standard Library Imports
import pygame

# Generic Base Item Class
# Contains base attributes that all items may have
class Item():
    def __init__(self, itemName, itemDescription, img, lgImg = None):
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.img = img
        self.lgImg = lgImg
        
        # Item price variables
        self.requiresManySoulTypes = False         # If false, only one price must be paid. If true, all prices must be paid. EX: FALSE = Item costs 1 mini boss OR 50 mobs. TRUE = Item costs 1 mini boss AND 50 mobs.
        self.mobSoulPrice = 0
        self.miniBossSoulPrice = 0
        self.regionBossSoulPrice = 0
        
# Weapon Subclass
# Has all attributes of Item class
## Can be be part of the same loadout as another 
## weapon as long is they're both one handed. Maybe 
## hot swap between them on a keybind.
class Weapon(Item):
    def __init__(self, itemName, itemDescription, imgIcn, lgImg, damage, atkSpeed, isRanged, isTwoHanded):
        super().__init__(itemName, itemDescription, imgIcn, lgImg)
        self.isTwoHanded = isTwoHanded
        self.isRanged = isRanged
        self.damage = damage
        self.atkSpeed = atkSpeed


