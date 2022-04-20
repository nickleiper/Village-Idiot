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
    pc = Sheet()    # Class 'Sheet' is used to house all the stuff a pc might need to call upon including skills
                    # this brings a sheet into the main to be used by the PC.
    inventory = Inventory()     # logs weapons possessed, their damage, and relevant stats, as well as quest items.
                                # Works simililarly to Sheet.
    build_me_a_pc(pc, inventory)    # fills out PC sheet with stats depending on answers to a quiz.
    home = Home()                   # home is a starting point the PC will return to between quests. It is also a class.
    story_path = StoryPath()        # things get messy here. houses all the quests, as well as their status. Directs
                                    # main to quests housed inside the story path.
    story_path.dev_storypath()      # This sets up the storypath
    home_write_up(home, pc, inventory, story_path) # how home presents itself to the player and gives them options.


if __name__ == '__main__':
    main()
