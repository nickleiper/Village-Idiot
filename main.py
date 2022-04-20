from CharacterAttribute import Sheet
# the sheet is a template class that is used to build the PC, it is made
#  of three other classes (stats, hitpoints, and skills). To call something
#  in the sheet, type sheet.(name_of_skill/stat/hp).value. See the classes
#  on how to modify the classes.
from CharacterBuilder import build_me_a_pc
#  build_me_a_pc is the name of the character giving module.
from Inventory import Inventory
# another class of classes.
from Home import Home, home_write_up
from Storypath import StoryPath
from Encounter import encounter
#  encounter plays out combat with an enemy whose stats are determined by the parameters of the function when called.


def main():
    pc = Sheet()
    inventory = Inventory()
    build_me_a_pc(pc, inventory)
    home = Home()
    story_path = StoryPath()
    home_write_up(home, pc, story_path)


if __name__ == '__main__':
    main()
