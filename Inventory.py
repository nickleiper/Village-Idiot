class Weapon:
    def __init__(self, possession, type, damage, bonus):
        self.possession = possession
        self.type = type
        self.damage = damage
        self.bonus = bonus

    def acquire(self):
        self.possession = True

    def do_i_have(self):
        return self.possession


'''Weapons are a bit more complex than misc but not much more.'''


class misc:
    def __init__(self, possession):
        self.possession = possession

    def acquire(self):
        self.possession = True

    def do_i_have(self):
        return self.possession


class Inventory:
    def __init__(self):
        # weapons
        self.fists = Weapon(True, "melee", 2, 0)
        self.dagger = Weapon(False, "melee", 3, 3)
        self.club = Weapon(False, "melee", 4, 0)
        self.sword = Weapon(False, "melee", 6, 1)
        self.great_sword = Weapon(False, "melee", 8, 1)
        self.war_axe = Weapon(False, "melee", 9, 0)
        self.slingshot = Weapon(True, "ranged", 1, 0)
        self.bow_arrow = Weapon(False, "ranged", 4, 0)
        self.crossbow = Weapon(False, "ranged", 6, 2)
        self.musket = Weapon(False, "ranged", 10, 0)
