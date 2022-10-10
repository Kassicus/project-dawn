# Standard Library Imports
import pygame

# Generic Base Item Class
# Contains base attributes that all items may have
class Item():
    def __init__(self, itemName, itemDescription):
        self.itemName = itemName
        self.itemDescription = itemDescription
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
    def __init__(self, damage, atkSpeed, isRanged, isTwoHanded):
        self.isTwoHanded = isTwoHanded
        self.isRanged = isRanged
        self.damage = damage
        self.atkSpeed = atkSpeed

# Two Handed Weapon Subclass
# Has all attributes of Item class
## Takes up both hands. So can't weapon swap.
## More powerful than a one handed weapon.
## Maybe give them an active ability?
###class TwoHandedWeapon(Item):
###    def __init__(self):
###        self.isTwoHanded = True
###        self.isRanged
###        self.damage = 2
###        self.atkSpeed = 0

# Offensive Magic Subclass
# Has all attributes of Item class
## Takes up its own slot on the hotbar.Thus
## can be used alongside the players weapon choice.
## Variety of effects (depending on how crazy we get)
class DestructionMagic(Item):
    def __init__(self, damage, coolDownTimer, magicCharges):
        self.damage = damage
        self.coolDownTimer = coolDownTimer
        self.magicCharges = magicCharges

# Healing Magic Subclass
# Has all attributes of Item class
## Purchasable with souls. Allows player to heal during
## combat a variable amount of times.
class RestorationMagic(Item):
    def __init__(self, healAmount, coolDownTimer, magicCharges):
        self.healAmount = healAmount
        self.coolDownTimer = coolDownTimer
        self.magicCharges = magicCharges
        pass
