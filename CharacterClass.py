class Stat:
    def __init__(self, value):
        self.value = value

    def grow(self, amount):
        self.value += amount

    def shrink(self, amount):
        self.value += amount

    def read_out(self):
        return self.value


'''Stats are the class used to describe the brawn, brain, quick, charm, and will. This class is referenced in the 
broader sheet category.'''


class HitPoints:
    def __init__(self, maxhp, value):
        self.maxhp = maxhp
        self.value = value

    def hit(self, amount):
        self.value -= amount

    def heal(self, amount):
        if self.value + amount <= self.maxhp:
            self.value += amount
        if self.value + amount > self.maxhp:
            self.value += self.maxhp - self.value

    def grow(self, amount):
        self.maxhp += amount
        self.value = int(self.maxhp)

    def shrink(self, amount):
        self.maxhp -= amount
        self.value = int(self.maxhp)

    def read_out_max(self):
        return self.maxhp

    def read_out_current(self):
        return self.value


'''HP is also seen in the broader sheet class that is referenced throughout the main and character builder.'''


class Skill:
    def __init__(self, value):
        self.value = value

    def grow(self, amount):
        self.value += amount

    def shrink(self, amount):
        self.value += amount

    def read_out(self):
        return self.value


'''Vv similar to the stats class, see CharacterAttribute for the sheet.'''
