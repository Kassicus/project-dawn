#Standard library imports
import itemLib

class Inventory():
    """
    A class that deals with anything that needs an inventory. Stores/Players/Bosses
    """
    def __init__(self) -> None:
        self.inventory = {}

    # a function to add an item to a player's inventory
    def addItem(self, item, inventorySlot):
        """
        A method for adding items to an inventory instance

        item: an item object
        inventorySlot: key to the inventory dictionary for stored items
        """
        self.inventory[inventorySlot] = item

class PlayerInventory(Inventory):
    """
    A class specifically for Player Inventory 
    """
    def __init__(self) -> None:
        super().__init__()
        self.key = "slot"

        self.loadout = {}
        self.loadout["slot1"] = itemLib.pistol1
        self.loadout["slot2"] = itemLib.katana1
        self.loadout["slot3"] = None
        self.loadout["slot4"] = None
        self.loadout["slot5"] = None

        self.inventory["slot1"] = itemLib.pistol1
        self.inventory["slot2"] = itemLib.katana1
        self.inventory["slot3"] = itemLib.katana1
        self.inventory["slot4"] = itemLib.katana1
        self.inventory["slot5"] = itemLib.katana1
        self.inventory["slot6"] = itemLib.katana1
        self.inventory["slot7"] = itemLib.katana1
        self.inventory["slot8"] = itemLib.katana1
        self.inventory["slot9"] = itemLib.katana1
        self.inventory["slot10"] = itemLib.pistol1
        self.inventory["slot11"] = itemLib.pistol1
        self.inventory["slot12"] = itemLib.pistol1
        self.inventory["slot13"] = itemLib.pistol1
        self.inventory["slot14"] = itemLib.pistol1
        self.inventory["slot15"] = itemLib.pistol1
        self.inventory["slot16"] = itemLib.pistol1
        self.inventory["slot17"] = itemLib.pistol1
        self.inventory["slot18"] = itemLib.katana1
        self.inventory["slot19"] = itemLib.katana1
        self.inventory["slot20"] = itemLib.katana1
        self.inventory["slot21"] = itemLib.pistol1
        self.inventory["slot22"] = itemLib.pistol1
        self.inventory["slot23"] = itemLib.pistol1
        self.inventory["slot24"] = itemLib.pistol1