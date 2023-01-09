# Standard library imports
import pygame

# Custom class imports
import item
assetPath = "assets/.resources/"
assetDict = {}
assetDict["katana"] = pygame.image.load(assetPath+"katana.png")
assetDict["katanaLg"] = pygame.image.load(assetPath+"katanaLg.png")
assetDict["pistol"] = pygame.image.load(assetPath+"basicPistol.png")
#------------- Weapon Library ---------------#
#                                            #
## Starter Pistol ##
pistol1 = item.Weapon("Pistol","A pistol that you start the game with. Good luck.",assetDict["pistol"],None,1,1,True,False)
####################

# ## Starter Secondary ##
katana1 = item.Weapon("Katana","A semi-dull katana that you start the game with. Good luck.",assetDict["katana"],assetDict["katanaLg"],1,1.1,False,False)
# knife1.itemName = "Butter Knife"
# knife1.itemDescription = "Your only line of defense when things get too close. Hope it isn't plastic."
# #######################

# ### Melee Weapons ###
# sword1 = item.Weapon(5,2,False,False)
# sword1.itemName = "Short Sword"
# sword1.itemDescription = "A knight's Trusty Weapon"
########################

#### Hand Guns ####

###################

## Automatic Guns ##

####################

#                                            #
#--------------------------------------------#


# #--------------- Magic Library --------------#
# #                                            #
# #Destruction Magics#
# iceMagic1 = item.DestructionMagic(5,1,2)
# iceMagic1.itemName = "Icicle of Murderous Intent"
# iceMagic1.itemDescription = "Shoots a spike of ice that homes in on the nearest enemy and exploads on contact dealing its damage in an AOE."
# iceMagic1.miniBossSoulPrice = 1
# iceMagic1.mobSoulPrice = 50

# fireMagic1 = item.DestructionMagic(500,10,1)
# fireMagic1.itemName = "Soul Flare"
# fireMagic1.itemDescription = "A burning flare erupts from you dealing massive damage to whatever it hits"
# fireMagic1.regionBossSoulPrice = 2 
# fireMagic1.miniBossSoulPrice = 2 
# fireMagic1.requiresManySoulTypes = True

# shockMagic1 = item.DestructionMagic(250, 7, 1)
# shockMagic1.itemName = "Lightning Storm"
# shockMagic1.itemDescription = "Call down a lightning storm at a location, damaging and stunning enemies over time"
# shockMagic1.regionBossSoulPrice = 1
# shockMagic1.miniBossSoulPrice = 1
# shockMagic1.requiresManySoulTypes = True

# shockMagic2 = item.DestructionMagic(5, 1, 2)                      #Starter Spell 0 cost
# shockMagic2.itemName = "Sparks"
# shockMagic2.itemDescription = "Shoots out a shower of sparks that deal damage and temporarily stun enemies"
# shockMagic2.mobSoulPrice = 0
# shockMagic2.requiresManySoulTypes = False

# ####################

# ## Restoration Magics ##
# healMagic1 = item.RestorationMagic(5,1,2)
# healMagic1.itemName = "Basic Heal"
# healMagic1.itemDescription = "Knits small wounds back together healing 5HP."
# healMagic1.mobSoulPrice = 10
# ########################

#                                            #
#--------------------------------------------#
