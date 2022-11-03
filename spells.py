import pygame

import lib
import projectile
import particle

class BasicRangedSpell():
    def __init__(self, summonerType: str) -> None:
        """Base class for ranged spells
        
        Arguments:
        level: object - The current game level
        summonerType: str - The indicator of which entity type is casting the spell ["friendly", "hostile"]
        """
        
        self.spellDamage = 0
        self.projectileSize = 1
        self.projectileSpeed = 100
        self.level = lib.levelref
        self.drawContainer = self.level.worldCamera
        self.projectileSound = ""
        self.particleSystem = None
        self.summonerType = summonerType
        self.maxCooldown = 100
        self.cooldown = 0
        self.canBeCast = True

    def update(self) -> None:
        self.cooldown -= 1

        if self.cooldown <= 0:
            self.cooldown = 0
            self.canBeCast = True
        else:
            self.canBeCast = False

    def castSpell(self, originX: int, originY: int, targetX: int, targetY: int) -> None:
        p = projectile.Projectile(originX, originY, targetX, targetY, self.projectileSize, self.projectileSpeed, self.particleSystem, self.drawContainer, self.spellDamage, self.projectileSound)
        if self.summonerType == "friendly":
            self.level.friendlyProjectiles.add(p)
        elif self.summonerType == "hostile":
            self.level.hostileProjectiles.add(p)
        self.level.worldCamera.add(p)
        self.cooldown = self.maxCooldown

class MagicMissle(BasicRangedSpell):
    def __init__(self, summonerType: str) -> None:
        """Magic Missle spell
        
        Arguments:
        level: object - The current game level
        summonerType: str - The indicator of which entity type is casting the spell ["friendly", "hostile"]
        """
        
        super().__init__(summonerType)

        self.spellDamage = 5
        self.projectileSpeed = 200
        self.projectileSize = 3
        self.projectileSound = "magic"
        self.particleSystem = particle.MagicProjectileParticleSystem
        self.maxCooldown = 20

class Fireball(BasicRangedSpell):
    def __init__(self, summonerType: str) -> None:
        """Fireball spell
        
        Arguments:
        level: object - The current game level
        summonerType: str - The indicator of which entity type is casting the spell ["friendly", "hostile"]
        """
        
        super().__init__(summonerType)

        self.spellDamage = 20
        self.projectileSpeed = 100
        self.projectileSize = 6
        self.projectileSound = "fireball"
        self.particleSystem = particle.FireTrailParticleSystem
        self.maxCooldown = 200