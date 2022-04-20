from CharacterClass import Stat, HitPoints, Skill


class Sheet:
    def __init__(self):
        # Stats
        self.brawn = Stat(0)
        self.brain = Stat(0)
        self.quick = Stat(0)
        self.charm = Stat(0)
        self.will = Stat(0)
        # HP
        self.hp = HitPoints(0, 0)
        # Skills
        self.melee_weapon = Skill(0)
        self.ranged_weapon = Skill(0)
        # charm skills
        self.talk = Skill(0)
        self.intimidate = Skill(0)
        self.lie = Skill(0)
        # quick skills
        self.retreat = Skill(0)
        self.stealth = Skill(0)
        self.pickpocket = Skill(0)
        self.acrobat = Skill(0)
        # brawn skills
        self.force = Skill(0)
        self.athlete = Skill(0)
        # brain skills
        self.know = Skill(0)
        self.detect = Skill(0)
        self.design = Skill(0)
        # will skills
        self.pray = Skill(0)
        self.brave = Skill(0)
